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
    input(f"{colors.cyan}Press any key to continue...{colors.end}")
    if reset == 'clear':
        clear_console()
