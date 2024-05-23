import os

from classes.hero_class import *
from classes.enemy_class import *

from utils.miscellaneous import clear_console
from utils.ascii_arts import *

player = Warrior('Guts')
enemy  = Goblin('Mokoto Nobunaga, the Goblin!')


#print(player.get_attack(0, 'right_hand'))


def battle(pc, npc):
    clear_console()
    print(ascii_battle)
    print(f"{pc.name} VS {npc.name}!")
    # Health Bars
    health_bar(pc)
    # Player Stats
    print(f"| Level: {pc.level} | HP: {pc.hp}")
    print(f"| Strength: {pc.strength} | Agility: {pc.agility} | Intelligence: {pc.intelligence} | Luck: {pc.luck}")
    # Actions
    print("------")
    print("| Actions:")
    print("| 1. Attack | 2. Use Item | 3. Check Equipament | 4. Run")

def health_bar(character):
    print(f"{character.name} | HP: {character.current_hp}/{character.hp}")
    print(f"{10 * '■'}")

battle(player, enemy)