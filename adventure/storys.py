import random

from classes.enemy_class import *
from classes.world_class import *

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
        world = World()
        story = [
                ['new_line', f"Welcome to the adventure, {player.name}!"],
                ['new_line', "The day begins quietly, a sense of tranquility washes over your heart. You're probably a day's walk from the nearest town."],
                ['new_line', '']

        ]
        story.append(['new_line', ""])
        story.append(['new_line', ""])
        story.append(['new_line', ""])
        story.append(['new_line', ""])



