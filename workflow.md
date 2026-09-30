# Workflow: Adding and Updating Adventures

Files (all in /tmp/outputs): `silent-bell.twee` (the game), `design.md` (design notes), `changelog.md`, `validate.py`, and this file.

## Golden rules
1. Back up first: copy the twee to `/tmp/silent-bell.pre-<change>.twee`.
2. Edit with a scripted, assert-based Python patch (each replacement must match exactly once) instead of hand edits, so failures are loud.
3. Run `python3 validate.py` after every change and fix everything it reports.
4. Update all three docs together: `design.md` (what it is), `changelog.md` (what changed), and the game. A change is not done until all three agree.
5. Deliver all changed files.

## Conventions the code relies on
- SugarCube 2.36.1 only. Use `<b>`, not `**bold**`. `<<= >>` prints plain text only. Inside link callbacks use `<<capture>>` for temp variables.
- Attribute codes: `vig`, `fin`, `wit`, `pre`. Checks: `<<chk "attr" "Skill" hitsNeeded>>` (1 easy to 4 very hard). Fear checks in the Deep: `<<scare need dread>>`.
- One adventure = a run of passages with a shared name prefix (Prologue/Brackenford..., Rift..., Deep...). Each has an intro passage, a hub, several lairs or scenes, a finale, and endings that call banter (`setup.banterAll("end")`) before `<h2>The End</h2>`.
- Every scene sets `<<set $checkpoint to "PassageName">>` so defeat returns there.
- Fights: `setup.startFight({name, hp, guard, pool, dmg, loot, win:"Passage"})`. Do not pre-scale for party size; `startFight` does it.
- New shared state goes in `StoryInit`. Add a one-time-effect flag there for any NPC advantage.

## Adding a new adventure (checklist)
1. **Design first** in `design.md`: premise, hook, hub, 4-6 scenes, finale, endings, unique mechanic (if any), foes with stats, rewards, and what carries over.
2. **Sheet**: add a start link to the intro passage in the `Sheet` passage (currently Prologue, RiftIntro, DeepIntro).
3. **Passages**: prefix names consistently, add `$checkpoint`, use `<<chk>>` with needs from the difficulty table below.
4. **Hub extras**: `<<recruitlink "hubname">>`, `<<partylink>>`, and `talklink`s for each NPC. Add a hub entry to `setup.hubRoster` with 4 candidates from the roster (or new ones).
5. **NPCs**: add entries to `setup.npcs` (name, title, greet, 2-4 topics; one topic may carry an `effect` that sets a flag). Wire the flag into a check need, foe HP, or price at the point it matters.
6. **Companions**: to add one, put a full entry in `setup.companions` (role, roleText, pitch, three `talk` lines for Trust 0/1/2, chat lines, banter victory/dread/end, `t3` upgrade). Roles: Guardian (guard), Striker (pool, dmg), Healer (heal, healEvery), Trickster (weaken), Support (boost).
7. **Endings**: include `<<for _be range setup.banterAll("end")>>...<</for>>` before The End.
8. **Validate, simulate, document** (below).

## Updating an existing adventure
1. Read the passage(s) first, then patch with `pedit(name, old, new)`.
2. If you change a foe or a check, re-run the balance sim. If you change a rule in the JS, re-run it for all adventures.
3. If you rename a passage, search for every reference (links, `win:`, `$checkpoint`, `<<move>>`); the validator catches misses.
4. Record the change in `changelog.md` and adjust `design.md`.

## Difficulty and balance guide
- Check needs: 1 easy, 2 standard, 3 hard, 4 very hard. Companion aid gives +1 die when Trained; NPC hints lower a need by 1 (never below 1).
- Foe benchmarks (solo, unranked): minion hp 11-16, guard 1, pool 4; lair boss hp 20-26, guard 2, pool 5, dmg 2-3; final boss hp 30+ with the rank system.
- Party scaling is automatic: foe Stamina x1.2 (1 companion), x1.55 (2).
- Sim target (basic strategy, Blade/Spellwright/Voice): mid-game fights 85-95% solo, near 100% with two companions; finales 20-60% for an under-ranked party. Keep solo viable.
- Simulate with a Node harness: extract the Story JavaScript from the twee, stub `State`, `setup`, `random`, then loop `setup.startFight` / `setup.act("strike")` over the classes and party sets (see `/tmp/sim3.js` from this project).

## Files to touch, by change type
| Change | Game | design.md | changelog.md |
|---|---|---|---|
| New adventure | passages, Sheet, hubRoster, NPCs, StoryInit | new section | new entry (minor version) |
| New companion | setup.companions, hubRoster | roster table | entry |
| New NPC/topic | setup.npcs, passage link | NPC list | entry |
| Rules/balance | JS | rules + balance notes | entry |
| Bug fix | passage or JS | only if behavior changed | entry (Fixed) |

## Versioning
Bump the changelog heading: new adventure or system = next `vN`; smaller changes = `vN.x`. Newest entry first.

## Delivery
Send changed files with SendUserFile. Mention anything not verified in a real Twine run.
