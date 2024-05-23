from classes.special_effecs_class import *
import random


class attack:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.damage = 1
        self.velocity = 'default'
        self.critical_damage = 'default'
        self.critical_chance = 'default'
        self.type = 'default'
    def special(self):
        return None 

class blade_attack(attack):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.type = 'Blade'
    def special(self):
        random_number = random.randint(1, 100)
        if random_number < 10:
            return bleed
        else:
            return None

