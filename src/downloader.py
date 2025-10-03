"""Video downloader using yt-dlp"""

import os
import subprocess
from pathlib import Path
from typing import Dict, Optional
import json

from .utils import ensure_directory, print_progress


class VideoDownloader:
    """Download audio from YouTube videos using yt-dlp"""

    def __init__(self, temp_dir: str = "data/temp"):
        """
        Initialize the downloader.

        Args:
            temp_dir: Directory to store downloaded audio files
        """
        self.temp_dir = ensure_directory(temp_dir)

    def download_audio(self, video_id: str) -> str:
        """
        Download audio from a YouTube video.

        Args:
            video_id: YouTube video ID

        Returns:
            Path to the downloaded audio file

        Raises:
            RuntimeError: If download fails
        """
        output_path = self.temp_dir / f"{video_id}.%(ext)s"

        print_progress(f"Downloading audio for video: {video_id}")

        # yt-dlp options
        # Extracts best audio quality, converts to m4a
        cmd = [
            "yt-dlp",
            "--extract-audio",
            "--audio-format", "m4a",
            "--audio-quality", "0",  # Best quality
            "-o", str(output_path),
            "--no-playlist",
            "--quiet",
            "--progress",
            f"https://youtube.com/watch?v={video_id}"
        ]

        try:
            subprocess.run(cmd, check=True, capture_output=False)

            # Find the downloaded file
            audio_file = self.temp_dir / f"{video_id}.m4a"
            if not audio_file.exists():
                raise RuntimeError(f"Downloaded audio file not found: {audio_file}")

            print_progress(f"Audio downloaded: {audio_file}", "success")
            return str(audio_file)

        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Failed to download video {video_id}: {e}")

    def get_video_info(self, video_id: str) -> Dict:
        """
        Get video metadata using yt-dlp.

        Args:
            video_id: YouTube video ID

        Returns:
            Dictionary containing video metadata

        Raises:
            RuntimeError: If fetching metadata fails
        """
        print_progress(f"Fetching metadata for video: {video_id}")

        cmd = [
            "yt-dlp",
            "--dump-json",
            "--no-playlist",
            "--quiet",
            f"https://youtube.com/watch?v={video_id}"
        ]

        try:
            result = subprocess.run(
                cmd,
                check=True,
                capture_output=True,
                text=True
            )

            metadata = json.loads(result.stdout)

            # Extract relevant fields
            info = {
                "video_id": metadata.get("id", video_id),
                "title": metadata.get("title", "Unknown"),
                "description": metadata.get("description", ""),
                "channel_name": metadata.get("channel", "Unknown"),
                "channel_id": metadata.get("channel_id", ""),
                "upload_date": metadata.get("upload_date", ""),  # YYYYMMDD format
                "duration_seconds": metadata.get("duration", 0),
                "youtube_url": metadata.get("webpage_url", f"https://youtube.com/watch?v={video_id}"),
                "thumbnail_url": metadata.get("thumbnail", ""),
                "view_count": metadata.get("view_count", 0),
                "like_count": metadata.get("like_count", 0),
            }

            print_progress(f"Metadata fetched: {info['title']}", "success")
            return info

        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Failed to fetch metadata for {video_id}: {e}")
        except json.JSONDecodeError as e:
            raise RuntimeError(f"Failed to parse metadata for {video_id}: {e}")

    def cleanup_audio(self, audio_path: str):
        """
        Delete downloaded audio file.

        Args:
            audio_path: Path to audio file to delete
        """
        try:
            if os.path.exists(audio_path):
                os.remove(audio_path)
                print_progress(f"Cleaned up audio file: {audio_path}")
        except OSError as e:
            print_progress(f"Failed to cleanup {audio_path}: {e}", "warning")
