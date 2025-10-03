# Scrapyboy - YouTube Transcript Archive

Automatically transcribe YouTube videos using Whisper and generate searchable markdown transcripts.

## Features (Phase 1 & 2)

- ✅ **Single video transcription** - Process individual videos by ID
- ✅ **Full channel processing** - Automatically transcribe entire YouTube channels
- ✅ **Idempotent operation** - Won't re-transcribe existing videos (unless --force)
- ✅ **State management** - Tracks processed videos, retries failures
- ✅ **GPU/CPU auto-detection** - Uses faster-whisper with automatic fallback
- ✅ **Custom vocabulary** - Domain-specific term recognition
- ✅ **Markdown output** - Clickable timestamps that link to YouTube
- ✅ **Progress tracking** - Real-time batch processing statistics
- ✅ **Docker-based** - Zero host dependencies

## Quick Start

### 1. Setup Environment

```bash
# Copy environment template
cp .env.example .env

# Edit .env and add your YouTube API key
# REQUIRED for channel mode
nano .env
```

**Get a YouTube API Key:**
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project (or select existing)
3. Enable **YouTube Data API v3**: https://console.developers.google.com/apis/api/youtube.googleapis.com
4. Create credentials → API key
5. Add to `.env` file

### 2. Build Docker Image

```bash
docker compose build
```

This will take a few minutes to download and install:
- Python 3.11
- ffmpeg
- yt-dlp
- faster-whisper
- All dependencies

### 3. Usage

#### Single Video Mode

```bash
# Transcribe a single video by ID
docker compose run --rm transcription --video-id VIDEO_ID

# Example: Transcribe a Tailscale video
docker compose run --rm transcription --video-id e4AYC88gi6g

# Force re-transcription
docker compose run --rm transcription --video-id e4AYC88gi6g --force
```

#### Channel Mode (Phase 2)

```bash
# Process entire channel (configured in config.yaml)
docker compose run --rm transcription --channel

# Force re-process all videos
docker compose run --rm transcription --channel --force

# Skip failed video retries
docker compose run --rm transcription --channel --no-retry
```

**Idempotency:** The system automatically skips videos that have already been transcribed. State is tracked in `data/state.json`.

### 4. View Output

```bash
# Check the output
ls -lh data/transcripts/

# Read the transcript
cat data/transcripts/VIDEO_ID.md
```

## Configuration

Edit `config.yaml` to customize:

### Custom Vocabulary

Add domain-specific terms that should be recognized correctly:

```yaml
transcription:
  custom_vocabulary:
    - "Tailscale"
    - "WireGuard"
    - "headscale"
    # Add more terms...
```

### Model Selection

Choose the Whisper model:

```yaml
transcription:
  model_preference: "auto"  # auto, tiny, base, small, medium, large
```

- `auto`: Selects `medium` for GPU, `base` for CPU
- `base`: Fast, decent accuracy (~1GB)
- `medium`: Balanced (default for GPU, ~3GB)
- `large`: Best accuracy, slower (~6GB)

### Output Formats

```yaml
output:
  formats:
    - markdown  # Markdown with timestamps
    # - srt     # Subtitle format (Phase 2)
    # - txt     # Plain text (Phase 2)
```

## Performance

### GPU (NVIDIA)

To enable GPU acceleration:

1. Install [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html)
2. Uncomment the GPU section in `docker-compose.yml`:

```yaml
deploy:
  resources:
    reservations:
      devices:
        - driver: nvidia
          count: 1
          capabilities: [gpu]
```

**Expected speeds (1 hour video):**
- Base model: ~2 minutes
- Medium model: ~4 minutes
- Large model: ~8 minutes

### CPU (macOS/Linux)

**Expected speeds (1 hour video):**
- Base model: ~30-60 minutes
- Medium model: Not recommended (too slow)

## Output Format

### Markdown with Frontmatter

