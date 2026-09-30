# Tales of the Western Reach: Design Notes

Source of truth for the game in `silent-bell.twee`. Twine 2.6+ story, SugarCube 2 format, 112 passages. Import with Library, then Import. If the story format isn't set, choose SugarCube 2.

## Status

- Three adventures on one shared character creator and one rules system (112 passages, including the party, NPC and dialogue systems).
- The setting is generic fantasy. All Forgotten Realms and D&D terms were removed. Elf, Dwarf and Gnome remain as folklore staples.
- Checked by script: JS syntax, every link target exists, macro tags balance, and simulated fights run for all callings.
- Not yet playtested by hand in Twine. Enemy stats live in the `setup.startFight({...})` calls and are easy to tune.

## Rules

**Attributes:** Vigor, Finesse, Wits, Presence. Each starts at 1. Spend 6 points, max 4 each at creation. Lineage bonuses apply after, capped at 5.

**Checks:** roll (Attribute + 2 if Trained in the skill) d6, plus one Fate die.
- A die showing 4+ is a hit.
- Fate 6 = +2 hits. Fate 1 = -1 hit (only if you have one).
- Hits needed: 1 easy, 2 standard, 3 hard, 4 very hard.
- Smallfolk reroll any die showing 1 once. Gnomes get +1 die on Wits checks.
- Widget: `<<chk "attr" "Skill" hits>>`, which sets `_ok`. Attribute codes: vig, fin, wit, pre.

**Derived stats**
- Stamina = 10 + 2 x Vigor + calling bonus.
- Guard = calling armor + 1 if Finesse is 3+.
- Sparks = 3 (Human: 4). Refilled by resting.
- Healing draughts: start with 2, heal 3 + d4.
- Crowns = past's gold + 10.

**Combat**
- Attack pool = attack Attribute + 2 + rank bonus dice.
- Net hits = hits - foe Guard. If net is 1+, damage = weapon damage + net hits.
- Foes work the same way: foe pool vs your Guard, damage = foe damage + net hits.
- Each round, choose a stance:
  - Strike.
  - Press: +2 dice, your Guard -1 this round.
  - Brace: Guard +2 this round, recover 1 Stamina.
  - Feat: costs 1 Spark.
  - Drakeblood Breath: 4 damage, ignores Guard, once per rest.
  - Draught: heal 3 + d4.
- After your action, the foe acts. Tuskborn Relentless: drop to 1 Stamina instead of 0, once per rest.
- Defeat: wake at half Stamina, lose 5 crowns, return to the checkpoint passage (`$checkpoint`).
- Environmental damage (`setup.hurt`) never drops you below 1.

**Rank (Rift only):** each lair cleared gives +3 max Stamina, plus +1 attack die on every second rank.

## Character options

**Lineages**

| Lineage | Bonus | Extras |
|---|---|---|
| Human | +1 Presence, +1 Wits | extra Spark |
| Elf | +1 Finesse, +1 Wits | Nightsight, Perception |
| Dwarf | +2 Vigor | Nightsight, half trap/poison damage |
| Smallfolk | +1 Finesse, +1 Presence | reroll 1s once |
| Tuskborn | +2 Vigor | Nightsight, Intimidation, Relentless |
| Hellmarked | +1 Presence, +1 Wits | Nightsight, Deception |
| Drakeblood | +1 Vigor, +1 Presence | Breath Weapon |
| Gnome | +2 Wits | Nightsight, Investigation, +1 die on Wits |
| Twilight-kin | +1 Presence, +1 Finesse | Nightsight, Discernment |

Nightsight matters in Dunvar Hold's Hall of Echoes. Without it or a lantern, you take damage.

**Callings**

