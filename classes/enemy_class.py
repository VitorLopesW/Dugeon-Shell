class Enemy:
    def __init__(self):
        self.hp = 1
        self.strength = 1
        self.agility = 1
        self.intelligence = 1

class Goblin(Enemy):
    def __init__(self):
        super().__init__()
        self.hp = 10
        self.strength = 3
        self.agility = 1
        self.intelligence = 1