"""YouTube API client for fetching channel videos"""

import os
from typing import List, Dict, Optional
from datetime import datetime

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from .utils import print_progress


class YouTubeClient:
    """Client for YouTube Data API v3"""

    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize YouTube API client.

        Args:
            api_key: YouTube Data API key (if None, reads from env)
        """
        self.api_key = api_key or os.getenv("YOUTUBE_API_KEY")
        if not self.api_key:
            raise ValueError("YouTube API key not provided")

        self.youtube = build('youtube', 'v3', developerKey=self.api_key)

    def resolve_channel_id(self, channel_identifier: str) -> str:
        """
        Resolve channel ID from various formats.

        Args:
            channel_identifier: Can be channel ID (UCxxx), handle (@username), or username

        Returns:
            Channel ID (UCxxx format)

        Raises:
            RuntimeError: If channel not found
        """
        # Already a channel ID
        if channel_identifier.startswith("UC"):
            return channel_identifier

        # Handle format (@username)
        if channel_identifier.startswith("@"):
            username = channel_identifier[1:]
            return self._get_channel_id_by_handle(username)

        # Try as username
        return self._get_channel_id_by_username(channel_identifier)

    def _get_channel_id_by_handle(self, handle: str) -> str:
        """Get channel ID from handle"""
        try:
            request = self.youtube.search().list(
                part="snippet",
                q=f"@{handle}",
                type="channel",
                maxResults=1
            )
            response = request.execute()

            if response.get("items"):
                return response["items"][0]["snippet"]["channelId"]
            else:
                raise RuntimeError(f"Channel not found: @{handle}")

        except HttpError as e:
            raise RuntimeError(f"Failed to resolve channel handle: {e}")

    def _get_channel_id_by_username(self, username: str) -> str:
        """Get channel ID from username"""
        try:
            request = self.youtube.channels().list(
                part="id",
                forUsername=username
            )
            response = request.execute()

            if response.get("items"):
                return response["items"][0]["id"]
            else:
                raise RuntimeError(f"Channel not found: {username}")

        except HttpError as e:
            raise RuntimeError(f"Failed to resolve channel username: {e}")

    def get_channel_info(self, channel_id: str) -> Dict:
        """
        Get channel information.

        Args:
            channel_id: YouTube channel ID

        Returns:
            Dictionary with channel info

        Raises:
            RuntimeError: If API call fails
        """
        try:
            request = self.youtube.channels().list(
                part="snippet,statistics",
                id=channel_id
            )
            response = request.execute()

            if not response.get("items"):
                raise RuntimeError(f"Channel not found: {channel_id}")

            item = response["items"][0]
            snippet = item["snippet"]
            stats = item.get("statistics", {})

            return {
                "channel_id": channel_id,
                "title": snippet["title"],
                "description": snippet.get("description", ""),
                "custom_url": snippet.get("customUrl", ""),
                "published_at": snippet["publishedAt"],
                "thumbnail_url": snippet["thumbnails"]["default"]["url"],
                "video_count": int(stats.get("videoCount", 0)),
                "subscriber_count": int(stats.get("subscriberCount", 0)),
                "view_count": int(stats.get("viewCount", 0))
            }

        except HttpError as e:
            raise RuntimeError(f"Failed to fetch channel info: {e}")

    def get_channel_videos(
        self,
        channel_id: str,
        max_results: Optional[int] = None,
        order: str = "date"
    ) -> List[Dict]:
        """
        Get all videos from a channel.

        Args:
            channel_id: YouTube channel ID
            max_results: Maximum number of videos to fetch (None = all)
            order: Sort order (date, viewCount, rating, title)

        Returns:
            List of video dictionaries with metadata

        Raises:
            RuntimeError: If API call fails
        """
        videos = []
        page_token = None

        try:
            while True:
                # Search for videos in channel
                request = self.youtube.search().list(
                    part="id,snippet",
                    channelId=channel_id,
                    type="video",
                    order=order,
                    maxResults=50,  # Max per API call
                    pageToken=page_token
                )
                response = request.execute()

                # Process videos
                for item in response.get("items", []):
                    video_id = item["id"]["videoId"]
                    snippet = item["snippet"]

                    video_info = {
                        "video_id": video_id,
                        "title": snippet["title"],
                        "description": snippet.get("description", ""),
                        "published_at": snippet["publishedAt"],
                        "thumbnail_url": snippet["thumbnails"]["default"]["url"],
                        "channel_title": snippet["channelTitle"],
                        "channel_id": snippet["channelId"]
                    }

                    videos.append(video_info)

                    # Stop if we've hit max_results
                    if max_results and len(videos) >= max_results:
                        return videos[:max_results]

                # Check for next page
                page_token = response.get("nextPageToken")
                if not page_token:
                    break

                print_progress(f"Fetched {len(videos)} videos so far...")

            print_progress(f"Found {len(videos)} total videos", "success")
            return videos

        except HttpError as e:
            raise RuntimeError(f"Failed to fetch channel videos: {e}")

    def get_video_details(self, video_id: str) -> Dict:
        """
        Get detailed information about a specific video.

        Args:
            video_id: YouTube video ID

        Returns:
            Dictionary with video details

        Raises:
            RuntimeError: If API call fails
        """
        try:
            request = self.youtube.videos().list(
                part="snippet,contentDetails,statistics",
                id=video_id
            )
            response = request.execute()

            if not response.get("items"):
                raise RuntimeError(f"Video not found: {video_id}")

            item = response["items"][0]
            snippet = item["snippet"]
            details = item["contentDetails"]
            stats = item.get("statistics", {})

            # Parse duration (ISO 8601 format: PT1H2M3S)
            duration_str = details["duration"]
            duration_seconds = self._parse_duration(duration_str)

            return {
                "video_id": video_id,
                "title": snippet["title"],
                "description": snippet.get("description", ""),
                "channel_id": snippet["channelId"],
                "channel_title": snippet["channelTitle"],
                "published_at": snippet["publishedAt"],
                "duration_seconds": duration_seconds,
                "thumbnail_url": snippet["thumbnails"].get("maxresdefault", {}).get("url") or
                                snippet["thumbnails"]["default"]["url"],
                "view_count": int(stats.get("viewCount", 0)),
                "like_count": int(stats.get("likeCount", 0)),
                "comment_count": int(stats.get("commentCount", 0))
            }

        except HttpError as e:
            raise RuntimeError(f"Failed to fetch video details: {e}")

    def _parse_duration(self, duration: str) -> int:
        """
        Parse ISO 8601 duration to seconds.

        Args:
            duration: ISO 8601 duration string (e.g., PT1H2M3S)

        Returns:
            Duration in seconds
        """
        import re

        # Remove PT prefix
        duration = duration.replace("PT", "")

        # Extract hours, minutes, seconds
        hours = 0
        minutes = 0
        seconds = 0

        h_match = re.search(r'(\d+)H', duration)
        if h_match:
            hours = int(h_match.group(1))

        m_match = re.search(r'(\d+)M', duration)
        if m_match:
            minutes = int(m_match.group(1))

        s_match = re.search(r'(\d+)S', duration)
        if s_match:
            seconds = int(s_match.group(1))

        return hours * 3600 + minutes * 60 + seconds
