import os

from classes.hero_class import *
from classes.enemy_class import *

from utils.miscellaneous import *
from utils.ascii_arts import *

player = Warrior('Guts')
enemy  = Goblin('Mokoto Nobunaga, the Goblin!')
player.current_hp = 16

#print(player.get_attack(0, 'right_hand'))


def battle(pc, npc):
    clear_console()
    print(ascii_battle)
    print(f"| {pc.name} VS {npc.name}!")
    # Health Bars
    print(ascii_bar)
    health_bar(pc, 20)
    health_bar(npc, 20)
    # Player Stats
    print(ascii_bar)
    print(f"| Level: {pc.level} | HP: {pc.hp}")
    print(f"| Strength: {pc.strength} | Agility: {pc.agility} | Intelligence: {pc.intelligence} | Luck: {pc.luck}")
    # Actions
    print(ascii_bar)
    print("| Actions:")
    print("| 1. Attack | 2. Use Item | 3. Check Equipament | 4. Run")

def health_bar(character, total_squares):

    current_hp_porcentage = porcentage(character.current_hp, character.hp)

    white_squares = int(rule_of_three(100, total_squares, current_hp_porcentage))
    black_squares = total_squares - white_squares

    print(f"| {character.name} | HP: {character.current_hp}/{character.hp} | {white_squares * '■'}{black_squares * '◻'}")

battle(player, enemy)