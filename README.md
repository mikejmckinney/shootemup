# Shoot 'Em Up

A modern arcade-style shoot 'em up / survivor-shmup hybrid designed for quick sessions, high replayability, and long-term progression without pay-to-win mechanics.

## 🎮 Game Overview

**Hybrid: Stage-Select World Map + Scrolling Stages + Arena Events**

- **Session length**: 8–15 minute runs
- **Perspective**: Top-down (with occasional vertical scrolling segments)
- **Design philosophy**: Easy to pick up, hard to master

### Core Features

- **Build Diversity**: Weapons + passives + synergies create meaningful choices
- **Anti-Repetition Systems**: Branching routes, run modifiers, biome hazards, boss variants
- **Fair Competition**: Weekly challenges use normalized stats with fixed seeds
- **Ethical Monetization**: Cosmetics only, no pay-to-win

## 🎨 Visual Style

Modern arcade sci-fi aesthetic:
- HD 2D vector-style illustration
- Clean geometric shapes with flat colors
- Dark backgrounds, bright gameplay elements
- Minimalist sci-fi HUD

## 📁 Repository Structure

```
/
├── .context/                     # 📋 Authoritative project documentation
│   ├── 00_INDEX.md               # Context pack index (read order)
│   ├── 10_game-direction.md      # Core game design direction
│   ├── 10A_game-direction-expanded.md  # Expanded details
│   ├── 20_art-direction.md       # Visual style guidelines
│   ├── 30_ui-principles.md       # UI/HUD design rules
│   ├── 40_gameplay-systems.md    # Combat and weapon systems
│   └── ...                       # See 00_INDEX.md for full list
│
├── AI_REPO_GUIDE.md              # AI agent reference guide
├── AGENTS.md                     # Root agent instructions
├── install.sh                    # Codespace bootstrap script
├── test.sh                       # Verification script
│
└── .github/
    ├── copilot-instructions.md   # GitHub Copilot instructions
    └── prompts/                  # AI onboarding prompts
```

## 🚀 Getting Started

### For AI Agents

1. Read `.context/00_INDEX.md` for the authoritative context pack
2. Follow the read order specified in the index
3. Consult `AI_REPO_GUIDE.md` for conventions and commands

### Verification

```bash
# Verify repository integrity
./test.sh
```

## 📖 Documentation

The `.context/` folder contains the **authoritative project documentation**:

| Document | Purpose |
|----------|---------|
| `10_game-direction.md` | Core gameplay and design direction |
| `20_art-direction.md` | Visual style and rendering rules |
| `21_visual-keywords-whitelist.md` | Approved visual vocabulary |
| `30_ui-principles.md` | HUD layout and interaction rules |
| `40_gameplay-systems.md` | Combat, weapons, and encounters |
| `41_progression-economy.md` | In-run and meta progression |
| `50_weekly-challenges-fairplay.md` | Competitive mode rules |

## 🎯 Design Pillars

1. **Readability First**: Clear separation of player, enemies, projectiles, and background
2. **Build Diversity**: Meaningful choices that change gameplay
3. **Anti-Repetition**: Systems that keep runs fresh
4. **Skill-Based Competition**: Weekly challenges with normalized power
5. **Respect Player Time**: Fast restarts, fair progression

## 📄 License

MIT