| Calling | Attacks with | Weapon dmg | Armor | Stamina bonus | Trained | Feat (1 Spark) |
|---|---|---|---|---|---|---|
| Blade | Vigor | 2 | 2 | 3 | Athletics, Intimidation | Cleaving Blow: +3 damage |
| Shadow | Finesse | 2 | 1 | 2 | Stealth, Pilfering | Backstab: +3 dice, ignore 1 Guard |
| Spellwright | Wits | 3 (Ember Bolt) | 1 | 1 | Occult, Investigation | Arcane Bolt: ignore Guard, +3 damage |
| Vowed | Vigor | 2 | 2 | 3 | Medicine, Religion | Mending Prayer: heal 4 + Presence |
| Wayfarer | Finesse | 2 | 1 | 3 | Survival, Perception | Twin Shot: two attacks |
| Voice | Finesse | 2 | 1 | 3 | Persuasion, Performance | Cutting Word: 3 damage, foe -3 dice next turn |

Recommended builds (Vigor/Finesse/Wits/Presence): Blade 4/2/2/2, Shadow 1/4/3/2, Spellwright 1/2/4/3, Vowed 3/1/3/3, Wayfarer 2/4/3/1, Voice 1/3/2/4.

**Pasts:** Old Soldier (Athletics, Intimidation, 10 crowns), Temple-raised (Discernment, Religion, 15), Gutter-born (Deception, Stealth, 15), Scholar (Occult, History, 10), Wilder (Survival, Athletics, 10), Village Champion (Beast-craft, Survival, 10).

**Extra trained skill (pick one):** Perception, Investigation, Persuasion, Discernment, Stealth, Acrobatics.

Creation flow: Name, Lineage, Calling, Past, Extra skill, Attributes, Sheet (choose adventure).

## Adventure 1: The Silent Bell of Brackenford

Setting: the river town of Brackenford on the River Sable. Someone stole every bell, and the robed Hollow Choir cult is behind it.

Flow: Prologue at a wrecked wagon, then the Brackenford hub, then a journey to Dunvar Hold, then a dungeon, then a boss.

- **Wagon (Maeve Thornbrook):** tend her wounds (Medicine) for a draught, or study the tracks (Perception) for a clue.
- **Brackenford hub:** Temple of First Light (Brother Alden, Religion clue), the Gilded Heron inn (Tomas, Persuasion or 2 crowns for a clue; rest for 3 crowns), the market (draught 8 crowns, lantern 2), and the docks (Old Corvin, clue plus river shortcut). Need 2 clues to leave.
- **Journey:** road ambush by a starving wolf, or the river route (Athletics, else minor damage).
- **Dunvar Hold:** Hall of Echoes trap (Investigation, History or Acrobatics; failure means dart damage), Chapel (fight, Stealth, or Deception), Cells (free Sergeant Bram, who helps in the boss fight and heals you), Bell Chamber.
- **Boss:** Choirmaster Veyle. Options: Discernment then Persuasion (2 hits if you read him first, else 4), sabotage the bell (Occult, Religion or Athletics), or fight. Endings: EndPeace, EndShatter, then TheEnd (+50 crowns).

| Foe | Stamina | Guard | Pool | Damage |
|---|---|---|---|---|
| Starving Wolf | 11 | 1 | 4 | 2 |
| Choir Acolytes | 16 | 1 | 4 | 2 |
| Veyle | 26 | 2 | 5 | 2 |

Veyle if the bell was sabotaged: Stamina 18, Guard 1, Pool 4. If Bram is with you, Pool -1.

## Adventure 2: The Weeping Rift

Inspired by the classic frontier-keep-and-caves structure, but with its own keep, factions and plot. Sandbox hub play.

