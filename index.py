import os

from classes.hero_class import *
from classes.enemy_class import *

# Character Creation
from character_creation.index import *
# Adventure
from adventure.index import *
# Combat 
from combat.index import *
# Utilities
from utils.miscellaneous import *
from utils.ascii_arts import *

player = None

# Dev_Mode
dev_mode = True

def newGame():
    ## DELETE THIS LINE IN THE FINAL VERSION
    if dev_mode:
        clear_console()
        player = Warrior('Vitor')
        adventure(player)
    else:
        ascii_new_game()
        create_character(player)

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
    