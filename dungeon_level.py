# This file handles the leveling system

import dungeon_stats
import random

# Level check compares current experience to the required experience, and acts accordingly.


def level_check():
    if dungeon_stats.exp >= dungeon_stats.tnl:
        print("Congratulations! You have reach level ", dungeon_stats.level + 1, "!")

        # The following code generates random stat gains for the character
        # if a level up is achieved, and prints out which stats were increased by how much.

        dungeon_stats.hpup = random.randint(40,70)
        dungeon_stats.max_health += dungeon_stats.hpup
        dungeon_stats.health = dungeon_stats.max_health
        dungeon_stats.mpup = random.randint(10,20)
        dungeon_stats.max_mana += dungeon_stats.mpup
        dungeon_stats.mana = dungeon_stats.max_mana
        dungeon_stats.atkup = random.randint(2,6)
        dungeon_stats.attack += dungeon_stats.atkup
        dungeon_stats.defup = random.randint(2,6)
        dungeon_stats.defense += dungeon_stats.defup
        dungeon_stats.magup = random.randint(2,6)
        dungeon_stats.magic_attack += dungeon_stats.magup
        dungeon_stats.level += 1
        dungeon_stats.tnl = dungeon_stats.tnl * 4
        print("Max HP increased by ", dungeon_stats.hpup)
        print("Max Mana increased by ", dungeon_stats.mpup)
        print("Attack increased by ", dungeon_stats.atkup)
        print("Defense increased by ", dungeon_stats.defup)
        print("Magic Attack increased by ", dungeon_stats.magup)
        print("You are ", (dungeon_stats.tnl - dungeon_stats.exp),
              " experience points away from level ", dungeon_stats.level + 1)

    # If more experience is needed, this'll print how much more is needed.

    else:
        print("You are ", (dungeon_stats.tnl - dungeon_stats.exp),
              " experience points away from level ", dungeon_stats.level + 1)
