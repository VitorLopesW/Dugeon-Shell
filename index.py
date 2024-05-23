import os

from classes.hero_class import *
from classes.enemy_class import Goblin

from utils.miscellaneous import clear_console
from utils.ascii_arts import *

player = Warrior('Guts')


def battle():
    clear_console()
    print(ascii_battle)
    print(f"{player.name} VS Goblin")
    # Health Bars
    print(f"{player.name}: {'█' * player.hp}")
    print(f"Goblin: {'█' * 10}")    
    print("------")
    # Player Stats
    print(f"| Level: {player.level} | HP: {player.hp}")
    print(f"| Strength: {player.strength} | Agility: {player.agility} | Intelligence: {player.intelligence} | Luck: {player.luck}")
    # Actions
    print("------")
    print("| Actions:")
    print("| 1. Attack | 2. Use Item | 3. Check Equipament | 4. Run")

battle()