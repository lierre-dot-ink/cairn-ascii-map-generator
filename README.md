# cairn-ascii-map-generator

Generates text-based maps based on the TTRPG Cairn2e setting generation procedure.

[Cairn 2e](https://cairnrpg.com/second-edition) has an analogue setting generation procedure that I really like. In a nutshell, it allows you to create a little region of the world for the player characters to evolve in.

This repository's goal is to automate this analogue procedure to generate little text based maps to integrate in the game master/"Warden"'s notes. Here is an example done for the map depicted in [the procedure](https://cairnrpg.com/second-edition/wardens-guide/setting-seeds/).

Given that the layout can be a matter of taste as well as not trivial to program, this little project's core goal is to:

- generate the actual text based map and its legend
- generate the basics for the path connecting the points of interest

```
┌──────────────────────────────────────────────────────────────────────┐
│                            MINERAL REACH                             │
├──────────────────────────────────────────────────────────────────────┤
│Legend:                Connections:                                   │
│                                                                      │
│ ░: plateau             ─── : path                                    │
│ ▓: wasteland           ─x─ : blocked path                            │
│  : mountain                                                          │
│ ║: river                                                             │
├───────╥────────────┬─────────────────────────────────────────────────┤
│░░░░   ║            │ 1: Heart: Fortress, Dangerous, Portal           │
│░7─x─┐ ╚═══╗  ┌───3 │ 2: Buried Megalith, Irregular Gravity           │
│░░░░ │     ║B │   │ │ 3: Buried Megalith, Trash Heap                  │
│░A░  6──┐  ║  │ ┌x┘ │ 4: Waypoint: Inn, Sacred Grounds                │
│░░░  │  ├──1──┘ │   │ 5: Dungeon: Fort, Mirrored                      │
│░░ ┌─┘  │▓▓╚══╗▓2─┐▓│ 6: Echoing Fields, Ancient Battle Site          │
│░░ 8────┘▓▓▓▓▓║┌┘▓4▓│ 7: Dungeon: Tower, Crumbling                    │
│░       ▓▓▓▓C▓║│▓▓│▓│ 8: Lair: Abandoned Tower, Something Sleeps      │
│░      ▓▓▓▓┌──║┘▓▓│▓│ A: Silver Face                                  │
│░░▓▓▓▓▓▓▓▓▓5──║─x─┘▓│ B: Broken Sundial                               │
│░▓▓▓▓▓▓▓▓▓▓▓▓▓║▓▓▓▓▓│ C: Great Waterwheel                             │
├──────────────╨─────┴─────────────────────────────────────────────────┤
│1 ─── 2: Road, 1 Watch, Mineral Flecks - Divided by Political Dispute │
│1 ─── 3: Wilderness, 2.5 Days, Dead Vegetation - Frequent Flash Floods│
│1 ─── 6: Road, 1 Watch, Rusted Tools - Firebug Hive                   │
│1 ─── 8: Trail, 2 Days, Massive Grooves - Bandit Ambushes             │
│2 ─x─ 3: Trail, 1.5 Days, Follows The Stars - Smoke Filled            │
│2 ─── 4: Trail, 1.5 Days, Abandoned Fields - Blocked by Giant Boulder │
│2 ─── 5: Trail, 2 Days, Overgrown - Poisonous Fruit                   │
│4 ─x─ 5: Cattle Prints, 2 Days, Steep Climb                           │
│6 ─x─ 7: Trail, 1 Days, Constant Patrols - Collapsed Bridge           │
│6 ─── 8: Road, 1 Days, Twisted - Gets Extremely Cold                  │
└──────────────────────────────────────────────────────────────────────┘
```
