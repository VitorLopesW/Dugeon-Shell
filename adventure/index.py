import os
import random
import copy

from utils.ascii_arts import *
from utils.miscellaneous import *
from adventure.storys  import *

def adventure(player, story_unfolded, choosen_story):
    pause_choosen_story = copy.deepcopy(choosen_story)
    for list in choosen_story:
        if list[0] == 'new_line':
            print_story(story_unfolded)
            new_line(story_unfolded, list[1])
            pause_choosen_story.pop(0)
            continue_game_with_menu('clear', player, story_unfolded, pause_choosen_story)
        elif list[0] == 'random_event':
            # param 
            # list[1] = list : events
            list_of_events = list[1]
            random_number = random.randint(0, len(list_of_events) - 1)
            random_number = 0
            random_event = list_of_events[random_number]
            choosen_story = random_event
            return adventure(player, story_unfolded, choosen_story)
        elif list[0] == 'input':
            # param 
            # list[1] = str : question
            # list[2] = list : options
            # list[3] = list : paths
            while True:
                print_story(story_unfolded)
                while True:
                    player_input = input(f"\033[93m{list[1]}\033[0m")
                    options_list = list[2]
                    paths_list = list[3]
                    if player_input.lower() in options_list:
                        input_index = options_list.index(player_input)
                        choosen_story = paths_list[input_index]
                        clear_console()
                        return adventure(player, story_unfolded, choosen_story)
                    else:
                        clear_console()
                        print_story(story_unfolded)
                        print(f"\033[91mInvalid option\033[0m")
        elif list[0] == 'battle':
            from combat.index import battle
            # param 
            # list[1] = npc : npc
            # list[2] = function : new story path
            npc = list[1]
            new_story_path = list[2]
            return battle(player, npc,[story_unfolded, new_story_path])
        elif list[0] == 'new_function':
            new_story_path = list[1]
            return adventure(player, story_unfolded, new_story_path)

                




def print_story(list):
    for line in list:
        print(line)

def new_line(list, line):
    line = "| " + line
    list.append(line)
    print(line)