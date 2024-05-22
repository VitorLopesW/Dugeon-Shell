from hero_class import Warrior, Wizard, Rogue
from enemy import Goblin
from miscellaneous import clear_console

player = Warrior('Guts')


def battle():
    clear_console()
    print("""
 ___   _ _____ _____ _    ___ 
| _ ) /_\_   _|_   _| |  | __|
| _ \/ _ \| |   | | | |__| _| 
|___/_/ \_\_|   |_| |____|___|
    """)
    print(f"{player.name} VS Goblin")
    print("___")
    print(
f"""| Level: {player.level} |HP: {player.hp}
| Strength: {player.strength} | Agility: {player.agility} | Intelligence: {player.intelligence} | Luck: {player.luck}
| Weapon: {player.weapon}
"""
    )
    print("___")

battle()