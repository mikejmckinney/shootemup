# Art Production Pack

This folder contains the complete image-generation pack for the Shoot 'Em Up project.

## Structure

```
art/
├── manifest.json       # Master manifest with all 20 image entries
├── prompts/           # Individual prompt files (01-20)
├── renders/           # Generated images (output from image generation)
├── references/        # Reference materials and mood boards
├── contact_sheets/    # Contact sheets for review
└── exports/           # Final exported assets
```

## Manifest Overview

The `manifest.json` contains 20 entries across 5 categories:

| Category | Count | Description |
|----------|-------|-------------|
| Key Art & Identity | 2 | Title art and banner key art |
| Gameplay Screenshots | 4 | Core combat, boss, arena, hazard room |
| UI/UX Mockups | 6 | Level-up, HUD, pause, ship select, results, leaderboard |
| Assets & Kits | 5 | Ships, enemies, projectiles, UI components, pickups/VFX |
| Anti-Repetition Systems | 3 | Branching routes, run modifiers, boss variants |

## Style Anchor

All prompts include the project's STYLE_ANCHOR from `.context/20_art-direction.md`:

> HD 2D vector-style illustration, clean geometric shapes, flat color surfaces with subtle gradients, smooth edges, modern arcade sci-fi aesthetic

## Prompt File Format

Each prompt file in `prompts/` follows this structure:

- **Metadata**: filename, category, size
- **Purpose**: What the image communicates
- **Composition Notes**: Layout and framing guidance
- **Prompt**: Full generation prompt (includes STYLE_ANCHOR)
- **Negative Prompt**: Styles and elements to avoid
- **Consistency Constraints**: Elements that must match across images

## Image Sizes

All images use one of these approved sizes:
- `1024x1024` - Square format (UI screens, gameplay)
- `1536x1024` - Landscape format (key art, asset sheets)
- `1024x1536` - Portrait format (leaderboards, vertical UI)

## Usage

1. Select an entry from `manifest.json`
2. Open the corresponding prompt file in `prompts/`
3. Use the prompt with your image generation tool
4. Save renders to `renders/` folder
5. Review and export finals to `exports/`

## Consistency

These elements must remain consistent across all images:
- **Player ship silhouette**: Angular, arrow-like, cyan/blue identity
- **Enemy shape language**: Role-based shapes (fodder, ranged, elite, etc.)
- **HUD layout**: HP top-left, score top-right, weapons bottom-left, abilities bottom-right
- **Color palette**: Dark navy background, cyan player, red/orange enemies, gold/yellow rewards
