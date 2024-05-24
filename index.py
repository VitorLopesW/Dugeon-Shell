import os

from classes.hero_class import *
from classes.enemy_class import *

# Character Creation
from character_creation.index import *
# Combat 
from combat.index import *
# Utilities
from utils.miscellaneous import *
from utils.ascii_arts import *

player = Warrior('Hanzo')
enemy  = Goblin('Nobunaga, the Goblin')


def newGame():
    ascii_new_game()
    create_character()

def ascii_new_game():
    clear_console()
    print('Maximize your terminal window for the best experience.')
    input("Press any key to start a new game!")
    clear_console()
    print(ascii_logo)
    continue_game('clear')
    print(ascii_logo)
    print(ascii_game_made_by)
    continue_game('clear')









newGame()
    