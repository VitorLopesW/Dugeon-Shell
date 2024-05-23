class Weapon:
    def __init__(self):
        self.name = 'Hand'
        self.base_damage = 1
        self.velocity = 1
        self.critical_damage = 'default'
        self.critical_chance = 'default'
        
# BLADES 

class Blade (Weapon):
    def __init__(self):
        super().__init__()
        self.base_damage = 2
        self.type = 'Blade'

class rusty_sword (Blade):
    def __init__(self):
        super().__init__()
        self.name = 'Rusty Sword'

class dagger (Blade):
    def __init__(self):
        super().__init__()
        self.name = 'Dagger'
        self.base_damage = 1
        self.velocity = 2

# AXES 

class axe (Weapon):
    def __init__(self):
        super().__init__()
        self.base_damage = 3
        self.type = 'Axe'
        self.velocity = 0.8

class long_axe (axe):
    def __init__(self):
        super().__init__()
        self.name = 'Long Axe'
        self.base_damage = 4
        self.velocity = 0.5

# WANDS

class wand (Weapon):
    def __init__(self):
        super().__init__()
        self.base_damage = 1
        self.type = 'Wand'

class wooden_wand (wand):
    def __init__(self):
        super().__init__()
        self.name = 'Wooden Wand'
        self.base_damage = 1
        self.velocity = 1.5




