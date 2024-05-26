from classes.attack_class import *

class Weapon:
    def __init__(self):
        self.name = 'Hand'
        self.damage = 1
        self.velocity = 1
        self.critical_chance = 'default'
        
# BLADES 

class Blade (Weapon):
    def __init__(self):
        super().__init__()
        self.damage = 2
        self.type = 'Blade'
        self.attacks = [
            slash(),
            #stab(),
            #mordhau()
        ]

class rusty_sword (Blade):
    def __init__(self):
        super().__init__()
        self.name = 'Rusty Sword'
        self.description = 'A rusty sword, but still sharp enough to cut a throat or two, but not much more than that.'

class dagger (Blade):
    def __init__(self):
        super().__init__()
        self.name = 'Dagger'
        self.damage = 1
        self.velocity = 2

# AXES 

class axe (Weapon):
    def __init__(self):
        super().__init__()
        self.damage = 3
        self.type = 'Axe'
        self.velocity = 0.8

class long_axe (axe):
    def __init__(self):
        super().__init__()
        self.name = 'Long Axe'
        self.damage = 4
        self.velocity = 0.5

# WANDS

class wand (Weapon):
    def __init__(self):
        super().__init__()
        self.damage = 1
        self.type = 'Wand'

class wooden_wand (wand):
    def __init__(self):
        super().__init__()
        self.name = 'Wooden Wand'
        self.damage = 1
        self.velocity = 1.5




