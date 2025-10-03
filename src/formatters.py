"""Output formatters for transcription results"""

from datetime import datetime
from pathlib import Path
from typing import Dict

from .transcriber import TranscriptionResult
from .utils import format_timestamp_link, ensure_directory, print_progress


class MarkdownFormatter:
    """Format transcription as Markdown with frontmatter"""

    def __init__(self, output_dir: str = "data/transcripts"):
        """
        Initialize the formatter.

        Args:
            output_dir: Directory to save markdown files
        """
        self.output_dir = ensure_directory(output_dir)

    def format(
        self,
        result: TranscriptionResult,
        video_info: Dict,
        style: str = "timestamped"
    ) -> str:
        """
        Format transcription result as Markdown.

        Args:
            result: TranscriptionResult from transcriber
            video_info: Video metadata from downloader
            style: Output style ("timestamped" or "continuous")

        Returns:
            Formatted markdown string
        """
        # Build frontmatter
        frontmatter = self._build_frontmatter(result, video_info)

        # Build transcript body
        if style == "timestamped":
            body = self._format_timestamped(result, video_info["video_id"])
        else:
            body = self._format_continuous(result)

        # Combine
        markdown = f"{frontmatter}\n\n# {video_info['title']}\n\n{body}"
        markdown += "\n\n---\n\n*Automatically generated transcript. May contain errors.*\n"

        return markdown

    def _build_frontmatter(self, result: TranscriptionResult, video_info: Dict) -> str:
        """Build YAML frontmatter"""
        # Format upload date
        upload_date = video_info.get("upload_date", "")
        if upload_date and len(upload_date) == 8:  # YYYYMMDD
            upload_date = f"{upload_date[:4]}-{upload_date[4:6]}-{upload_date[6:8]}"

        # Count words
        word_count = sum(len(seg.text.split()) for seg in result.segments)

        # Escape quotes in strings
        title = video_info['title'].replace('"', r'\"')
        description = video_info.get('description', '')[:200].replace('"', r'\"')

        frontmatter = f"""---
video_id: "{video_info['video_id']}"
title: "{title}"
description: "{description}..."
channel_name: "{video_info['channel_name']}"
channel_id: "{video_info['channel_id']}"
published_at: "{upload_date}"
duration_seconds: {video_info['duration_seconds']}
youtube_url: "{video_info['youtube_url']}"
thumbnail_url: "{video_info['thumbnail_url']}"

# Transcription metadata
transcribed_at: "{datetime.now().isoformat()}"
transcription_method: "{result.method}"
model_used: "{result.model_used}"
language: "{result.language}"
word_count: {word_count}
transcription_time_seconds: {result.transcription_time:.1f}
---"""
        return frontmatter

    def _format_timestamped(self, result: TranscriptionResult, video_id: str) -> str:
        """Format with clickable timestamps"""
        lines = []

        for segment in result.segments:
            timestamp_link = format_timestamp_link(segment.start, video_id)
            lines.append(f"{timestamp_link} {segment.text}")

        return "\n\n".join(lines)

    def _format_continuous(self, result: TranscriptionResult) -> str:
        """Format as continuous text without timestamps"""
        return " ".join(seg.text for seg in result.segments)

    def save(
        self,
        result: TranscriptionResult,
        video_info: Dict,
        style: str = "timestamped"
    ) -> str:
        """
        Format and save transcription to file.

        Args:
            result: TranscriptionResult from transcriber
            video_info: Video metadata from downloader
            style: Output style

        Returns:
            Path to saved file
        """
        markdown = self.format(result, video_info, style)

        output_file = self.output_dir / f"{video_info['video_id']}.md"

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(markdown)

        print_progress(f"Transcript saved to {output_file}", "success")

        return str(output_file)


class SRTFormatter:
    """Format transcription as SRT subtitle file"""

    def __init__(self, output_dir: str = "data/transcripts"):
        """
        Initialize the formatter.

        Args:
            output_dir: Directory to save SRT files
        """
        self.output_dir = ensure_directory(output_dir)

    def _format_timestamp(self, seconds: float) -> str:
        """Format seconds as SRT timestamp (HH:MM:SS,mmm)"""
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        millis = int((seconds % 1) * 1000)

        return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"

    def format(self, result: TranscriptionResult) -> str:
        """
        Format transcription result as SRT.

        Args:
            result: TranscriptionResult from transcriber

        Returns:
            Formatted SRT string
        """
        lines = []

        for i, segment in enumerate(result.segments, 1):
            start = self._format_timestamp(segment.start)
            end = self._format_timestamp(segment.end)

            lines.append(f"{i}")
            lines.append(f"{start} --> {end}")
            lines.append(segment.text)
            lines.append("")  # Empty line between segments

        return "\n".join(lines)

    def save(self, result: TranscriptionResult, video_id: str) -> str:
        """
        Format and save transcription to SRT file.

        Args:
            result: TranscriptionResult from transcriber
            video_id: YouTube video ID

        Returns:
            Path to saved file
        """
        srt = self.format(result)

        output_file = self.output_dir / f"{video_id}.srt"

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(srt)

        print_progress(f"SRT saved to {output_file}", "success")

        return str(output_file)


class TXTFormatter:
    """Format transcription as plain text"""

    def __init__(self, output_dir: str = "data/transcripts"):
        """
        Initialize the formatter.

        Args:
            output_dir: Directory to save text files
        """
        self.output_dir = ensure_directory(output_dir)

    def format(self, result: TranscriptionResult) -> str:
        """
        Format transcription result as plain text.

        Args:
            result: TranscriptionResult from transcriber

        Returns:
            Formatted text string
        """
        return " ".join(seg.text for seg in result.segments)

    def save(self, result: TranscriptionResult, video_id: str) -> str:
        """
        Format and save transcription to text file.

        Args:
            result: TranscriptionResult from transcriber
            video_id: YouTube video ID

        Returns:
            Path to saved file
        """
        text = self.format(result)

        output_file = self.output_dir / f"{video_id}.txt"

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(text)

        print_progress(f"Text saved to {output_file}", "success")

        return str(output_file)
