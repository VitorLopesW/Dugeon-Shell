
from utils.miscellaneous import *
from utils.ascii_arts import *

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
        attack_list = ''
        left_hand = pc.check_equipment('left_hand')
        right_hand = pc.check_equipment('right_hand')
        number_of_weapons_equiped = 0
        if left_hand != 'empty':
            number_of_weapons_equiped += 1
            attack_list += f"| {colors.blue}{number_of_weapons_equiped}- {left_hand.name}{colors.end} "
        if right_hand != 'empty':
            number_of_weapons_equiped += 1
            attack_list += f"| {colors.green}{number_of_weapons_equiped}- {right_hand.name}{colors.end} "
        return_to_menu_number = number_of_weapons_equiped + 1
        attack_list += f"| {colors.red}{return_to_menu_number}- Back{colors.end}"
        print(attack_list)
        while True:
            left_hand_only = number_of_weapons_equiped == 1 and left_hand != 'empty'
            right_hand_only = number_of_weapons_equiped == 1 and right_hand != 'empty'
            both_hands = number_of_weapons_equiped == 2
            while True:
                input_weapon = input('| Choose a weapon: ')
                if left_hand_only:
                    if input_weapon == '1':
                        attack_select(pc, npc, turn, pc.check_equipment('left_hand'), colors.blue)
                        break
                    else:
                        battle(pc, npc, turn, 'menu')
                        break
                elif right_hand_only:
                    if input_weapon == '1':
                        attack_select(pc, npc, turn, pc.check_equipment('right_hand'), colors.green)
                        break
                    else:
                        battle(pc, npc, turn, 'menu')
                        break
                elif both_hands:
                    if input_weapon == '1':
                        attack_select(pc, npc, turn, pc.check_equipment('left_hand'), colors.blue)
                        break
                    elif input_weapon == '2':
                        attack_select(pc, npc, turn, pc.check_equipment('right_hand'), colors.green)
                        break
                    else:
                        battle(pc, npc, turn, 'menu')
                        break

def attack_select(pc, npc, turn, weapon, txt_color):
    colors_loop = [colors.blue, colors.green, colors.yellow, colors.cyan, colors.red, colors.magenta]
    print("| Attacks:")
    attack_list = ''
    position_number = 1
    for i in range(len(weapon.attacks)):
        attack_list += f"| {txt_color}{position_number}- {weapon.attacks[i].name}{colors.end} "
        position_number += 1
    attack_list += f"| {colors.red}{position_number}- Back{colors.end}"
    print(attack_list)
    while True:
        input_attack = input('| Choose an attack: ')
        list_attack_length = len(weapon.attacks)
        if int(input_attack) <= list_attack_length:
            attack_logic(pc, npc, turn, weapon, weapon.attacks[int(input_attack) - 1])
            break
        elif int(input_attack) == list_attack_length + 1:
            battle(pc, npc, turn, 'weapon_select')

def attack_logic(pc, npc, turn, weapon, attack):
    # Player Attack
    # tuple : attack stats 
        # int : damage
        # bool : critical hit notificator
        # float : velocity
        # str : special effect
    attack_stats = pc.get_attack(weapon, attack)
    attack_damage, attack_critical, attack_velocity, attack_special = attack_stats
    # Enemy Attack  
        # tuple : attack stats
        # str: attack description
        # float : velocity
        # str : special effect
    enemy_attack = npc.get_attack()
    enemy_attack_description, enemy_attack_damage, enemy_attack_velocity, enemy_attack_special = enemy_attack
    #
    pc_description = f"| {colors.blue}{attack.pre_description}{attack.description} and cause {attack_damage} damage to {npc.name}{colors.end}!"
    npc_description = f"| {colors.red}{enemy_attack_description} and cause {enemy_attack_damage} damage to you{colors.end}!"
    
    def pc_attack():
        print(pc_description)
        npc.modify_hp(-attack_damage)
        if npc.current_hp <= 0:
            print(ascii_bar)
            print(f"| {colors.green}{npc.name} has been defeated!{colors.end}")
    def npc_attack():
        print(npc_description)
        pc.modify_hp(-enemy_attack_damage)
    if(attack_velocity > enemy_attack_velocity):
        pc_attack()
        if npc.current_hp > 0:
            print(ascii_bar)
            npc_attack()
    else:
        npc_attack()
        if pc.current_hp > 0:
            print(ascii_bar)
            pc_attack()
    #
    pc_is_dead = pc.current_hp <= 0
    npc_is_dead = npc.current_hp <= 0
    if(npc_is_dead):
        end_of_battle(pc, npc)
    elif(pc_is_dead):
        print(ascii_bar)
        print(f"| {colors.red}{pc.name} has been defeated!{colors.end}")
        print(f'| {colors.red}Your story comes to an end.{colors.end}')
        print(f"| {colors.red}GAME OVER!{colors.end}") 
    else:
        continue_game = input('| Type any key to continue: ')
        print(ascii_bar)
        battle(pc, npc, turn + 1, 'menu')

def end_of_battle(pc, npc):
    print(ascii_bar)
    print(f'| {colors.green}After a fierce battle, you have defeated your enemy!{colors.end}')
    xp, gold = npc.get_defeat()
    print(f"| {colors.green}You gain {xp} xp and {gold} gold!{colors.end}")
    pc.add_xp(xp)
    pc.add_gold(gold)

