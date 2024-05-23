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

class slash(blade_attack):
    def __init__(self):
        super().__init__('Slash', 'A simple slash')
        self.damage = 2
        self.velocity = 1.2
        self.critical_damage = 1.5
        self.critical_chance = 10

class stab(blade_attack):
    def __init__(self):
        super().__init__('Stab', 'A quick stab')
        self.damage = 1
        self.velocity = 2
        self.critical_damage = 2
        self.critical_chance = 5

class mordhau(blade_attack):
    def __init__(self):
        super().__init__('Mordhau', 'A powerful overhead swing')
        self.damage = 3
        self.velocity = 0.6
        self.critical_damage = 1.5
        self.critical_chance = 15
    def special(self):
        return None