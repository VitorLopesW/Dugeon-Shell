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
        if player_input == '1':
            break
        elif player_input == '2':
            inventory = pc.inventory

            os.system('cls')
            print('inventory: ')
            for item in inventory:
                print(f' {item.name} - {item.description}')
            while True:
                string_input = f'{colors.cyan}Type The name of the item to use it: or type [B] to go back: ${colors.end}'
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

        elif player_input == '3':
            break
        elif player_input == '4':
            break
        else:
            break
        #from utils.miscellaneous import continue_game
        #continue_game('clear')