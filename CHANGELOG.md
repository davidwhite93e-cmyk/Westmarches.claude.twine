# Change Log: Tales of the Western Reach

Keep this file updated alongside `silent-bell.twee` and `design.md`. Newest entries first.

## v4.1: Workflow and tooling
- Added `workflow.md` (procedure for adding adventures and updating existing ones) and `validate.py` (link, macro, JS, NPC and companion reference checks). Current game passes with no findings.
- Fixed the title screen subtitle in `silent-bell.twee` ("Two" to "Three fantasy adventures").
- Corrected the passage counts in `design.md` (112) and added `claude-code-github-setup.md` (repository setup instructions for Claude Code).

## v4: Party, NPCs and dialogue (all three adventures)
**Added**
- Party of the player plus up to 2 companions; roster of 9 (Kess, Wren, Osric, Pip, Sable, Gar, plus story allies Bram, Tam, Vess).
- Hire candidates at a wanderers' table in each hub; story allies join free (Bram in Cells, Vess after a parley, Tam in the Deep chapel).
- Combat roles (Guardian, Striker, Healer, Trickster, Support), skill aid (+1 die when a companion is Trained), Trust 0-3 with personal stories, banter after victories, fear checks and endings.
- NPC topic menus for 14 NPCs across all adventures, with one-time effects (lower check difficulty, weaker foes, cheaper items, free items, clues).
- New passages: Talk, TalkTopic, Recruit, Party, PartyTalk, PartyJoin. New widgets: talklink, joinlink, partylink, recruitlink.
**Changed**
- Foes gain +20% Stamina with 1 companion and +55% with 2. Deep camps cost 2 Provisions with 2 companions. Broken nerve in the Deep makes companions below Trust 2 leave.
**Fixed**
- Two parley checks (Choirmaster, Rift vault) used the old "cha" attribute code; now "pre".
- Foes no longer get the Smallfolk reroll of 1s.
**Files:** silent-bell.twee (112 passages), design.md (new Party, NPCs and Dialogue section).

## v3: Adventure 3, the Deep (horror and resource crawl)
- Added Light, Dread, Provisions, the Stirring clock and hunts, oil flasks, holy salt, camps (chapel is safer), survivor Tam, and five endings.
- Balance pass: Spellwright armor 1, damage 3; Voice vitality 3; base Stamina 8 to 10; Blade vitality 4 to 3.

## v2: Design file
- Added design.md covering rules, options, adventures, balance and IP notes.

## v1: IP-clear rewrite
- Replaced D&D rules with a custom dice-pool system (four Attributes, Hits, Sparks, Callings, Lineages, Pasts).
- Removed Forgotten Realms and D&D terms; kept generic folklore races.
- Adapted the frontier-keep adventure into original Adventures 1 (Silent Bell) and 2 (the Rift).
