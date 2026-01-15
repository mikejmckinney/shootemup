# AI_REPO_GUIDE.md

> **Purpose**: Canonical reference for AI agents working with the Shoot 'Em Up project.  
> **Last verified**: 2026-01-15

## Overview

This is a **modern arcade-style shoot 'em up / survivor-shmup hybrid** game project. The repository currently contains the authoritative design documentation in the `.context/` folder, with game implementation to follow.

**Key characteristics:**
- Quick sessions (8–15 minutes)
- High replayability through anti-repetition systems
- Build diversity with meaningful choices
- Fair competitive modes (skill-only leaderboards)
- Cosmetics-only monetization

## Canonical Truth Hierarchy

**Always consult sources in this order:**

1. **`.context/**`** — Authoritative project direction and constraints
2. **`docs/**`** — Supporting detail (when created)
3. **Codebase** — Current implementation reality

### Context Pack Index

Start with `.context/00_INDEX.md` which provides the read order:

| Priority | Document | Purpose |
|----------|----------|---------|
| 1 | `10_game-direction.md` | Core gameplay direction |
| 2 | `20_art-direction.md` | Visual style rules |
| 3 | `21_visual-keywords-whitelist.md` | Approved visual vocabulary |
| 4 | `22_visual-prompt-template.md` | Image generation templates |
| 5 | `30_ui-principles.md` | UI/HUD design rules |
| 6 | `40_gameplay-systems.md` | Combat and weapon systems |
| 7 | `41_progression-economy.md` | Progression and rewards |
| 8 | `50_weekly-challenges-fairplay.md` | Competitive mode rules |
| 9 | `60_asset-list-and-style-rules.md` | Asset specifications |
| 10 | `70_marketing-visuals.md` | Marketing guidelines |

## How to Use the Context Pack

### For Game Design Work
- Follow `10_game-direction.md` for gameplay decisions
- Reference `40_gameplay-systems.md` and `41_progression-economy.md` for systems

### For Visual/Art Work
- Follow `20_art-direction.md` strictly
- Use only keywords from `21_visual-keywords-whitelist.md`
- Apply `22_visual-prompt-template.md` for image generation

### For UI Design
- Follow `30_ui-principles.md` strictly
- Respect the visual hierarchy defined there

### For Competitive Features
- Follow `50_weekly-challenges-fairplay.md` for fairness rules

## Repository Structure

```
/
├── .context/                     # 📋 AUTHORITATIVE DOCS (read first!)
│   ├── 00_INDEX.md               # Read order for context pack
│   ├── 10_game-direction.md      # Game design direction
│   ├── 20_art-direction.md       # Art style guidelines
│   └── ...                       # Additional context docs
│
├── AI_REPO_GUIDE.md              # This file (AI reference)
├── AGENTS.md                     # Root agent instructions
├── README.md                     # Project overview
├── install.sh                    # Codespace bootstrap
├── test.sh                       # Verification script
│
├── .cursor/                      # Cursor AI config
├── .gemini/                      # Gemini AI config
└── .github/
    ├── copilot-instructions.md   # GitHub Copilot config
    ├── agents/                   # AI agent definitions
    └── prompts/                  # Onboarding prompts
```

## Quick Commands

### Verification
```bash
# Verify repository integrity
./test.sh
```

### Setup (Codespaces)
```bash
# Bootstrap script (runs automatically in Codespaces)
bash install.sh
```

## Conventions

### Documentation
- `.context/` files are **authoritative** — do not modify without explicit instruction
- Propose changes to `.context/` via notes, not direct edits
- Keep this guide (`AI_REPO_GUIDE.md`) updated when structure changes

### File Naming
- Context docs: numbered prefix for read order (e.g., `10_`, `20_`)
- Expanded docs: `A` suffix (e.g., `10A_game-direction-expanded.md`)

### Design Decisions
- Always cite the relevant `.context/` document when making design choices
- Readability is the top priority in all visual decisions
- No pay-to-win mechanics in any feature

## Next Steps (Project Roadmap)

1. **Game Engine Setup** — Choose engine and set up project structure
2. **Core Mechanics** — Implement movement, shooting, and collision
3. **Weapon System** — Build weapon archetypes per `40_gameplay-systems.md`
4. **Enemy System** — Create enemy types with clear visual language
5. **Progression** — Implement in-run leveling and meta unlocks
6. **UI Implementation** — Build HUD per `30_ui-principles.md`

## Gotchas / Known Issues

- This is currently a **design documentation repository**; game code will be added
- The `.context/` folder contains some duplicate/legacy files (e.g., `art-direction.md` vs `20_art-direction.md`) — always prefer the numbered versions
- `install.sh` requires `$DOTFILES` environment variable (set by Codespaces)

## Updating This Guide

When making changes that affect:
- Commands or scripts → Update "Quick Commands" section
- File structure → Update "Repository Structure" section
- Conventions → Update "Conventions" section
- Project status → Update "Next Steps" section

State "AI_REPO_GUIDE.md: no changes required" if your PR doesn't affect these areas.
