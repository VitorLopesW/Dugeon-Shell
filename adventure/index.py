import os
import random

from utils.miscellaneous import *
from adventure.storys  import *


def adventure(player, story_unfolded = [], choosen_story = None):
    if choosen_story == None:
        choosen_story = intro(player)[0]

    for list in choosen_story:
        if list[0] == 'new_line':
            print_story(story_unfolded)
            new_line(story_unfolded, list[1])
            continue_game('clear')
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
                player_input = input(list[1])
                options_list = list[2]
                paths_list = list[3]
                if player_input in options_list:
                    input_index = options_list.index(player_input)
                    choosen_story = paths_list[input_index]
                    return adventure(player, story_unfolded, choosen_story)
        elif list[0] == 'new_function':
            new_story_path = list[1]
            print(list[1])
            input('stop')
            return adventure(player, story_unfolded, new_story_path)

                




def print_story(list):
    for line in list:
        print(line)

def new_line(list, line):
    line = "| " + line
    list.append(line)
    print(line)