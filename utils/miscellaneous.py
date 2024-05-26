import os

from utils.ascii_arts import colors

def rule_of_three(a, b, c):
    result = (b * c) / a
    return result

def porcentage(a, b):
    result = (a / b) * 100
    return result
    
def clear_console():
    os.system('cls')

def continue_game(reset = False):
    continue_text = f"{colors.cyan}Press enter key to continue...{colors.end}"
    input(continue_text) 
    if reset == 'clear':
        clear_console()

def continue_game_with_menu(reset = False, pc = None):
    continue_text = f"{colors.cyan}Press enter key to continue... or press [M] to open menu.{colors.end}"
    player_input = input(continue_text) 
    if player_input.lower() == 'm':
        from adventure.game_menu import game_menu
        game_menu(pc)
        return continue_game('clear')

def invalide_option():
    print(f"{colors.red}Invalid Option{colors.end}")