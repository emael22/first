import minions
import character_class
from character_class import CharacterClass
import random



cpu_minions = []
player1_class = input("choose your class")

while not CharacterClass.is_valid_class(player1_class):
    print("wrong class name, please re enter a class name.")
    print("Here are all the classes available :", CharacterClass.class_list)
    player1_class = input("choose your class")

print(player1_class, " selected")

player_minions = []
while len(player_minions) < 3:
    player_minions.append(random.choice())
print(player_minions)

#pu_class = random.choice(class_list)
#print(cpu_class, " selected")