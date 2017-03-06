# This class is used to control the battle system for the game, Including
# which monster's you run into, as well as the rest of the battle sequence.

import random
import dungeon_stats
import dungeon_level
import dungeon_enemy

# This begins the battle phase


def battle():
    # This calls the battle start def, which selects the enemy the character fights
    dungeon_enemy.battle_start()

    # Loop will stay active as long as enemy is alive
    while dungeon_stats.inbattle > 0:
        print("What will you do?")
        action = input("> ")
        commands[action]()

# These Definitions control the various commands.

# Fight - Players basic attack.


def fight():
        damage = ((random.randint(1,5) * dungeon_stats.attack) / dungeon_stats.enemy_defense)
        dungeon_stats.enemy_hp -= damage
        print("You did ", damage, "damage.")
        if dungeon_stats.enemy_hp <= 0:
            print("You won!")
            print("You have gained", dungeon_stats.enemy_exp, "EXP!")
            dungeon_stats.exp += dungeon_stats.enemy_exp
            dungeon_level.level_check()
            dungeon_stats.inbattle = 0
        else:
            enemy_turn()

# Magic - Players equipped magic attack.


def magic():
    if dungeon_stats.mana < dungeon_stats.magcost:
        print("You don't have enough Mana...")
    else:
        magic_damage = (random.randint(2,7) * dungeon_stats.magic_attack)
        dungeon_stats.enemy_hp -= magic_damage
        print("You cast Magic...")
        print(dungeon_stats.enemy_name, " takes ", magic_damage, " in magic damage.")
        dungeon_stats.mana -= 5
        if dungeon_stats.enemy_hp <= 0:
            print("You won!")
            print("You have gained", dungeon_stats.enemy_exp, "EXP!")
            dungeon_stats.exp += dungeon_stats.enemy_exp
            dungeon_level.level_check()
            dungeon_stats.inbattle = 0
        else:
            enemy_turn()

# Escape - Attempts escape from battle


def escape():
    if dungeon_stats.escape > random.randint(0,9):
        print("You have Escaped.")
        dungeon_stats.inbattle = 0
    else:
        print("You failed to escape...")
        enemy_turn()


# This command gives info about the commands available to the player.


def help():
    print("""Type "fight" to do a regular attack.
    Type "magic" to use a magic spell attack. Type "run" if you need to try escaping.""")


# This runs through the enemies turn.


def enemy_turn():
    enemy_damage = ((random.randint(1,4) * dungeon_stats.enemy_attack) / dungeon_stats.defense)
    dungeon_stats.health -= enemy_damage
    print(dungeon_stats.enemy_name, " did ", enemy_damage,
          "damage to you. You have ", dungeon_stats.health, "remaining.")
    if dungeon_stats.health <= 0:
        print("You died!")
        raw_input("> ")
        exit()


# The various commands available during battle.

commands = {"fight": fight, "magic": magic, "run": escape, "help": help}