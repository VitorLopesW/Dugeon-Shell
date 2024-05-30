from classes.hero_class import *
from utils.ascii_arts import *
from adventure.index import *

def create_character():
    print('Welcome to the character creation!')
    # Name
    name = input('Enter your name: ')
    while True: 
        confirm_name = input(f'Are you sure you want to name your character {name}? (Y/N): ')
        if confirm_name.lower() == 'y':
            break
        else:
            name = input('Enter your name: ')
    # Class
    character_class = input('Choose your class: 1 - Warrior, 2 - Mage, 3 - Rogue: ')
    while True:
        if character_class == '1':
            print(ascii_warrior)
            player = Warrior(name)
            if are_you_sure(player):
                break
        elif character_class == '2':
            print(ascii_mage)
            player = Wizard(name)
            if are_you_sure(player):
                break
        elif character_class == '3':
            print(ascii_rogue)
            player = Rogue(name)
            if are_you_sure(player):
                break
        character_class = input('Choose your class: 1 - Warrior, 2 - Mage, 3 - Rogue: ')
    from adventure.storys import intro
    adventure(player, [], intro(player))


def are_you_sure(player):
    are_you_sure = input(f'Are you sure you want to be a {player.__class__.__name__}? (Y/N): ')
    if are_you_sure.lower() == 'y':
        return True
    else:
        return False