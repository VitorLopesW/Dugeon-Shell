from classes.weapon_class import * 

class Hero:
    def __init__(self, name):
        self.name = name
        # Level Up
        self.level = 1
        self.xp = 0
        self.hp = 10
        self.current_hp = self.hp
        # Stats
        self.strength = 5
        self.agility = 5
        self.intelligence = 5
        self.luck = 5
        # Equipment
        self.gold = 50
        self.equipment = {
            'left_hand': 'empty',
            'right_hand': Weapon(),
            'head': 'empty',
            'body': 'empty',
        }
        self.inventory = ['Lesser Healing Potion','Lesser Healing Potion']
    # Level Up
    def level_up(self):
        self.level += 1
        self.strength += 1
        self.agility += 1
        self.intelligence += 1
        self.luck += 1
        print(f"{self.name} has leveled up! {self.name} is now level {self.level}.")
    # Inventory Management
    def add_to_inventory(self, item):
        self.inventory.append(item)
    def remove_from_inventory(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
        else:
            print(f"{item} not found in inventory.")
    # Equipment Management
    def equip(self, bodyPart, item):
        self.equipment[bodyPart] = item
    def unequip(self, bodyPart, position):
        unequipped_equipment = self.equipment[bodyPart]
        self.equipment[bodyPart] = 'empty'
        if position == 'inventory':
            self.add_to_inventory(unequipped_equipment)
        else:
            pass
    

class Warrior(Hero):
    def __init__(self, name):
        super().__init__(name)
        # Stats
        self.hp = 16
        self.current_hp = self.hp
        self.strength = 10
        self.agility = 8
        self.intelligence = 3
        # Equipment
        self.equipment['right_hand'] = rusty_sword()

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
        self.current_hp = self.hp
        self.strength = 3
        self.agility = 8
        self.intelligence = 10
        # Equipment
        self.equipment['right_hand'] = wooden_wand()

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
        self.current_hp = self.hp
        self.agility = 10
        self.luck = 9
        self.strength = 3
        self.intelligence = 6
        # Equipment
        self.equipment['right_hand'] = dagger()
        self.gold += 100
    def level_up(self):
        super().level_up()
        self.strength += 1
        self.agility += 2
        self.luck += 1
        print(f"str: {self.strength}, agi: {self.agility}, int: {self.intelligence}, luck: {self.luck}")

