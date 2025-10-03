"""Main CLI entry point for scrapyboy"""

import argparse
import sys
import os
from pathlib import Path
from typing import Optional
import yaml
from dotenv import load_dotenv

from .downloader import VideoDownloader
from .transcriber import Transcriber
from .formatters import MarkdownFormatter, SRTFormatter, TXTFormatter
from .youtube_client import YouTubeClient
from .state_manager import StateManager
from .utils import print_progress


def load_config(config_path: str = "config.yaml") -> dict:
    """Load configuration from YAML file"""
    try:
        with open(config_path, "r") as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        print_progress(f"Config file not found: {config_path}", "error")
        sys.exit(1)
    except yaml.YAMLError as e:
        print_progress(f"Invalid config file: {e}", "error")
        sys.exit(1)


def process_video(video_id: str, config: dict, force: bool = False):
    """
    Process a single video: download, transcribe, format.

    Args:
        video_id: YouTube video ID
        config: Configuration dictionary
        force: Force re-transcription even if file exists
    """
    print_progress(f"Processing video: {video_id}")
    print_progress("=" * 60)

    # Initialize components
    temp_dir = config["output"]["temp_dir"]
    output_dir = config["output"]["output_dir"]

    # Check if already transcribed (idempotency)
    if not force:
        from pathlib import Path
        existing_file = Path(output_dir) / f"{video_id}.md"
        if existing_file.exists():
            print_progress(f"Video already transcribed: {existing_file}", "success")
            print_progress("Use --force to re-transcribe")
            print_progress("=" * 60)
            return

    downloader = VideoDownloader(temp_dir=temp_dir)
    transcriber = Transcriber(
        model_preference=config["transcription"]["model_preference"],
        custom_vocabulary=config["transcription"]["custom_vocabulary"],
        common_corrections=config["transcription"].get("common_corrections", {}),
        language=config["transcription"]["language"]
    )

    try:
        # Step 1: Get video metadata
        print_progress("Step 1/4: Fetching video metadata...")
        video_info = downloader.get_video_info(video_id)

        print_progress(f"Title: {video_info['title']}")
        print_progress(f"Channel: {video_info['channel_name']}")
        print_progress(f"Duration: {video_info['duration_seconds']}s")

        # Estimate transcription time
        estimated_time = transcriber.estimate_time(video_info['duration_seconds'])
        print_progress(f"Estimated transcription time: {estimated_time}")

        # Step 2: Download audio
        print_progress("\nStep 2/4: Downloading audio...")
        audio_path = downloader.download_audio(video_id)

        # Step 3: Transcribe
        print_progress("\nStep 3/4: Transcribing audio...")
        result = transcriber.transcribe(audio_path)

        # Step 4: Format and save
        print_progress("\nStep 4/4: Saving transcripts...")

        output_formats = config["output"]["formats"]
        output_files = []

        if "markdown" in output_formats:
            formatter = MarkdownFormatter(output_dir=output_dir)
            md_file = formatter.save(
                result,
                video_info,
                style=config["output"]["markdown_style"]
            )
            output_files.append(md_file)

        if "srt" in output_formats:
            formatter = SRTFormatter(output_dir=output_dir)
            srt_file = formatter.save(result, video_id)
            output_files.append(srt_file)

        if "txt" in output_formats:
            formatter = TXTFormatter(output_dir=output_dir)
            txt_file = formatter.save(result, video_id)
            output_files.append(txt_file)

        # Cleanup
        if not config["processing"]["keep_audio"]:
            downloader.cleanup_audio(audio_path)

        # Success!
        print_progress("=" * 60)
        print_progress(f"✓ Processing complete!", "success")
        print_progress(f"  Video: {video_info['title']}")
        print_progress(f"  Segments: {len(result.segments)}")
        print_progress(f"  Transcription time: {result.transcription_time:.1f}s")
        print_progress(f"  Output files:")
        for file in output_files:
            print_progress(f"    - {file}")

    except Exception as e:
        print_progress(f"Failed to process video: {e}", "error")
        sys.exit(1)


