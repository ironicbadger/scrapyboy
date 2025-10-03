"""Utility functions for scrapyboy"""

import os
import hashlib
import subprocess
import sys
from pathlib import Path
from typing import Optional


def check_gpu_available() -> bool:
    """
    Check if NVIDIA GPU is available and accessible.

    Returns:
        True if GPU is available, False otherwise
    """
    try:
        # Check if nvidia-smi is available
        result = subprocess.run(
            ["nvidia-smi"],
            capture_output=True,
            timeout=5
        )
        return result.returncode == 0
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return False


def get_file_hash(filepath: str) -> str:
    """
    Generate SHA-256 hash of a file.

    Args:
        filepath: Path to the file

    Returns:
        Hex digest of the file hash
    """
    hash_sha256 = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha256.update(chunk)
    return hash_sha256.hexdigest()


def format_duration(seconds: int) -> str:
    """
    Format seconds into HH:MM:SS format.

    Args:
        seconds: Duration in seconds

    Returns:
        Formatted duration string
    """
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60

    if hours > 0:
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"
    else:
        return f"{minutes:02d}:{secs:02d}"


def format_timestamp_link(seconds: float, video_id: str) -> str:
    """
    Create a clickable YouTube timestamp link.

    Args:
        seconds: Timestamp in seconds
        video_id: YouTube video ID

    Returns:
        Markdown-formatted timestamp link
    """
    timestamp_str = format_duration(int(seconds))
    youtube_url = f"https://youtube.com/watch?v={video_id}&t={int(seconds)}s"
    return f"**[{timestamp_str}]({youtube_url})**"


def ensure_directory(path: str) -> Path:
    """
    Ensure a directory exists, creating it if necessary.

    Args:
        path: Directory path

    Returns:
        Path object
    """
    dir_path = Path(path)
    dir_path.mkdir(parents=True, exist_ok=True)
    return dir_path


def print_progress(message: str, level: str = "info"):
    """
    Print a formatted progress message.

    Args:
        message: Message to print
        level: Message level (info, success, warning, error)
    """
    colors = {
        "info": "\033[94m",     # Blue
        "success": "\033[92m",  # Green
        "warning": "\033[93m",  # Yellow
        "error": "\033[91m",    # Red
    }
    reset = "\033[0m"

    color = colors.get(level, colors["info"])
    prefix = {
        "info": "ℹ",
        "success": "✓",
        "warning": "⚠",
        "error": "✗",
    }.get(level, "•")

    print(f"{color}{prefix} {message}{reset}", file=sys.stderr)
