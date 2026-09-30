# Tales of the Western Reach

A collection of three fantasy text adventures for Twine, written as a single Twee3 file for the SugarCube 2.36.1 story format. All three adventures share one character creator and one original dice-pool rules system. Characters have four Attributes (Vigor, Finesse, Wits, Presence), roll d6 pools where each 4+ is a hit, and add a Fate die. You pick one of nine Lineages, one of six Callings and a Past. Along the way you can talk to NPCs through topic menus and recruit up to two companions, each with a combat role, Trust levels and personal stories. The setting, places, characters and rules text are original generic fantasy.

## The adventures

1. **The Silent Bell of Brackenford.** Someone has stolen every bell in the river town of Brackenford. You follow the clues to Dunvar Hold and face the Hollow Choir and Choirmaster Veyle.
2. **The Weeping Rift.** A sandbox built around Thornwatch Keep: clear four lairs in any order, collect sigils, and open the Ashen Vault to face Ash-Priest Kessrick. The Rift also has a rank system.
3. **The Lampless Deep.** A horror dungeon crawl through a silver mine that has gone dark. You manage Light, Dread and Provisions while the Stirring builds toward hunts. It ends at the Heart Vault, where you seal, destroy or loot the source.

## How to play

The game is `src/silent-bell.twee` (112 passages).

- **Twine 2.6+:** in the Library choose Import, then pick `src/silent-bell.twee`. If Twine doesn't set the story format, choose SugarCube 2 (2.36.1).
- **Tweego:** with [Tweego](https://www.motoslave.net/tweego/) and SugarCube 2.36.1 installed, run `make build` (or `tweego -f sugarcube-2 -o dist/index.html src/`) and open `dist/index.html` in a browser. Tagged releases on GitHub attach a prebuilt `index.html`.

## Repository layout

```
src/silent-bell.twee     the game (source of truth)
docs/design.md           design notes: rules, adventures, foes, balance
docs/workflow.md         procedure for adding and updating adventures
CHANGELOG.md             change log, newest first
tools/validate.py        link, macro, JS and reference checker
tools/extract_js.py      extracts the Story JavaScript to build/check.js
tools/sim.js             fight-balance simulation (Node)
Makefile                 build, validate and sim targets
```

## Tools

Run these from the repository root. You need Python 3 and Node 20+.

- `python3 tools/validate.py` checks that every link, `<<goto>>`, `win:`, `<<move>>` and `$checkpoint` target exists. It also checks macro tag balance, `**bold**` markup, old attribute codes, JS syntax, and NPC and companion references. It prints `OK: no problems found` when everything passes.
- `python3 tools/extract_js.py` writes the Story JavaScript, with stubs for Node, to `build/check.js`.
- `node tools/sim.js` simulates fights for each calling and party mix and prints win rates. Run `extract_js.py` first.

CI runs the validator and a JS syntax check on every push and pull request to `main`.

## Contributing

Read [`docs/workflow.md`](docs/workflow.md) before you add or change an adventure. Every change to the game also updates `docs/design.md` and `CHANGELOG.md`.

## License

Copyright © the author. All rights reserved. No license is granted to copy, modify or distribute this work.
