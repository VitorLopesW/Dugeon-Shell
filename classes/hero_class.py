from classes.weapon_class import * 
from classes.generic_character_class import generic_character
import random

class Hero(generic_character):
    def __init__(self, name):
        super().__init__(name)
        # Level Up
        self.level = 1
        self.xp = 0
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
    # Attack 
    def get_attack(self, attack_position, equipment_position):
        equiped_weapon = self.equipment[equipment_position]
        active_attack = equiped_weapon.attacks[attack_position]
        base_damage = equiped_weapon.damage + active_attack.damage
        # Add random damage based on the modifier
        division = 3
        if self.modifier == 'agility':
            division = 2
        # Minimum and Maximum Damage
        minimum_damage = int(self.__dict__[self.modifier]/division)
        maximum_damage = self.__dict__[self.modifier]
        # Total Damage
        total_damage = base_damage + random.randint(minimum_damage, maximum_damage)
        # critical hit
        critical_chance = random.randint(1, 100)
        # critical modifier
        if equiped_weapon.critical_chance != 'default':
            critical_chance += equiped_weapon.critical_chance
        if active_attack.critical_chance != 'default':
            critical_chance += active_attack.critical_chance
        if(critical_chance >= 90):
            total_damage = total_damage * 1.5
        # special effects
        check_special_effect = active_attack.special()
        special_effect = None
        if check_special_effect != None:
            special_effect = check_special_effect.name
        # return
        return int(total_damage), critical_chance >= 90, special_effect
    

class Warrior(Hero):
    def __init__(self, name):
        super().__init__(name)
        # Stats
        self.hp = 16
        self.current_hp = self.hp
        self.strength = 10
        self.agility = 8
        self.intelligence = 3
        self.modifier = 'strength'
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
        self.modifier = 'intelligence'
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
        self.modifier = 'agility'
        # Equipment
        self.equipment['right_hand'] = dagger()
        self.gold += 100
    def level_up(self):
        super().level_up()
        self.strength += 1
        self.agility += 2
        self.luck += 1
        print(f"str: {self.strength}, agi: {self.agility}, int: {self.intelligence}, luck: {self.luck}")