- **Thornwatch Keep hub:** Warden-Captain Isolde Marrow (briefing, first-visit flask and 10 crowns), the Traders' Yard (draught 8, lantern 2, antitoxin 5), the Broken Shield tavern (rumors, rest 3 crowns), and the ravine.
- **Four lairs, any order:** each has several approaches (skill checks that weaken or bypass the fight). Every clear gives a sigil, 12 crowns plus loot, and a rank-up.
  - Sporegrotto (Survival, Medicine, or fire).
  - Crimson Ledger camp (Persuasion, Intimidation or Stealth can skip the fight).
  - Silk Galleries (Perception, Athletics, or fire; antitoxin lowers the spider's damage).
  - Brine Cistern (pay 10 crowns, Persuasion, Intimidation, or fight the hag).
- **Ashen Vault:** opens with 3+ sigils. Boss: Ash-Priest Kessrick. Options: Persuasion (2 hits with 4 sigils, else 3), sabotage the idol (Occult or Religion), or fight. Ending: RiftEnd (+100 crowns).

| Foe | Stamina | Guard | Pool | Damage |
|---|---|---|---|---|
| Sporebound Wanderers | 8 or 13 | 0 | 3 | 1 |
| Ledger Captain Harl Vess | 20 | 2 | 5 | 2 |
| Silk-Weaver | 10 or 16 | 1 | 5 | 3 (2 with antitoxin) |
| Cistern Hag | 20 | 1 | 5 | 2 |
| Kessrick | max(16, 32 - 3 x sigils - 5 if idol cracked) | 2 | 6 - floor(sigils / 2) | 3 |

Lower Stamina applies when your approach check succeeds.

## Adventure 3: The Lampless Deep (horror dungeon crawl)

Orrow's Deep, a silver mine under the hill village of Orrow's Rest, has gone dark. The Mine-Warden, Ilse Varn, hires you to find out why and seal it. The entity below is the Lampless One, an absence that eats light.

**Crawl resources** (the point of this adventure; all default to 0 in the other two):
- **Light** (0-12): every step (`<<move>>`) burns 1. Nightsight lineages burn it only on odd steps. At 0, each step adds +1 Dread. Oil flasks refill 6.
- **Dread** (0-10): at 3 you are Shaken (-1 die on all checks and attacks), at 6 Haunted (-2 dice), at 10 you break (`DeepBroken`: flee to the surface, Dread resets to 6, lose 1 Provision, progress is kept). Eased by camping (-3, or -4 at the Chapel of Lamps) and holy salt (-2).
- **Provisions:** 1 per camp. Camping restores Stamina, Sparks, Breath and Relentless.
- **The Stirring:** each step +1, each camp +2 (+1 in the Chapel), some failed checks +1 or +2. When it reaches the threshold (first at 6, then every 6 more), the next move is interrupted by a hunt (`DeepHunt`) scaled by depth: Skulking Dark (10 Stamina, Guard 1, Pool 4, damage 2), Hollow Miner (14, 1, 5, 2), Lampless Thing (18, 2, 5, 3).
- **Defeat in the crawl:** wake at the last camp with half Stamina, -1 Provision, -2 Light, +2 Dread.
- **Resolve check:** Presence + 2 if you are Trained in Religion, Intimidation, Discernment or Performance, +1 die if Tam is with you. Used by `<<scare hits dread>>`, which adds Dread on failure.
- **Surface prep** (`DeepSurface`): oil flask 3 crowns, Provisions 2, holy salt 5, healing draught 8, bunkhouse rest 3. Start with Light 6 and 2 Provisions. You can return to the surface between descents.

**Map** (each arrow is one step; camp sites in brackets):
- Depth 1: Adit [camp], Cart Tunnel, Bunkhouse [camp], Collapsed Shaft. Adit connects to Carts and Bunkhouse, and both connect to the Shaft.
- Depth 2: Lower Landing, Flooded Gallery, Assay Office, Chapel of Lamps [best camp], Echo Hall. Landing connects to Flood, Assay and Chapel. Assay and Chapel connect. Flood leads to Echo.
- Depth 3: Lampless Gate (no camp), Heart Vault. Echo leads to Gate, and Gate to Heart.
- The direct route is 8 steps. Detours to Assay and Chapel add 2 each.

**Events**
- Carts: search (Perception, +1 Provision) and listen (Discernment, learn the binding name Orrow Venn).
- Bunkhouse: dust-sleepers (Resolve), +1 flask and +1 Provision.
- Shaft: Acrobatics, Athletics, or spend 2 Light. Always passable, failure costs resources.
- Flooded Gallery: Silt-stalker (14 Stamina, Guard 1, Pool 5, damage 2) or bypass with Athletics, Stealth, or a thrown flask.
- Assay Office: read the journal (Investigation; reveals the sealing rite needs the chalk and 4 Light) and open the strongbox (Pilfering or Athletics; sealing chalk). Retries add Stirring.
- Chapel of Lamps: survivor Tam Orrick (Persuasion or Medicine; +2 Provisions, +1 die on Resolve) and a votive lamp (+2 Light).
- Echo Hall: answer the voice (Resolve, learn the name), run (Athletics), or sing (Performance, +20 crowns).
- Lampless Gate: Wick-Wraith (18, Guard 2, Pool 5, damage 3) or sneak (Stealth) or burn 3 Light.
- Heart Vault: seal it (needs the journal, chalk and 4 Light; Religion or Occult, 2 hits if you know the name else 3), improvise a ward (Occult, 4 hits), fight the Lampless One (30 Stamina, Guard 2, damage 3, Pool 6 with 1-3 Light, 5 with 4+ Light, 7 with 0 Light), or grab silver and run.
- Endings: DeepEndSeal (+60 crowns), DeepEndDestroy (+60), DeepEndGreed (+80, bittersweet).

**Resource pacing (simulated):** a direct run costs 8 Light, so Light 6 is not enough. With detours and a camp it costs about 12, plus 4 for the rite. Expect to buy flasks and use the two found in the dungeon. Hunts trigger about once on a direct run and twice with detours.

## Balance notes

Simulated fights (bot uses a feat first, drinks a draught below 6 Stamina). Boss win rates with recommended builds: Blade, Vowed, Wayfarer 92-95%, Shadow and Spellwright 87-94%, Voice 78-80%. Weakest calling is Voice in straight fights, but it has the best social options. Ranks and draughts help in the Rift.

## Technical notes

- **Special passages:** StoryInit (state defaults), StoryCaption (sidebar), Widgets (`chk`), Story JavaScript (all rules in `setup.*`), Story Stylesheet.
- **Key state:** `$final` (Attributes), `$skills`, `$hp`, `$maxhp`, `$guard`, `$sparks`, `$potions`, `$gold`, `$fight`, `$checkpoint`, `$sigils`, `$rift`, `$rank`, `$atkBonus`. Deep crawl: `$light`, `$dread`, `$prov`, `$flasks`, `$salt`, `$stir`, `$nextHunt`, `$hunt`, `$huntDest`, `$depth`, `$seen` (per-room event flags), `$survivor`, `$knowsName`, `$journal`, `$chalk`, `$crawling`.
- **Crawl widgets:** `<<move "Passage" "Label">>` (burns Light, adds Stirring, may divert to a hunt or to `DeepBroken`), `<<scare hits dread>>` (Resolve check), `<<packlink>>` (opens `DeepPack`), `<<camplink>>` (camp at the current room). Room passages avoid rolls on entry; rolls happen in sub-passages so re-rendering the room (e.g. closing the pack) is harmless.
- **Starting a fight:** `<<run setup.startFight({name, hp, guard, pool, dmg, loot, win:"PassageName"})>><<goto "Combat">>`. Combat routes to Victory (then `$fight.win`) or Defeat.
- **Choices with state changes:** `<<link>>` with `<<goto>>` (creation +/- buttons reload the passage).
- **Markup gotcha:** SugarCube doesn't render `**bold**`. Use `<b>`.

## IP notes

The setting, places, NPCs, plots, and rules text are original. The mechanics follow common dice-pool ideas (d6 pool, count 4+, extra die). It's a generic-fantasy adaptation, so it is safe from Forgotten Realms and D&D naming. Not legal advice; check any commercial use with a lawyer.

## Possible next steps

Hand playtest and tune foe stats. Add rank progression to adventure 1. Add more Rift lairs, hirelings, or gear. Add Twine story-format polish (title art, save slots).

---

## Party, NPCs and Dialogue (all three adventures)

**Party size.** The player plus up to 2 companions. A third would need someone sent away first (Party screen).

**Recruiting.** Two routes. (1) *Hire* at a wanderers' table in each hub (Gilded Heron, Broken Shield, Orrow's Rest) for a crown fee, four candidates per hub. (2) *Story allies* who join free after being rescued or won over: Bram Holloway (Adventure 1 Cells), Harl Vess (Adventure 2, if persuaded or faced down rather than robbed), Tam Orrick (Adventure 3 chapel, once found). Companions carry over between adventures.

