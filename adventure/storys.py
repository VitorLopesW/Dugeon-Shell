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
        story = []
        story.append(['new_line', f"Welcome to the world of " + world.name + "!"])
        story.append(['new_line', f"You are a {player.player_class}"])
        # Class check
        if player.player_class == 'Wizard':
                story.append(['new_line', f"As a wizard, you have the ability to cast spells."])
        elif player.player_class == 'Warrior':
                story.append(['new_line', f"As a warrior, you have the ability to use weapons."])
        elif player.player_class == 'Rogue':
                story.append(['new_line', f"As a rogue, you have the ability to sneak and use daggers."])
        story.append(['new_line', f"You grab your {player.equiped_weapons_name()} and head out into the world."])
        story.append(['new_line', f""])
        # Random Weather
        world.random_weather()
        story.append(['new_line', f"{world.weather_world_building()}, "])
        story.append(['new_line', f""])
        story.append(['new_line', f""])



