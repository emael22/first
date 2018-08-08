import random

pally_minions = {"Knife Juggler": [2, 2], "Silver Hand Recruit": [1, 1], "Tyrion Fordring": [6, 6],
                 "Mysterious Challenger": [6, 6]}
mage_minions = {"Mana Wyrm": [1, 3], "Kirin tor Mage": [4, 3], "Sorcerer's apprentice": [3, 2],
                "Water Elemental": [3, 6]}
hunter_minions = {"Hyena": [2, 2], "Houndmaster": [4, 3], "Savannah Highmane": [6, 5], "King Krush": [8, 8]}
priest_minions = {"Northshire Cleric": [1, 3], "Radiant elemental": [2, 3], "Auchenai Soulpriest": [3, 5],
                  "Prophet Velen": [7, 7]}
warrior_minions = {"Amani Berserker": [2, 3], "Garrosh": [4, 10], "Trognepute": [4, 8], "Direhorn hatchling": [3, 6]}

classes = {"hunter": hunter_minions, "mage": mage_minions, "paladin": pally_minions, "priest": priest_minions,
           "warrior": warrior_minions}

name = input("Choose your class")
player_minion = []

print(name, "selected")
while len(player_minion) < 3:
    player_minion.append(random.choice(list(classes[name])))

print("Your minions are :", player_minion)

cpu_class = random.choice(list(classes))
cpu_minion = []
print("CPU has selected", cpu_class)
while len(cpu_minion) < 3:
    cpu_minion.append(random.choice(list(classes[cpu_class])))

print("CPU minions are :", cpu_minion)

user_start = input("Wanna start the game ? y/n")
if user_start == "y":
    print("Let the battle begin !")
elif user_start == "n":
    exit()

winner_list = []

for round in range(3):
    round_in_progress = round + 1
    print("Battle", round_in_progress, ":", player_minion[round], "VS", cpu_minion[round])
    attack_value_player1 = classes[name][player_minion[round]][0]
    health_value_player1 = classes[name][player_minion[round]][1]
    attack_value_cpu1 = classes[cpu_class][cpu_minion[round]][0]
    health_value_cpu = classes[cpu_class][cpu_minion[round]][1]

    if attack_value_cpu1 >= health_value_player1 and attack_value_player1 < health_value_cpu:
        print("CPU", cpu_minion[round], "won round", round_in_progress, "!")
        winner_list.append(cpu_class)
    elif attack_value_cpu1 < health_value_player1 and attack_value_player1 >= health_value_cpu:
        print("Player 1", player_minion[round], "won round", round_in_progress, "!")
        winner_list.append(name)
    else:
        print("It's a draw")

if winner_list.count(cpu_class) > winner_list.count(name):
    print("CPU won ! :(")
elif winner_list.count(cpu_class) < winner_list.count(name):
    print("You Won !")
else:
    print("Draw Game")





