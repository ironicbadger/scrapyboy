# Scrapyboy Website

Static website for browsing and searching YouTube transcripts.

## Features

- 📹 Grid view of all transcribed videos
- 🔍 Full-text search powered by Pagefind
- 📝 Individual video pages with full transcripts
- ⏱️ Clickable timestamps linking to YouTube
- 📱 Responsive design with Tailwind CSS

## Development

### Using Docker (Recommended)

```bash
cd website
docker compose up
```

Visit http://localhost:4321

### Local Development

```bash
cd website
npm install
npm run dev
```

## Building for Production

### Using Docker

```bash
docker compose run website npm run build
```

Output will be in `dist/` directory.

### Local Build

```bash
npm run build
```

The build process:
1. Astro generates static HTML/CSS/JS
2. Pagefind indexes all content for search
3. Output is fully static - can be served from any web server

## Deployment

The `dist/` directory contains the complete static site. Deploy to:
- Netlify
- Vercel
- GitHub Pages
- Any static hosting service
- Or serve with nginx/caddy

## Architecture

- **Framework**: Astro (static site generator)
- **Styling**: Tailwind CSS
- **Search**: Pagefind (static search)
- **Content**: Symlinked from `../data/transcripts/`

The transcripts are read directly from the git repository - no database needed!
