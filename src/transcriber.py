"""Transcription using faster-whisper with GPU/CPU auto-detection"""

import time
from typing import List, Dict, Optional
from dataclasses import dataclass

from .utils import check_gpu_available, print_progress


@dataclass
class TranscriptionSegment:
    """A single transcription segment with timing"""
    start: float
    end: float
    text: str


@dataclass
class TranscriptionResult:
    """Complete transcription result"""
    segments: List[TranscriptionSegment]
    language: str
    duration: float
    method: str  # "gpu" or "cpu"
    model_used: str
    transcription_time: float


class Transcriber:
    """Transcribe audio using Whisper"""

    def __init__(
        self,
        model_preference: str = "auto",
        custom_vocabulary: Optional[List[str]] = None,
        common_corrections: Optional[Dict[str, str]] = None,
        language: str = "en"
    ):
        """
        Initialize the transcriber.

        Args:
            model_preference: Model to use (auto, tiny, base, small, medium, large)
            custom_vocabulary: List of terms to recognize correctly
            common_corrections: Dict of misheard terms -> correct terms
            language: Target language code
        """
        self.custom_vocabulary = custom_vocabulary or []
        self.common_corrections = common_corrections or {}
        self.language = language
        self.use_gpu = check_gpu_available()

        # Select model based on preference and available resources
        self.model_name = self._select_model(model_preference)

        print_progress(
            f"Initializing transcriber with {self.model_name} model "
            f"({'GPU' if self.use_gpu else 'CPU'})"
        )

        # Initialize the Whisper model
        self._initialize_model()

    def _select_model(self, preference: str) -> str:
        """
        Select appropriate model based on preference and resources.

        Args:
            preference: Model preference string

        Returns:
            Model name to use
        """
        if preference != "auto":
            return preference

        # Auto-select based on available resources
        if self.use_gpu:
            return "medium"  # Good balance for GPU
        else:
            return "base"    # Faster for CPU

    def _initialize_model(self):
        """Initialize the Whisper model"""
        try:
            from faster_whisper import WhisperModel

            device = "cuda" if self.use_gpu else "cpu"
            compute_type = "float16" if self.use_gpu else "int8"

            print_progress(f"Loading {self.model_name} model on {device}...")

            self.model = WhisperModel(
                self.model_name,
                device=device,
                compute_type=compute_type,
                download_root="/data/temp/whisper_models"
            )

            print_progress(f"Model loaded successfully", "success")

        except Exception as e:
            raise RuntimeError(f"Failed to initialize Whisper model: {e}")

    def _build_initial_prompt(self) -> Optional[str]:
        """
        Build initial prompt with custom vocabulary.

        Returns:
            Initial prompt string or None
        """
        if not self.custom_vocabulary:
            return None

        # Use all vocabulary terms in a natural format
        # Whisper works better with multiple short sentences
        vocab_chunks = []
        chunk_size = 10

        for i in range(0, len(self.custom_vocabulary), chunk_size):
            chunk = self.custom_vocabulary[i:i + chunk_size]
            vocab_chunks.append(", ".join(chunk))

        # Create prompt with all terms distributed across sentences
        prompt_parts = []
        for i, chunk in enumerate(vocab_chunks):
            if i == 0:
                prompt_parts.append(f"This video discusses {chunk}.")
            else:
                prompt_parts.append(f"It also covers {chunk}.")

        return " ".join(prompt_parts)

    def _apply_corrections(self, text: str) -> str:
        """
        Apply common corrections to transcribed text.

        Args:
            text: Original transcribed text

        Returns:
            Corrected text
        """
        if not self.common_corrections:
            return text

        corrected_text = text

        # Apply each correction (case-insensitive)
        for wrong_term, correct_term in self.common_corrections.items():
            # Replace case-insensitively while preserving original case pattern
            import re

            # Try to match with word boundaries to avoid partial replacements
            pattern = re.compile(re.escape(wrong_term), re.IGNORECASE)
            corrected_text = pattern.sub(correct_term, corrected_text)

        return corrected_text

    def transcribe(self, audio_path: str) -> TranscriptionResult:
        """
        Transcribe an audio file.

        Args:
            audio_path: Path to audio file

        Returns:
            TranscriptionResult object

        Raises:
            RuntimeError: If transcription fails
        """
        print_progress(f"Starting transcription of {audio_path}")

        start_time = time.time()

        try:
            # Build initial prompt with vocabulary
            initial_prompt = self._build_initial_prompt()

            if initial_prompt:
                print_progress(f"Using custom vocabulary: {', '.join(self.custom_vocabulary[:5])}...")

            # Transcribe
            segments_iter, info = self.model.transcribe(
                audio_path,
                language=self.language,
                initial_prompt=initial_prompt,
                beam_size=5,
                vad_filter=True,  # Voice activity detection
                vad_parameters=dict(
                    min_silence_duration_ms=500
                )
            )

            # Convert segments to our format and apply corrections
            segments = []
            corrections_applied = 0

            for segment in segments_iter:
                original_text = segment.text.strip()
                corrected_text = self._apply_corrections(original_text)

                if corrected_text != original_text:
                    corrections_applied += 1

                segments.append(TranscriptionSegment(
                    start=segment.start,
                    end=segment.end,
                    text=corrected_text
                ))

            if corrections_applied > 0:
                print_progress(f"Applied {corrections_applied} automatic corrections")

            transcription_time = time.time() - start_time

            print_progress(
                f"Transcription complete in {transcription_time:.1f}s "
                f"({len(segments)} segments)",
                "success"
            )

            return TranscriptionResult(
                segments=segments,
                language=info.language,
                duration=info.duration,
                method="gpu" if self.use_gpu else "cpu",
                model_used=self.model_name,
                transcription_time=transcription_time
            )

        except Exception as e:
            raise RuntimeError(f"Transcription failed: {e}")

    def estimate_time(self, duration_seconds: int) -> str:
        """
        Estimate transcription time.

        Args:
            duration_seconds: Audio duration in seconds

        Returns:
            Estimated time string
        """
        if self.use_gpu:
            # GPU is typically 15-30x realtime
            multiplier = 20
        else:
            # CPU is typically 0.5-1x realtime
            multiplier = 1

        estimated_seconds = duration_seconds / multiplier

        minutes = int(estimated_seconds // 60)
        seconds = int(estimated_seconds % 60)

        return f"~{minutes}m {seconds}s"
