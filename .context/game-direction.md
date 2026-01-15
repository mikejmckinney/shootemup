# Game Direction — Non-authoritative Copy

> **Important:** This file is a **convenience / alternate-format copy** of the authoritative design document at **`.context/10_game-direction.md`**.
>
> - Treat **`10_game-direction.md`** as the **single source of truth** for game direction.
> - **Do not** update this file independently; instead, make changes in `10_game-direction.md` and then sync or regenerate this copy if it is still needed.
> - If you are unsure which file to edit, **edit `10_game-direction.md` only**.

---

# Game Direction — Chosen Primary Direction

## Project Overview

This project is a modern arcade-style **shoot ’em up / survivor-shmup hybrid** designed for quick sessions, high replayability, and long-term progression without pay-to-win mechanics.

The game blends:
- Classic shoot ’em up clarity and intensity
- Modern survivor-style progression and build variety
- A flexible structure that supports future content expansion

The goal is to create a game that is:
- Easy to pick up
- Skill-expressive
- Visually modern and clean
- Resistant to repetition and staleness

---

## Chosen Primary Direction

### **Hybrid: Stage-Select World Map + Scrolling Stages + Arena Events**

This direction combines authored level pacing with systemic replayability.

Instead of committing to only classic scrolling stages or only arena survival, the game uses a **hybrid structure** that mixes both, allowing for varied pacing and player choice.

---

## Camera & Perspective

- Primary view: **Top-down**
- Occasional **vertical scrolling segments** for classic shmup moments
- Camera remains fixed and readable at all times
- No rotation or perspective distortion during gameplay

---

## Session Structure

- Typical run length: **8–15 minutes**
- Designed for “one more run” play
- Fast restart loop
- Clear start, escalation, climax, and resolution

---

## World Map & Stage Flow

- Runs begin on a **Stage Select World Map**
- Players choose between multiple branching routes
- Routes represent different risk/reward tradeoffs

### Stage Types Include:
- Scrolling combat stages
- Arena survival encounters
- Mini-boss hunts
- Timed objective events
- Hazard-focused challenge rooms

Not every run uses the same sequence of stages.

---

## Reducing Repetition

The game actively avoids repetition through:

- **Branching routes** on the world map
- **Run modifiers** (e.g. enemy behavior changes, environmental rules)
- **Biome-specific mechanics**
- **Boss variants** with different attack patterns
- **Objective variety** (survive, escort, hunt, hold zone)

Even familiar stages can play differently across runs.

---

## Progression Systems

### In-Run Progression
- Player levels up during a run
- Each level offers meaningful build choices
- Weapons, passives, and synergies combine into unique builds
- Builds can radically change how the game plays

### Meta Progression
- Unlock new ships, starting modules, and cosmetic items
- Meta progression expands **options**, not raw power
- No permanent stat advantages in competitive modes

---

## Weekly Challenges & Fair Play

The game includes **weekly skill-based challenges** designed to be fair and competitive.

Key rules:
- Fixed or standardized loadouts
- Normalized player stats
- Fixed random seed per challenge
- Leaderboards reflect skill, not grind or spending

These challenges exist alongside the main progression, not against it.

---

## Monetization Philosophy

- Cosmetic-only monetization
- Skins, visual effects variants, and UI themes
- No power boosts
- No stat advantages
- No pay-to-win mechanics

---

## Design Pillars

1. **Clarity first** — gameplay must always be readable
2. **Meaningful choices** — every upgrade should matter
3. **Short sessions, deep systems**
4. **Skill expression over grind**
5. **Modern presentation, timeless mechanics**

---

## Summary

The Hybrid Stage-Select Direction provides:
- Fast, engaging sessions
- High replay value without procedural chaos
- Strong foundations for long-term expansion
- A modern arcade identity that respects classic shmup design

This direction should be treated as the authoritative foundation for all visual, UI, gameplay, and systems decisions going forward.
