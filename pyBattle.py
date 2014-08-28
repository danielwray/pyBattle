#!/usr/bin/env python3

__Version__ = '0.0.3'
__status__ = 'Prototype'

'''
pyBattle refactor
The code became to much of a mess - I couldn't take it anymore
'''

from random import randint


# classes
# NOTE: This should be just character class, and a 'game' class should be made for the game state
class Characters(object):
    """
    Character class
    Contains properties of game characters (character objects)
    - name, health stats, state, levels, items...
    """

    def __init__(self):
        self.name = " "
        self.min_health = 1
        self.cur_health = 1
        self.max_health = 1
        self.state = " "
        self.skill_level = 1
        self.skill_crafting = 1
        self.skill_fighting = 1
        self.skill_trading = 1
        self.item_list = {}


# Note: I'm not even sure if this is how to use a class...
class EnemyCharacter(Characters):
    def __init__(self, enemy_name, enemy_health, enemy_level, enemy_fighting, enemy_items):
        Characters.__init__(self)
        self.name = enemy_name
        self.min_health = 1
        self.enemy_health = enemy_health
        self.skill_level = enemy_level
        self.skill_fighting = enemy_fighting
        self.item_list = enemy_items


    def enemy_data(self):
        return {"Name": self.name}

    @property
    def enemy_name(self):
        self.name = self.name
        return self.name

    @property
    def enemy_cur_health(self):
        self.enemy_health = self.enemy_health
        return self.enemy_health

    @property
    def enemy_f_skill(self):
        self.skill_fighting = self.skill_fighting
        return self.skill_fighting


# NOTE: Nor this. It doesn't seem to make very much sense.
class PlayerCharacter(Characters):
    def __init__(self, name, state, level, crafting, fighting, trading):
        Characters.__init__(self)
        self.name = name
        self.min_health = 1
        self.cur_health = 50
        self.max_health = 200
        self.state = state
        self.skill_level = level
        self.skill_crafting = crafting
        self.skill_fighting = fighting
        self.skill_trading = trading
        self.item_list = {"Iron Sword": "An old, rusted sword", "Satchel": "Old leather satchel"}

    @property
    def player_name(self):
        self.name = self.name
        return self.name

    @property
    def player_min_health(self):
        return "min health working"

    @property
    def player_cur_health(self):
        self.cur_health = self.cur_health
        return self.cur_health

    @property
    def player_max_health(self):
        return "max health working"

    @property
    def player_state(self):
        return "state is working"

    @property
    def player_skill_level(self):
        return "player skill level working"

    @property
    def player_crafting_level(self):
        return "lorem ipsum"

    @property
    def player_fighting_level(self):
        return "lorem ipsum"

    @property
    def player_trading_level(self):
        return "lorem ipsum"

    @property
    def player_item_list(self):
        return "lorem ipsum"


class Dice(object):
    def __init__(self):
        self.player_roll = randint(1, 6)
        self.enemy_roll = randint(1, 6)

    def roll_result(self):
        return self.player_roll, self.enemy_roll

    # NOTE: This looks terrible, a better function should be developed - It should take player skill as a var
    def roll_comparison(self):
        if self.player_roll > self.enemy_roll:
            return "attack"
        elif self.player_roll < self.enemy_roll:
            return "defend"
        else:
            return "draw"


# Note: This seems logical to have a class to call to process text input... But is it?
class PlayerInput:
    @staticmethod
    def input_parser():
        player_input = input("~> ")
        player_output = player_input
        return player_output.lower()


def main():
    game_active = True
    init_game = input("Type 'new game' to start a new game: ")

    if init_game == "new game":
        print("Welcome to pyBattle, an exercise in enlightenment, and a wannabe-programmers journey.\n")
        print("Make a character, battle monsters, capture goodies, craft items.\n")
        print("Enter your name")
        player_name = input("~>")
        player = PlayerCharacter(player_name, "state", 1, 1, 2, 1)
        print("\nLet's get going {0}".format(player.player_name))
        print("type 'menu' to bring up the available activities.\n")
    else:
        print("I've always wanted to be a lumberjack.")
        exit()

    while game_active:
        game_mode = game_state
        command = PlayerInput.input_parser()
        if command == "menu":
            print("Select a game mode: rest, fight, craft, trade.\n")
            game_mode(PlayerInput.input_parser())
        elif command == "help?":
            print(" insert game help here - read from file...")
        elif command == "quit":
            print("Goodbye")
            return False
        else:
            print("For a list of commands type 'help?'")


def game_state(state):
    if state == " ":
        print("...\n")

    elif state == "fight":
        fight_active = True
        print("You are drawn into battle\n")
        if randint(2, 4) > 2:
            create_enemy = EnemyCharacter("Goblin", 25, 2, 3, {"Sword": "weapon", "shield": "weapon", 2: "Coins"})
            print(create_enemy.enemy_data())

    elif state == "rest":
        rest_active = True
        print("You sit and rest for a moment; the sun beams down and you feel well\n")

    elif state == "craft":
        craft_active = True
        print("You pull out a hammer and start getting creative\n")

    elif state == "trade":
        trade_active = True
        print("You put on your haggling hat and start looking for deals\n")

    else:
        print("You sit on a rock, and ponder the mysteries of life\n")



if __name__ == "__main__":
    main()