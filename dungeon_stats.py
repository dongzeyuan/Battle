# This class contains the various stats to be used in the game, including both Player and Enemy stats.

# Call this definition to show current stats.


def stats():
    print("HP:   ", health, "/", max_health)
    print("MP:   ", mana, "/", max_mana)
    print("ATK:  ", attack)
    print("DEF:  ", defense)
    print("M-ATK:", magic_attack)
    print("EXP:  ", exp, "/", tnl)


# Character stats

level = 1
max_health = 100
health = 100
max_mana = 20
mana = 20
exp = 0
tnl = 200
attack = 2
wpnatk = 0
defense = 1
armdef = 0
magic_attack = 2
magcost = 5
magspell = 0
escape = 0

# Leveling

hpup = 0
mpup = 0
atkup = 0
defup = 0
magup = 0

# Enemies

enemy_name = ""
enemy_hp = 0
enemy_attack = 0
enemy_defense = 0
enemy_magdef = 0
enemy_exp = 0
inbattle = 0