```markdown
---
video_id: "dQw4w9WgXcQ"
title: "Video Title"
channel_name: "Tailscale"
published_at: "2025-10-03"
duration_seconds: 3600
youtube_url: "https://youtube.com/watch?v=..."
transcribed_at: "2025-10-03T15:30:00"
transcription_method: "gpu"
model_used: "medium"
word_count: 7200
---

# Video Title

**[00:00](https://youtube.com/watch?v=...&t=0s)** Welcome everyone! Today we're going to talk about...

**[00:15](https://youtube.com/watch?v=...&t=15s)** First, let's cover the architecture...

**[00:42](https://youtube.com/watch?v=...&t=42s)** Now, moving on to...
```

### Clickable Timestamps

Each timestamp is a clickable link that opens YouTube at that exact moment.

## Project Structure

```
scrapyboy/
├── docker-compose.yml      # Docker configuration
├── Dockerfile              # Container definition
├── config.yaml            # User configuration
├── .env                   # API keys (gitignored)
├── requirements.txt       # Python dependencies
├── README.md             # This file
│
├── src/
│   ├── main.py           # CLI entry point
│   ├── downloader.py     # YouTube video/metadata downloader
│   ├── transcriber.py    # Whisper transcription
│   ├── formatters.py     # Output formatters (MD/SRT/TXT)
│   └── utils.py          # Helper functions
│
└── data/
    ├── transcripts/      # Output files (.md)
    └── temp/            # Downloaded audio (auto-cleanup)
```

## Troubleshooting

### "YOUTUBE_API_KEY not set"

This is just a warning in Phase 1. You can ignore it or set the API key for future use.

**To get a YouTube API key:**
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project
3. Enable YouTube Data API v3
4. Create credentials (API key)
5. Add to `.env` file

### "Failed to download video"

Common causes:
- Video is private/deleted
- Video has age restrictions
- Network connectivity issues

Try:
```bash
# Test yt-dlp directly
docker compose run --rm transcription yt-dlp --version
```

### Slow transcription on CPU

Use a smaller model:

```yaml
transcription:
  model_preference: "base"  # or "tiny"
```

### Out of memory

Reduce model size or enable GPU acceleration.

## Development

### Run without Docker (for development)

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run
python -m src.main --video-id VIDEO_ID
```

### Project Status

- ✅ **Phase 1:** Single video transcription with idempotency
- ✅ **Phase 2:** Full channel processing, state management (COMPLETE!)
- ⏳ **Phase 3:** Static website generation with search
- ⏳ **Phase 4:** GitHub Actions automation
- ⏳ **Phase 5:** Advanced features and polish

## Quick Reference

```bash
# Single video mode
docker compose run --rm transcription --video-id VIDEO_ID [--force]

# Channel mode
docker compose run --rm transcription --channel [--force] [--no-retry]

# Options
--video-id VIDEO_ID    # YouTube video ID (single video mode)
--channel              # Process entire channel from config.yaml
--config CONFIG        # Path to config.yaml (default: config.yaml)
--force                # Force re-transcription of existing videos
--no-retry             # Don't retry failed videos (channel mode only)

# Examples
docker compose run --rm transcription --video-id e4AYC88gi6g
docker compose run --rm transcription --channel
docker compose run --rm transcription --channel --force
```

### State Management

Channel mode tracks progress in `data/state.json`:
- ✓ Completed videos
- ✗ Failed videos (auto-retried up to 3 times)
- Statistics (total time, average time, etc.)

View statistics any time by running channel mode - it will show stats and skip already-processed videos.

## Next Steps

Once Phase 1 is working:

1. **Phase 2:** Implement channel-wide processing
   - YouTube API integration
   - Batch processing
   - State management (track processed videos)
   - SRT and TXT output

2. **Phase 3:** Build static website
   - Astro-based site generation
   - Pagefind search
   - Responsive design

3. **Phase 4:** Automation
   - GitHub Actions workflow
   - Scheduled updates
   - Auto-deployment

## License

MIT

## Credits

- [faster-whisper](https://github.com/guillaumekln/faster-whisper) - GPU-accelerated transcription
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - YouTube video/audio downloader
- [OpenAI Whisper](https://github.com/openai/whisper) - Speech recognition model
