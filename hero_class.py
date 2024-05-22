class Hero:
    def __init__(self, name):
        self.name = name
        # Level Up
        self.level = 1
        self.xp = 0
        self.hp = 10
        # Stats
        self.strength = 5
        self.agility = 5
        self.intelligence = 5
        self.luck = 5
        # Equipment
        self.gold = 50
        self.equipment = {
            'left_hand': 'empty',
            'right_hand': 'empty',
            'head': 'empty',
            'body': 'empty',
        }
        self.inventory = ['Lesser Healing Potion','Lesser Healing Potion']
    def level_up(self):
        self.level += 1
        self.strength += 1
        self.agility += 1
        self.intelligence += 1
        self.luck += 1
        print(f"{self.name} has leveled up! {self.name} is now level {self.level}.")

class Warrior(Hero):
    def __init__(self, name):
        super().__init__(name)
        # Stats
        self.hp = 16
        self.strength = 10
        self.agility = 8
        self.intelligence = 3

    def level_up(self):
        super().level_up()
        self.strength += 1
        self.agility += 1
        print(f"str: {self.strength}, agi: {self.agility}, int: {self.intelligence}, luck: {self.luck}")

class Wizard(Hero):
    def __init__(self, name):
        super().__init__(name)
        # Stats
        self.hp = 12
        self.strength = 3
        self.agility = 8
        self.intelligence = 10

    def level_up(self):
        super().level_up()
        self.intelligence += 4
        self.agility += 1
        print(f"str: {self.strength}, agi: {self.agility}, int: {self.intelligence}, luck: {self.luck}")

class Rogue(Hero):
    def __init__(self, name):
        super().__init__(name)
        #Stats
        self.hp = 14
        self.agility = 10
        self.luck = 9
        self.strength = 3
        self.intelligence = 6
    def level_up(self):
        super().level_up()
        self.strength += 1
        self.agility += 2
        self.luck += 1
        print(f"str: {self.strength}, agi: {self.agility}, int: {self.intelligence}, luck: {self.luck}")

