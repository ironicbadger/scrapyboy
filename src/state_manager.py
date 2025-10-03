"""State management for tracking processed videos"""

import json
from pathlib import Path
from typing import Dict, List, Optional, Set
from datetime import datetime
from dataclasses import dataclass, asdict

from .utils import print_progress


@dataclass
class VideoState:
    """State information for a single video"""
    status: str  # pending, processing, completed, failed
    processed_at: Optional[str] = None
    duration_seconds: Optional[int] = None
    transcription_time: Optional[float] = None
    method: Optional[str] = None  # gpu, cpu
    error: Optional[str] = None
    attempt_count: int = 0


class StateManager:
    """Manage processing state for videos"""

    def __init__(self, state_file: str = "/data/state.json"):
        """
        Initialize state manager.

        Args:
            state_file: Path to state JSON file
        """
        self.state_file = Path(state_file)
        self.state = self._load_state()

    def _load_state(self) -> Dict:
        """Load state from file"""
        if self.state_file.exists():
            try:
                with open(self.state_file, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError as e:
                print_progress(f"Invalid state file, creating new: {e}", "warning")
                return self._create_empty_state()
        else:
            return self._create_empty_state()

    def _create_empty_state(self) -> Dict:
        """Create empty state structure"""
        return {
            "channel_id": None,
            "channel_name": None,
            "last_checked": None,
            "videos_processed": 0,
            "videos_failed": 0,
            "last_video_date": None,
            "videos": {}
        }

    def save(self):
        """Save state to file"""
        try:
            # Ensure directory exists
            self.state_file.parent.mkdir(parents=True, exist_ok=True)

            # Write atomically (write to temp, then rename)
            temp_file = self.state_file.with_suffix('.tmp')
            with open(temp_file, 'w') as f:
                json.dump(self.state, f, indent=2)

            temp_file.replace(self.state_file)

        except Exception as e:
            print_progress(f"Failed to save state: {e}", "error")

    def set_channel_info(self, channel_id: str, channel_name: str):
        """Set channel information"""
        self.state["channel_id"] = channel_id
        self.state["channel_name"] = channel_name
        self.state["last_checked"] = datetime.now().isoformat()

    def is_video_processed(self, video_id: str) -> bool:
        """Check if video has been successfully processed"""
        video_state = self.state["videos"].get(video_id)
        if not video_state:
            return False
        return video_state.get("status") == "completed"

    def get_video_state(self, video_id: str) -> Optional[VideoState]:
        """Get state for a specific video"""
        video_data = self.state["videos"].get(video_id)
        if not video_data:
            return None
        return VideoState(**video_data)

    def mark_video_processing(self, video_id: str):
        """Mark video as currently being processed"""
        if video_id not in self.state["videos"]:
            self.state["videos"][video_id] = asdict(VideoState(status="processing"))
        else:
            self.state["videos"][video_id]["status"] = "processing"
            self.state["videos"][video_id]["attempt_count"] += 1

        self.save()

    def mark_video_completed(
        self,
        video_id: str,
        duration_seconds: int,
        transcription_time: float,
        method: str
    ):
        """Mark video as successfully processed"""
        self.state["videos"][video_id] = asdict(VideoState(
            status="completed",
            processed_at=datetime.now().isoformat(),
            duration_seconds=duration_seconds,
            transcription_time=transcription_time,
            method=method,
            attempt_count=self.state["videos"].get(video_id, {}).get("attempt_count", 0) + 1
        ))

        self.state["videos_processed"] += 1
        self.save()

    def mark_video_failed(self, video_id: str, error: str):
        """Mark video as failed"""
        current_attempts = self.state["videos"].get(video_id, {}).get("attempt_count", 0)

        self.state["videos"][video_id] = asdict(VideoState(
            status="failed",
            processed_at=datetime.now().isoformat(),
            error=error,
            attempt_count=current_attempts + 1
        ))

        self.state["videos_failed"] += 1
        self.save()

    def get_unprocessed_videos(self, all_video_ids: List[str]) -> List[str]:
        """
        Get list of video IDs that haven't been processed yet.

        Args:
            all_video_ids: Complete list of video IDs from channel

        Returns:
            List of unprocessed video IDs
        """
        return [
            vid for vid in all_video_ids
            if not self.is_video_processed(vid)
        ]

    def get_failed_videos(self, max_attempts: int = 3) -> List[str]:
        """
        Get list of failed videos that can be retried.

        Args:
            max_attempts: Maximum number of retry attempts

        Returns:
            List of failed video IDs that haven't exceeded max attempts
        """
        failed = []
        for video_id, video_data in self.state["videos"].items():
            if (video_data.get("status") == "failed" and
                video_data.get("attempt_count", 0) < max_attempts):
                failed.append(video_id)

        return failed

    def get_statistics(self) -> Dict:
        """Get processing statistics"""
        total_videos = len(self.state["videos"])
        completed = sum(1 for v in self.state["videos"].values() if v.get("status") == "completed")
        failed = sum(1 for v in self.state["videos"].values() if v.get("status") == "failed")
        processing = sum(1 for v in self.state["videos"].values() if v.get("status") == "processing")
        pending = total_videos - completed - failed - processing

        # Calculate total transcription time
        total_time = sum(
            v.get("transcription_time", 0)
            for v in self.state["videos"].values()
            if v.get("transcription_time")
        )

        # Calculate average transcription time
        completed_with_time = [
            v.get("transcription_time", 0)
            for v in self.state["videos"].values()
            if v.get("status") == "completed" and v.get("transcription_time")
        ]
        avg_time = sum(completed_with_time) / len(completed_with_time) if completed_with_time else 0

        return {
            "channel_id": self.state.get("channel_id"),
            "channel_name": self.state.get("channel_name"),
            "last_checked": self.state.get("last_checked"),
            "total_videos": total_videos,
            "completed": completed,
            "failed": failed,
            "processing": processing,
            "pending": pending,
            "total_transcription_time": total_time,
            "average_transcription_time": avg_time
        }

    def print_statistics(self):
        """Print formatted statistics"""
        stats = self.get_statistics()

        print_progress("=" * 60)
        print_progress("Processing Statistics", "info")
        print_progress("=" * 60)
        print_progress(f"Channel: {stats['channel_name']} ({stats['channel_id']})")
        print_progress(f"Last checked: {stats['last_checked']}")
        print_progress("")
        print_progress(f"Total videos: {stats['total_videos']}")
        print_progress(f"  ✓ Completed: {stats['completed']}", "success")
        print_progress(f"  ✗ Failed: {stats['failed']}", "error" if stats['failed'] > 0 else "info")
        print_progress(f"  ⋯ Processing: {stats['processing']}")
        print_progress(f"  ○ Pending: {stats['pending']}")
        print_progress("")
        print_progress(f"Total transcription time: {stats['total_transcription_time']:.1f}s")
        print_progress(f"Average time per video: {stats['average_transcription_time']:.1f}s")
        print_progress("=" * 60)