def process_channel(config: dict, force: bool = False, retry_failed: bool = True, limit: Optional[int] = None):
    """
    Process all videos from a channel.

    Args:
        config: Configuration dictionary
        force: Force re-transcription of all videos
        retry_failed: Retry previously failed videos
        limit: Maximum number of videos to process (for testing)
    """
    api_key = os.getenv(config["youtube"]["api_key_env"])
    if not api_key:
        print_progress("YouTube API key not found", "error")
        sys.exit(1)

    # Initialize services
    youtube = YouTubeClient(api_key)
    state = StateManager(state_file="/data/state.json")
    temp_dir = config["output"]["temp_dir"]
    output_dir = config["output"]["output_dir"]

    try:
        # Resolve channel ID
        channel_identifier = config["channel"]["id"]
        print_progress(f"Resolving channel: {channel_identifier}")
        channel_id = youtube.resolve_channel_id(channel_identifier)
        print_progress(f"Channel ID: {channel_id}", "success")

        # Get channel info
        print_progress("Fetching channel information...")
        channel_info = youtube.get_channel_info(channel_id)
        print_progress(f"Channel: {channel_info['title']}", "success")
        print_progress(f"Total videos: {channel_info['video_count']}")

        # Update state
        state.set_channel_info(channel_id, channel_info['title'])

        # Get all videos from channel
        print_progress("\nFetching all videos from channel...")
        all_videos = youtube.get_channel_videos(channel_id)
        print_progress(f"Found {len(all_videos)} videos", "success")

        # Determine which videos to process
        if force:
            videos_to_process = [v["video_id"] for v in all_videos]
            print_progress(f"Force mode: Will process all {len(videos_to_process)} videos")
        else:
            # Get unprocessed videos
            all_video_ids = [v["video_id"] for v in all_videos]
            unprocessed = state.get_unprocessed_videos(all_video_ids)

            # Add failed videos if retry is enabled
            if retry_failed:
                failed = state.get_failed_videos(max_attempts=3)
                videos_to_process = list(set(unprocessed + failed))
            else:
                videos_to_process = unprocessed

            print_progress(f"Videos to process: {len(videos_to_process)}")
            print_progress(f"  New: {len(unprocessed)}")
            if retry_failed:
                print_progress(f"  Retry: {len(failed)}")

        # Apply limit if specified
        if limit and len(videos_to_process) > limit:
            print_progress(f"\n⚠ Limiting to first {limit} videos (--limit flag)")
            videos_to_process = videos_to_process[:limit]

        if not videos_to_process:
            print_progress("\nAll videos already processed!", "success")
            state.print_statistics()
            return

        # Initialize transcriber (reused for all videos)
        print_progress("\nInitializing transcriber...")
        transcriber = Transcriber(
            model_preference=config["transcription"]["model_preference"],
            custom_vocabulary=config["transcription"]["custom_vocabulary"],
            common_corrections=config["transcription"].get("common_corrections", {}),
            language=config["transcription"]["language"]
        )

        downloader = VideoDownloader(temp_dir=temp_dir)

        # Process each video
        print_progress("\n" + "=" * 60)
        print_progress("Starting batch processing")
        print_progress("=" * 60)

        for i, video_id in enumerate(videos_to_process, 1):
            print_progress(f"\n[{i}/{len(videos_to_process)}] Processing: {video_id}")

            # Check if already exists (idempotency)
            if not force:
                existing_file = Path(output_dir) / f"{video_id}.md"
                if existing_file.exists():
                    print_progress(f"Skipping - already exists: {video_id}", "success")
                    continue

            state.mark_video_processing(video_id)

            try:
                # Get video info
                video_info = downloader.get_video_info(video_id)
                print_progress(f"  Title: {video_info['title']}")
                print_progress(f"  Duration: {video_info['duration_seconds']}s")

                # Download audio
                audio_path = downloader.download_audio(video_id)

                # Transcribe
                result = transcriber.transcribe(audio_path)

                # Save markdown
                formatter = MarkdownFormatter(output_dir=output_dir)
                formatter.save(result, video_info, style=config["output"]["markdown_style"])

                # Cleanup
                if not config["processing"]["keep_audio"]:
                    downloader.cleanup_audio(audio_path)

                # Update state
                state.mark_video_completed(
                    video_id,
                    video_info['duration_seconds'],
                    result.transcription_time,
                    result.method
                )

                print_progress(f"  ✓ Completed in {result.transcription_time:.1f}s", "success")

            except Exception as e:
                print_progress(f"  ✗ Failed: {e}", "error")
                state.mark_video_failed(video_id, str(e))

                # Continue with next video
                continue

        # Print final statistics
        print_progress("\n" + "=" * 60)
        print_progress("Batch processing complete!", "success")
        print_progress("=" * 60)
        state.print_statistics()

    except Exception as e:
        print_progress(f"Channel processing failed: {e}", "error")
        sys.exit(1)


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description="Scrapyboy - YouTube Transcript Archive System",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Transcribe a single video
  python -m src.main --video-id dQw4w9WgXcQ

  # Process entire channel (from config.yaml)
  python -m src.main --channel

  # Force re-process all channel videos
  python -m src.main --channel --force

For more information, see README.md
        """
    )

    # Mode selection (mutually exclusive)
    mode_group = parser.add_mutually_exclusive_group(required=True)
    mode_group.add_argument(
        "--video-id",
        help="YouTube video ID to transcribe (single video mode)"
    )
    mode_group.add_argument(
        "--channel",
        action="store_true",
        help="Process entire channel from config.yaml"
    )

    parser.add_argument(
        "--config",
        default="config.yaml",
        help="Path to config file (default: config.yaml)"
    )

    parser.add_argument(
        "--force",
        action="store_true",
        help="Force re-transcription even if already processed"
    )

    parser.add_argument(
        "--no-retry",
        action="store_true",
        help="Don't retry previously failed videos (channel mode only)"
    )

    parser.add_argument(
        "--limit",
        type=int,
        help="Maximum number of videos to process (channel mode only)"
    )

    args = parser.parse_args()

    # Load environment variables
    load_dotenv()

    # Load configuration
    config = load_config(args.config)

    # Check for API key
    api_key_env = config["youtube"]["api_key_env"]
    if not os.getenv(api_key_env):
        if args.channel:
            print_progress(f"Error: {api_key_env} not set (required for channel mode)", "error")
            sys.exit(1)
        else:
            print_progress(
                f"Warning: {api_key_env} not set. You'll need this for channel mode.",
                "warning"
            )

    # Route to appropriate mode
    if args.channel:
        process_channel(config, force=args.force, retry_failed=not args.no_retry, limit=args.limit)
    else:
        process_video(args.video_id, config, force=args.force)


if __name__ == "__main__":
    main()
