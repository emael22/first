import random


class CharacterClass:

    name = str
    health = 30
    class_minions = []

    def __init__(self, health, name, class_minions):
        self.health = health
        self.name = name
        self.class_minions = class_minions


class Minions:

    def __init__(self, name, attack, health, mana_cost):
        self.name = name
        self.attack = attack
        self.health = health
        self.mana_cost = mana_cost


knife_juggler = Minions("knife juggler", 2, 2, 2)
silver_hand_recruit = Minions("silver hand recruit", 1, 1, 1)
mysterious_challenger = Minions("Mysterious Challenger", 6, 6, 6)
tyrion_fordring = Minions("Tyirion Fordring", 6, 6, 8)

scavenging_hyena = Minions("Scavenging Hyena", 2, 2, 2)
houndmaster = Minions("houndmaster", 4, 3, 4)
savannah = Minions("Savannah Highmane", 6, 5, 6)
king_krush = Minions("King Krush", 8, 8, 9)

mana_wyrm = Minions("Mana Wyrm", 1, 3, 1)
kirintor_mage = Minions("Kirin Tor Mage", 4, 3, 3)
sorcerers_apprentice = Minions("Sorcerer's apprentice", 3, 2, 2)
water_elemental = Minions("Water Elemental", 3, 6, 4)

northshire_cleric = Minions("Northshire Cleric", 1, 3, 1)
radiant_elemental = Minions("Radiant Elemental", 2, 3, 2)
auchenai = Minions("Auchenai Soulpriest", 3, 5, 4)
prophet_velen = Minions("Prophet Velen", 7, 7, 7)

amani_berserker = Minions("Amani Berserker", 2, 3, 2)
garrosh = Minions("Garrosh", 4, 10, 8)
trognepute = Minions("Trognepute", 4, 8, 8)
direhorn_hatchling = Minions("Direhorn Hatchling", 3, 6, 5)

pally = CharacterClass(30, "paladin", [knife_juggler, silver_hand_recruit, tyrion_fordring, mysterious_challenger])
hunter = CharacterClass(30, "hunter", [scavenging_hyena, houndmaster, savannah, king_krush])
mage = CharacterClass(30, "mage", [mana_wyrm, sorcerers_apprentice, kirintor_mage, water_elemental])
priest = CharacterClass(30, "priest", [northshire_cleric, radiant_elemental, auchenai, prophet_velen])
warrior = CharacterClass(30, "warrior", [amani_berserker, garrosh, trognepute, direhorn_hatchling])

class_list = [pally.name, hunter.name, mage.name, priest.name, warrior.name]

player_minions = []
cpu_minions = []

player1_class = input("choose your class")

print(player1_class, " selected")
while len(player_minions) < 3:
    player_minions.append(random.choice(CharacterClass.class_minions[player1_class]))
print(player_minions)

cpu_class = random.choice(class_list)
print(cpu_class, " selected")



