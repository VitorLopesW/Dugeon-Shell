
from classes.enemy_class import *

#
# When i want to create a function who is only used to be a bifurcation of a another story,
# I must use previous story function name as a prefix, add the new function name as a suffix.
# Example: intro > intro_help_girl
#
# New Line: ['new_line', 'string']
# Random Event: ['random_event', [list of events]]
# Input: ['input', 'string', [list of options], [list of paths]]
# Battle: ['battle', npc]

def intro(player):
    introdutory_storys = [
            ['new_line', f"Welcome to the adventure, {player.name}!"],
            ['new_line', f"It all begins on a calm morning, where only the cutting sound of the wind spreads through your ears."],
            ['new_line', f"A feeling of freedom washes over you as you realize it's your first day as an adventurer. "],
            ['new_line', f'Your gear is all packed, and you have a {player.equiped_weapons_name()} with you.'],
            ['new_line', f"It's not the best weapon in the world, but it's the one you inherited from your family."],
            ['new_line', f"After leaving the fields behind, selling your land, and venturing into the unknown, everything seems better."],
            ['new_line', f"Your life will never be the same again. You have {player.gold} left in your pockets, if needed."],
            ['new_line', f"After a few hours of traveling, you hear..."],
            [
                'random_event',
                [
                    [
                        ['new_line', 'A loud noise coming from the bushes.'],
                        ['new_function', intro_help_girl(player)]
                    ],
                    [
                        ['new_line', 'A scream in the distance.'],
                        ['new_function', intro_help_girl(player)]
                    ],
                ]
            ]
    ]
    
    return introdutory_storys

def intro_help_girl(player):
    help_girl = [
        ['new_line', "As you get closer, you can also hear a girl's voice screaming for help."],
        ['new_line', "-Help! This vile goblin is grabbing me!"],
        [
            'input', 
            'Shoud you help the girl? (Y/N)',
            ['y', 'n'],
            [
                [
                    ['new_line', "It's time to show courage and help this girl."],
                    ['new_function', story_battle(player)]
                ],
                [
                    ['new_line', "Maybe it's not the right time, and you might not be strong enough."],
                    ['new_function', morning_of_ashes(player)],
                ]
            ]
        ]
    ]
    return help_girl

def morning_of_ashes(player):
    morning_of_ashes = [
        ['new_line', "you're a chicken"]
    ]
    return morning_of_ashes

def story_battle(player):
    battle = [
        ['battle', Goblin('Goblin das Montanhas')]
    ]
    return battle