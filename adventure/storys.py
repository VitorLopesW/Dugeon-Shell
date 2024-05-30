import random

from classes.enemy_class import *
from classes.world_class import *
from classes.event_class import *

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
        npcs = {}
        story.append(['new_line', f"Welcome to the world of " + world.name + "!"])
        story.append(['new_line', f"You are a {player.player_class}"])
        # Class based story
        if player.player_class == 'Wizard':
                story.append(['new_line', f"young and inexperienced wizard."])
        elif player.player_class == 'Warrior':
                story.append(['new_line', f"You are a novice warrior, with a old sword."])
        elif player.player_class == 'Rogue':
                story.append(['new_line', f"As a rogue, you are kicked out of your city, because of your crimes."])
                story.append(['new_line', f"But this is a new day, and you are ready to start a new life."])
        #
        story.append(['new_line', f"You grab your {player.equiped_weapons_name()} and head out into the world."])
        story.append(['new_line', f"You have {player.gold} gold, in your pocket."])

        # Random
        # Random Weather
        world.random_weather()

        # random npc 
        npcs['lonely_child'] = Children('female')
        # random location
        possible_locations = ['inside a bush', 'in a tree', 'behind a rock', 'in a hole']
        child_location = random.choice(possible_locations)
        ###
        story.append(['new_line', f"{world.weather_world_building()}, And you hear a noise, {child_location}, what could it be?"])
        story.append(
                [
                'input', 
                f"Would you like to investigate? (Y/N)", 
                ['y', 'n'], 
                [intro_help_girl(player, npcs, world), intro_end(player, npcs, world)]
                ])
        #
        story.append(['new_line', f"You have {player.gold} gold, in your pocket."])

        return story

def intro_help_girl(player, npcs, world):
        # random enemy
        enemy = get_random_enemy(player)
        story = [
                ['new_line', f"You walk over to the noise, and see girl, crying. She looks up at you, with tears in her eyes."],
                ['new_line', f"She is wearing a {npcs['lonely_child'].clothes_color} dress. She looks scared and pale. She is holding a small doll."],
        ]
        if enemy.intelligence > 0:
                story.append(['new_line', f"She says: 'Please help me, a {enemy.name} is using me as bait!'"])
        else:
                story.append(['new_line', f"She says: 'Please help me, a {enemy.name} is chasing me!'"]) 
        story.append(['battle', enemy, intro_girl_saved])
        
        return story 

def intro_girl_saved(player, npcs, world):
        story = [
                ['new_line', f"You have save this girl"],
        ]
        return story
def intro_end(player, npcs, world):
        return [['new_line', f"You decide to ignore the noise and continue on your journey."]]