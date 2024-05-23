from classes.generic_character_class import generic_character

class Goblin(generic_character):
    def __init__(self, name):
        super().__init__(name)
        self.hp = 5
        self.current_hp = self.hp
        self.strength = 3
        self.agility = 3
        self.intelligence = 3
        self.luck = 3
        self.status = {
            'bleeding': False,
            'poisoned': False,
        }