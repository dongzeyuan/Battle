# This file is a collection of enemies and their stats

import random
import dungeon_stats
import dungeon_battle

# This code generates a random number to select an enemy which will be pushed into the battle code.


def battle_start():
    dungeon_stats.inbattle = 1
    enemy = random.randint(1,2)

    # SLIME

    if enemy == 1:
        dungeon_stats.enemy_name = "Slime"
        dungeon_stats.enemy_hp = 30
        dungeon_stats.enemy_attack = 2
        dungeon_stats.enemy_defense = 1
        dungeon_stats.enemy_exp = 100
        dungeon_stats.escape = 7
        print("Slime Appeared!!")

    # BAT

    elif enemy == 2:
        dungeon_stats.enemy_name = "Bat"
        dungeon_stats.enemy_hp = 45
        dungeon_stats.enemy_attack = 3
        dungeon_stats.enemy_defense = 2
        dungeon_stats.enemy_exp = 150
        dungeon_stats.escape = 5
        print("Bat Appeared!!")
