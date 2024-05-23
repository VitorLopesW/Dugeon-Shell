import os

from classes.hero_class import *
from classes.enemy_class import Goblin
from utils.miscellaneous import clear_console

player = Warrior('Guts')


def battle():
    clear_console()
    print("""
 ___   _ _____ _____ _    ___ 
| _ ) /_\_   _|_   _| |  | __|
| _ \/ _ \| |   | | | |__| _| 
|___/_/ \_\_|   |_| |____|___|
    """)
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