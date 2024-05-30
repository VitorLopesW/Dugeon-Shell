from classes.generic_character_class import generic_character
import random

def get_random_enemy(player):
    if player.level == 1 or player.level == 2:
        random_chance = random.randint(1, 100)
        if random_chance <= 30:
            return Young_wolf('Young Wolf')
        elif random_chance <= 60:
            return Wolf('Wolf')
        elif random_chance <= 90:
            return Goblin('Goblin')
        else:
            return Red_Goblin('Red Goblin')



class Goblin(generic_character):
    def __init__(self, name):
        super().__init__(name)
        # hp
        self.hp = 10
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
                random.randint(1,3) + self.strength,
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
        xp = 50 + random.randint(1, 20)
        gold = 30 + random.randint(1, 20)
        return xp, gold

class Red_Goblin(Goblin):
    def __init__(self, name):
        super().__init__(name)
        self.hp = 8
        self.current_hp = self.hp
        self.strength = 6
        self.agility = 3
        self.intelligence = 3
        self.luck = 3
    def get_defeat(self):
        xp = 70 + random.randint(1, 30)
        gold = 50 + random.randint(1, 30)
        return xp, gold

class Wolf(generic_character):
    def __init__(self, name):
        super().__init__(name)
        # hp
        self.hp = 15
        self.current_hp = self.hp
        # Type
        self.type = 'Wolf'
        self.weapon = 'teeth'
        # Stats
        self.strength = 1
        self.agility = 6
        self.intelligence = 0
        self.luck = 1
    def get_attack(self):
        attack_random = random.randint(1, 3)
        if attack_random == 1 or attack_random == 2:
            return (
                f"{self.name}, bites you with his sharp teeth!",
                random.randint(1,2) + self.strength,
                2,
                None
            )
        elif attack_random == 3:
            return (
                f"{self.name}, misses his bite!",
                0,
                0,
                None
            )
    def get_defeat(self):
        xp = 15 + random.randint(1, 40)
        gold = 0
        return xp, gold

class Young_wolf(Wolf):
    def __init__(self, name):
        super().__init__(name)
        self.hp = 5
        self.current_hp = self.hp
        self.strength = 1
        self.agility = 4
        self.luck = 1
    def get_defeat(self):
        xp = 10 + random.randint(1, 20)
        gold = 0
        return xp, gold