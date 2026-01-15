# Art Bible (Expanded) — Modern Arcade Shooter

## Design Intent
The game should look modern, premium, and clarity-first: a contemporary arcade shooter with clean HD 2D rendering and restrained neon energy.

This is NOT retro, gritty realism, or painterly concept art. The look should feel like a polished modern 2D game with crisp shapes and clear UI.

---

## Rendering Rules (Hard)
- HD 2D vector-style illustration
- Smooth edges everywhere
- Flat color surfaces with controlled gradients (use gradients sparingly)
- No texture noise, no grit overlays, no “film grain”
- Background detail is intentionally minimal
- Avoid “busy” starfields, clouds, fog, or noisy procedural textures

---

## Readability Hierarchy (Hard)
1) Player ship silhouette
2) Enemy silhouettes + telegraphs
3) Projectiles (danger)
4) Pickups and XP shards
5) UI (status)
6) Background (theme)

If anything threatens this hierarchy, simplify it.

---

## Palette (Base + Rules)
Base palette suggestion (adjust per biome, keep contrast):
- Background: deep navy / near-black
- Player identity: cyan/blue
- Enemy identity: red/orange
- Neutral hazards: purple or acid green (use sparingly)
- Reward items: gold/yellow

Rules:
- Background saturation stays low
- Gameplay saturation stays higher
- Telegraphs are brighter than damage projectiles
- Avoid equal brightness across everything (causes mush)

---

## Shape Language (Hard)
### Player ships
- Arrow/triangular forward motion
- 2–3 “hero angles”: front, 3/4, side
- Profile must be recognizable at small scale

### Enemies
- Each enemy type has a signature shape:
  - “Fodder” = small, simple, numerous
  - “Ranged” = asymmetric cannons
  - “Ram” = pointed, aggressive
  - “Elite” = larger, chunkier silhouette
  - “Spawner” = bulbous core + vents
- Use “negative space” (holes, gaps) to keep shapes readable

### Bosses
- Large, graphic forms with clear readable appendages
- 2–3 major attack patterns only (readable phases)
- Telegraphs must be unmistakable

---

## Projectiles & Telegraphs
Each projectile family must look distinct:
- Beam: thin straight line + crisp endpoint
- Bolt: rounded capsule + trail
- Spread: small triangles or chevrons
- Homing: teardrop + gentle curve trail
- AoE: clear boundary circle/cone/arc

Telegraphs:
- Use outline shapes, wedges, arcs, rings
- Telegraph opacity 40–70% (visible but not blocking)
- Telegraph duration long enough to react (visual design supports gameplay)

---

## VFX Language (Restrained, Modern)
Goals:
- Show impact and reward without obscuring gameplay.

Rules:
- Explosions are short-lived and graphic (shape bursts)
- Limit particle counts
- Avoid smoke/fog layers
- Shield hit: clean ripple or hex arc, quick flash
- Pickup: subtle pulse ring and glow, not spark spam

---

## UI Style Guide
- Floating panels, minimal borders
- Consistent corner radius and stroke width
- Icons as primary language; text is minimal
- Use spacing generously (mobile-safe)
- Avoid decorative frames that reduce content area

HUD baseline layout suggestion:
- Top-left: HP/Shield + status
- Top-right: score/timer/objective
- Bottom corners: abilities/cooldowns, weapon slots

---

## Typography Guidance (No fonts required)
- Geometric sans feel
- All caps for headers
- Numbers large and spaced
- Short labels only (e.g., “UPGRADE”, “STAGE 2”, “WEEKLY”)

---

## Consistency Anchors
- Player ship silhouette stays consistent across all images
- Enemy families share a language but remain distinct
- Icon style consistent (stroke weight, corner radius, fill approach)
- HUD component locations consistent

---

## Acceptance Checklist (Quick)
✅ No texture noise
✅ Background subdued
✅ Player silhouette pops
✅ Telegraphs unmistakable
✅ UI readable at a glance
✅ Effects don’t hide bullets
