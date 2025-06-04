from classes.hero_class import Berserker
from adventure.index import adventure
from adventure.storys import intro, hunger_story
from utils.miscellaneous import clear_console


def main():
    clear_console()
    # Dev start with Berserker
    player = Berserker('Hero')
    adventure(player, [], intro(player))
    while player.current_hp > 0:
        adventure(player, [], hunger_story(player))
        player.hunger_turn()


if __name__ == '__main__':
    main()

