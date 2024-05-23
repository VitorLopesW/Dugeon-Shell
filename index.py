import os

from classes.hero_class import *
from classes.enemy_class import *

from utils.miscellaneous import *
from utils.ascii_arts import *

player = Warrior('Guts')
enemy  = Goblin('Nobunaga, the Goblin!')
player.current_hp = 16

#print(player.get_attack(0, 'right_hand'))


def battle(pc, npc, turn = 1, actions_position = 'menu'):
    clear_console()
    print(ascii_battle)
    print(f"| {colors.blue}{pc.name} VS {npc.name}!{colors.end}")
    # Health Bars
    print(ascii_bar)
    health_bar(pc, 20)
    health_bar(npc, 20)
    # Player Stats
    print(ascii_bar)
    player_stats(pc)
    # Turns 
    print(ascii_bar)
    print(f"| {colors.yellow}Turn: {turn}{colors.end}")
    # Actions
    print(ascii_bar)
    battle_actions(pc, npc, turn, actions_position)

def health_bar(character, total_squares):
    current_hp_porcentage = porcentage(character.current_hp, character.hp)

    white_squares = int(rule_of_three(100, total_squares, current_hp_porcentage))
    black_squares = total_squares - white_squares

    print(f"| {colors.blue}{character.name}{colors.end} | HP: {character.current_hp}/{character.hp} | {colors.red} {white_squares * '■'}{black_squares * '◻'} {colors.end}")

def player_stats(character):
    line_one = '| Player Stats:'
    line_two = ''
    print(line_one)
    stats_print_list = [
        [colors.blue, f"Level: {character.level}"],
        [colors.green, "Strength: " + str(character.strength)],
        [colors.yellow, "Agility: " + str(character.agility)],
        [colors.cyan, "Intelligence: " + str(character.intelligence)],
    ]
    for component in stats_print_list:
        line_two += f"| {component[0]}{component[1]}{colors.end} "
    print(line_two)

def battle_actions(pc, npc, turn, position):
    if position == 'menu':
        print("| Actions:")
        menu = ''
        menu_list = [
            [colors.blue, f"1- Attack"],
            [colors.green, "2 - Inventory"],
            [colors.yellow, "3 - Magic"],
            [colors.cyan, "4 - Run"],
        ]
        for component in menu_list:
            menu += f"| {component[0]}{component[1]}{colors.end} "
        print(menu)
        while True:
            input_action = input("| Choose an action: ")
            if input_action == '1':
                battle(pc, npc, turn, 'weapon_select')
                break
            elif input_action == '2':
                break
            elif input_action == '3':
                break
            elif input_action == '4':
                break
            else :
                print(f"{colors.red}| Invalid option! Try again{colors.end}")
    if position == 'weapon_select':
        colors_loop = [colors.blue, colors.green, colors.yellow, colors.cyan, colors.red, colors.magenta]
        print("| Choose an weapon:")
        attack_list = ''
        left_hand = pc.check_equipment('left_hand')
        right_hand = pc.check_equipment('right_hand')
        number_of_weapons_equiped = 0
        if left_hand != 'empty':
            number_of_weapons_equiped += 1
            attack_list += f"| {colors_loop[0]}{number_of_weapons_equiped}- {left_hand.name}{colors.end} "
        if right_hand != 'empty':
            number_of_weapons_equiped += 1
            attack_list += f"| {colors_loop[1]}{number_of_weapons_equiped}- {right_hand.name}{colors.end} "
        print(attack_list)







battle(player, enemy)
