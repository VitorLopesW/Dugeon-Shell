class Hero:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.strength = 5
        self.agility = 5
        self.intelligence = 5
        self.luck = 5
        self.xp = 0

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
        self.strength = 10
        self.agility = 8
        self.intelligence = 3
        self.weapon = 'Broken Sword'

    def level_up(self):
        super().level_up()
        self.strength += 1
        self.agility += 1
        print(f"str: {self.strength}, agi: {self.agility}, int: {self.intelligence}, luck: {self.luck}")

class Wizard(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.strength = 3
        self.agility = 8
        self.intelligence = 10
        self.weapon = 'Novice Wand'

    def level_up(self):
        super().level_up()
        self.intelligence += 4
        self.agility += 1
        print(f"str: {self.strength}, agi: {self.agility}, int: {self.intelligence}, luck: {self.luck}")

class Rogue(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.agility = 10
        self.luck = 9
        self.strength = 3
        self.intelligence = 6
        self.weapon = 'Rusty Dagger'
    def level_up(self):
        super().level_up()
        self.strength += 1
        self.agility += 2
        self.luck += 1
        print(f"str: {self.strength}, agi: {self.agility}, int: {self.intelligence}, luck: {self.luck}")

