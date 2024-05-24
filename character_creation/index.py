from classes.hero_class import *

def create_character():
    print('Welcome to the character creation!')
    #
    name = input('Enter your name: ')
    while True: 
        confirm_name = input(f'Are you sure you want to name your character {name}? (Y/N): ')
        if confirm_name.lower() == 'y':
            break
        else:
            name = input('Enter your name: ')
    #
    character_class = input('Choose your class: 1 - Warrior, 2 - Mage, 3 - Rogue: ')
    while True:
        if character_class == '1':
            player = Warrior(name)
            break
        elif character_class == '2':
            player = Wizard(name)
            break
        elif character_class == '3':
            player = Rogue(name)
            break
        else:
            character_class = input('Choose your class: 1 - Warrior, 2 - Mage, 3 - Rogue: ')