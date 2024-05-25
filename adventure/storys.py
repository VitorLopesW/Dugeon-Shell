
from classes.enemy_class import *

#
# When i want to create a function who is only used to be a bifurcation of a another story,
# I must use previous story function name as a prefix, add the new function name as a suffix.
# Example: intro > intro_help_girl
#
# New Line: ['new_line', 'string']
# Random Event: ['random_event', [list of events]]
# Input: ['input', 'string', [list of options], [list of paths]]
# Battle: ['battle', npc, function_name]
# New Function: ['new_function', function_name]

def intro(player):
    introdutory_storys = [
            ['new_line', f"Welcome to the adventure, {player.name}!"],
            ['battle', Goblin('Goblin Green'), intro_part_2(player)],
    ]
    return introdutory_storys
    
def intro_part_2(player):
    introdutory_storys = [
            ['new_line', f"{player.name}, You defeated the goblin!"],
            ['new_line', f"{player.name}, You defeated the goblin!"],
            ['new_line', f"{player.name}, You defeated the goblin!"],

    ]
    return introdutory_storys

