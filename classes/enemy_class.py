from classes.generic_character_class import generic_character
import random

class Goblin(generic_character):
    def __init__(self, name):
        super().__init__(name)
        # hp
        self.hp = 1
        self.current_hp = self.hp
        # Type
        self.type = 'Goblin'
        self.weapon = 'Club'
        # Stats
        self.strength = 3
        self.agility = 3
        self.intelligence = 3
        self.luck = 3
    def get_attack(self):
        attack_random = random.randint(1, 3)
        if attack_random == 1:
            return (
                f"{self.name},  Strike with all your might, bring your {self.weapon}! down",
                random.randint(3,6) + self.strength,
                2,
                None
            )
        elif attack_random == 2:
            return (
                f"{self.name}, smash with his {self.weapon}!",
                7,
                1,
                None
            )
        elif attack_random == 3:
            return (
                f"{self.name}, tries to hit you with his {self.weapon}, but misses!",
                0,
                0,
                None
            )
    def get_defeat(self):
        xp = 10 + random.randint(1, 20)
        gold = 10 + random.randint(1, 20)
        return xp, gold