**Roster (9).**

| Companion | Role | Effect in combat | Trained | Fee |
|---|---|---|---|---|
| Kess Dunmarrow (dwarf) | Guardian | +1 Guard (+2 at Trust 3) | Athletics, Survival | 8 |
| Wren Ashgrove (elf) | Striker | 4 dice, dmg 2 (5 dice at T3) | Perception, Stealth | 10 |
| Osric Vale (temple healer) | Healer | Heals 3 every 2nd round (every round at T3) | Medicine, Religion | 6 |
| Pip Copperkettle (smallfolk) | Trickster | Foe -1 die (-2 at T3) | Pilfering, Stealth | 5 |
| Sable Marrowe (hellmarked) | Striker | 3 dice, dmg 2, ignores Guard (dmg 3 at T3) | Occult, Investigation | 12 |
| Gar Thorne (tuskborn) | Striker | 4 dice, dmg 3 (5 dice at T3) | Athletics, Intimidation | 9 |
| Bram Holloway | Guardian | +1 Guard (+2 at T3) | Athletics, Perception | free |
| Tam Orrick | Support | Your next attack +2 dice (+3 at T3) | Survival, Discernment | free |
| Harl Vess | Striker | 5 dice, dmg 2 (dmg 3 at T3) | Intimidation, Persuasion | free |

