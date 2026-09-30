# CLAUDE.md

Project memory for Claude Code sessions.

## What this is

"Tales of the Western Reach": three fantasy text adventures (The Silent Bell, The Rift, The Deep) in one Twee3 file for Twine using SugarCube 2.36.1. The game has a custom dice-pool rules system, NPC dialogue and a recruitable party.

## Layout

```
src/silent-bell.twee      the game (source of truth)
docs/design.md            design notes: what the game is (rules, adventures, foes, balance)
docs/workflow.md          procedure for adding and updating adventures
CHANGELOG.md              what changed, newest first
tools/validate.py         checker; run from the repo root
tools/extract_js.py       writes the Story JavaScript to build/check.js (gitignored)
tools/sim.js              fight-balance sim; loads build/check.js
Makefile                  build (Tweego -> dist/index.html), validate, sim
.github/workflows/        validate.yml (CI), release.yml (tagged builds)
```

## Rules

- Edit with small, exact patches. Each replacement must match exactly once, so failures are loud. Read the passage before you patch it.
- Run `python3 tools/validate.py` after every change. It must print `OK: no problems found`.
- SugarCube only. Use `<b>`, not `**bold**` (SugarCube doesn't render Markdown bold).
- Attribute codes are `vig`, `fin`, `wit`, `pre`. The old codes (`cha`, `str`, `dex`, `con`, `int`) are errors.
- Never pre-scale foes for party size. `setup.startFight` does it.
- Every scene sets `<<set $checkpoint to "PassageName">>` so defeat returns there.
- If you change a foe, a check or a rule in the JS, re-run the sim: `python3 tools/extract_js.py && node tools/sim.js`.
- Any change to the game must also update `docs/design.md` and add an entry to `CHANGELOG.md` (newest first; `vN` for a new adventure or system, `vN.x` for smaller changes). A change isn't done until all three agree.
- Keep the game clear of D&D, Forgotten Realms and other third-party IP. Generic folklore races (elf, dwarf, gnome and so on) are fine.
- Don't claim something was playtested in Twine unless it was. Say which checks actually ran.

## Adding or updating adventures

Follow `docs/workflow.md`. It has the new-adventure checklist, the update procedure, the difficulty and balance guide, and which files each change type touches.
