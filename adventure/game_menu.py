import os
from utils.ascii_arts import *

def game_menu(pc):
    while True:
        os.system('cls')
        print(ascii_menu)
        print(f'{colors.red}1 - Continue.{colors.end}')
        print(f'{colors.green}2 - inventory{colors.end}')
        print(f'{colors.yellow}3 - Equipaments{colors.end}')
        print(f'{colors.blue}4 - Quit{colors.end}')
        player_input = input('Choose an option: ')
        os.system('cls')
        if player_input == '1':
            break
        elif player_input == '2':
            inventory(pc)
        elif player_input == '3':
            equipamens_menu(pc)

def inventory(pc):
    inventory = pc.inventory
    print('inventory: ')
    for item in inventory:
        print(f' {item.name} - {item.description}')
    while True:
        string_input = f'{colors.cyan}Type The name of the item to use it: or type [B] to go back: {colors.end}'
        player_input = input(string_input)
        if player_input.lower() == 'b':
            break
        # find the first item that has the same name as the player input
        for item in inventory:
            if item.name.lower() == player_input.lower():
                item.use(pc)
                break
            else:
                print(f'{colors.red}Invalid item name, type again.{colors.end}')
    game_menu(pc)

def equipamens_menu(pc):
    print('Equipaments:')
    body_parts_list = ['Left Hand', 'Right Hand', 'Head', 'Body']
    body_parts_list_lower = [body_part.lower() for body_part in body_parts_list]
    for body_part in body_parts_list:
        list_finder = body_part.lower().replace(' ', '_')
        str_to_print = f'{body_part}: '
        if pc.equipment[list_finder] == None:
            str_to_print += f'Empty'
        else:
            str_to_print += f'{colors.blue}{pc.equipment[list_finder].name}{colors.end} - '
            str_to_print += f'{colors.green}{pc.equipment[list_finder].description}{colors.end}'
        print(str_to_print)
        print(ascii_bar)
    while True:
        player_input = input(f'{colors.cyan}Type the [Body Part] of the item to unequip it or type [B] to go back{colors.end}')
        if player_input.lower() == 'b':
            break
        if player_input.lower() in body_parts_list_lower :
            body_part = player_input.lower().replace(' ', '_')
            if pc.equipment[body_part] != None:
                pc.unequip(body_part, 'inventory')
                print(f'{colors.green}Item unequiped{colors.end}')
                from utils.miscellaneous import continue_game
                continue_game('clear')
                return equipamens_menu(pc)
            else:
                print(f'{colors.red}No item to unequip{colors.end}')


        #from utils.miscellaneous import continue_game
        #continue_game('clear')