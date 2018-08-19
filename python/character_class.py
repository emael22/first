import random
import minions


class CharacterClass:

    health = 30
    class_list = ["pally", "hunter", "mage", "priest", "warrior"]

    def __init__(self, name, class_minions):

        self.name = name
        self.class_minions = class_minions

    @staticmethod
    def is_valid_class(name):
        return name in CharacterClass.class_list


pally = CharacterClass("paladin", [minions.knife_juggler, minions.silver_hand_recruit, minions.tyrion_fordring,
                                   minions.mysterious_challenger])
hunter = CharacterClass("hunter", [minions.scavenging_hyena, minions.houndmaster, minions.savannah, minions.king_krush])
mage = CharacterClass("mage", [minions.mana_wyrm, minions.sorcerers_apprentice, minions.kirintor_mage,
                               minions.water_elemental])
priest = CharacterClass("priest", [minions.northshire_cleric, minions.radiant_elemental, minions.auchenai,
                                   minions.prophet_velen])
warrior = CharacterClass("warrior", [minions.amani_berserker, minions.garrosh, minions.trognepute,
                                     minions.direhorn_hatchling])