Hub rosters: Bell: Kess, Wren, Pip, Osric. Rift: Kess, Osric, Sable, Gar. Deep: Wren, Pip, Sable, Gar.

**Skill aid.** If a companion is Trained in the skill being checked, you get +1 die (shown as "Aid" on the check). Lost while Dread is 6 or higher. Resolve is aided by Religion/Intimidation/Discernment/Performance companions.

**Trust (0-3).** Each companion may talk once per rest/camp. Each talk moves Trust up one step and gives a personal story (three per companion); at Trust 3 the role bonus upgrades and later talks are short banter. In the Deep, a talk also removes 1 Dread. Story allies start at Trust 1.

**Costs.** Each hire costs crowns. Foes gain +20% Stamina with one companion and +55% with two. In the Deep, camping with two companions costs 2 Provisions. If you break in the Deep, companions with Trust below 2 desert.

**Banter.** Companions comment after victories, after failed Resolve checks (Dread), and at all five endings.

**NPC dialogue.** A data-driven topic menu (`setup.npcs`). Each topic can be asked once for its effect; re-asking just repeats the text.
- Adventure 1: Maeve (clue, cheaper draughts after you tended her, Bram hook), Brother Alden (Veyle backstory eases the parley, bell-breaking tip, free draught), Tomas (weaker wolf), Old Corvin (Hall of Echoes needs 1 less hit), Bram, Veyle (understand his grief).
- Adventure 2: Marrow (Ledger and Cistern hints, Kessrick's history), Hessa (Spore and Silk foes -2 Stamina), Vess, Marga, Kessrick.
- Adventure 3: Warden Varn (free oil flask, Orrow Venn's name), Old Dorrin (Wraith needs only 2 Light, holy salt for 3 crowns), Tam.

**Balance (simulated, 1500 runs per cell, basic strategy).** A Blade goes from 90% (solo) to about 100% against the Choirmaster with two companions, while an unranked Spellwright or Voice reaches 92-100%. Solo play remains viable; two companions trade a large power boost for money, Provisions and tougher foes.

**Technical.** New passages Talk, TalkTopic, Recruit, Party, PartyTalk, PartyJoin. New widgets talklink, joinlink, partylink, recruitlink. Party state: `$party` (ids), `$trust` (id to 0-3), `$campTalk` (reset on rest), `$talked` (topics used).
