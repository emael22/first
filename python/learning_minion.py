import random


class_list = ["hunter", "mage", "paladin", "priest", "warrior"]
pally_minions = {"knife juggler": [2, 2], "silver hand recruit": [1, 1], "Tyrion Fordring": [6, 6],
                 "Mysterious Challenger": [6, 6]}
mage_minions = {"Mana Wyrm": [1, 3], "Kirin tor Mage": [4, 3], "Sorcerer's apprentice": [3, 2], "Water Elemental": [3, 6]}
hunter_minions = {"hyena": [2, 2], "houndmaster": [4, 3], "Savannah highmane": [6, 5], "King Krush": [8, 8]}
priest_minions = {"Northshire Cleric": [1, 3], "Radiant elemental": [2, 3], "Auchenai Soulpriest": [3, 5],
                  "Prophet Velen": [7, 7]}
warrior_minions = {"Amani Berserker": [2, 3], "Garrosh": [4, 10], "Trognepute": [4, 8], "Direhorn hatchling": [3, 6]}


name = input("choose your class")
player_minion = []
if name == "hunter":
    print("hunter selected")
    while len(player_minion) < 3:
        player_minion.append(random.choice(list(hunter_minions)))
elif name == "mage":
    print("mage selected")
    while len(player_minion) < 3:
        player_minion.append(random.choice(list(mage_minions)))
elif name == "paladin":
    print("paladin selected")
    while len(player_minion) < 3:
        player_minion.append(random.choice(list(pally_minions)))
elif name == "priest":
    print("priest selected")
    while len(player_minion) < 3:
        player_minion.append(random.choice(list(priest_minions)))
elif name == "warrior":
    print("warrior selected")
    while len(player_minion) < 3:
        player_minion.append(random.choice(list(warrior_minions)))
print("Your minions are :", player_minion)

cpu_class = random.choice(class_list)
cpu_minion = []
if cpu_class == "hunter":
    print("CPU has selected hunter")
    while len(cpu_minion) < 3:
        cpu_minion.append(random.choice(list(hunter_minions)))
elif cpu_class == "mage":
    print("CPU has selected mage")
    while len(cpu_minion) < 3:
        cpu_minion.append(random.choice(list(mage_minions)))
elif cpu_class == "paladin":
    print("CPU has selected paladin")
    while len(cpu_minion) < 3:
        cpu_minion.append(random.choice(list(pally_minions)))
elif cpu_class == "priest":
    print("CPU has selected priest")
    while len(cpu_minion) < 3:
        cpu_minion.append(random.choice(list(priest_minions)))
elif cpu_class == "warrior":
    print("CPU has selected warrior")
    while len(cpu_minion) < 3:
        cpu_minion.append(random.choice(list(warrior_minions)))
print("CPU minions are :", cpu_minion)

user_start = input("Wanna start the game ? y/n")
if user_start == "y":
    print("let the battle begin !")
elif user_start == "n":
    exit()

print("Battle 1 :", player_minion[1],  "VS", cpu_minion[1])





