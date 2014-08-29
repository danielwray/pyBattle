#!/usr/bin/env python3

__Version__ = '0.0.4'
__status__ = 'Prototype'

'''
pyBattle refactor
The code became to much of a mess - I couldn't take it anymore
'''

from random import randint


class Characters(object):
    """
    Character class
    Contains properties of game characters (character objects)
    - name, health stats, state, levels, items
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


class EnemyCharacter(Characters):
    """
    Character class
        - EnemyCharacter class
    Contains properties of enemy character (character object)
    - name, health stats, levels, items
    """
    def __init__(self, enemy_name, enemy_health, enemy_level, enemy_fighting, enemy_items):
        Characters.__init__(self)
        self.name = enemy_name
        self.min_health = 1
        self.enemy_health = enemy_health
        self.skill_level = enemy_level
        self.skill_fighting = enemy_fighting
        self.item_list = enemy_items

    def enemy_data(self):
        e_data = dict(Name=self.name, Health=self.enemy_health, Level=self.skill_level, Items=self.item_list)
        return dict.items(e_data)


class PlayerCharacter(Characters):
    """
    Character class
        - PlayerCharacter class
    Contains properties of player character (character object)
    - name, health stats, state, levels, items
    """
    def __init__(self, name, state, level, crafting, fighting, trading):
        Characters.__init__(self)
        self.name = name
        self.min_health = 1
        self.cur_health = 50
        self.max_health = 999
        self.state = state
        self.skill_level = level
        self.skill_crafting = crafting
        self.skill_fighting = fighting
        self.skill_trading = trading
        self.item_list = {"Iron Sword": "An old, rusted sword", "Satchel": "Old leather satchel"}

    def player_data(self):
        p_data = dict(Name=self.name, Health=self.cur_health, State=self.state, Level=self.skill_level,
                      Crafting=self.skill_crafting, Fighting=self.skill_fighting, Trading=self.skill_trading,
                      Items=self.item_list)
        return dict.items(p_data)


class Die(object):
    """
    Die
    Contains methods for Die class (Die object)
    - roll_result (get random ints), roll_comparison(get random ints and determine winner)
    """
    def __init__(self):
        self.player_roll = randint(1, 6)
        self.enemy_roll = randint(1, 6)

    def roll_result(self):
        return self.player_roll, self.enemy_roll

    def roll_comparison(self):
        if self.player_roll > self.enemy_roll:
            outcome = "Player wins"
            return outcome
        elif self.player_roll < self.enemy_roll:
            outcome = "Player loses"
            return outcome
        else:
            outcome = "Draw"
            return outcome


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
        print("You are drawn into battle\n")
        if randint(2, 4) > 2:
            new_enemy = (EnemyCharacter("Goblin", 25, 2, 3, {"Sword": "_weapon_", "Shield": "_weapon_", 2: "_coin_"}))
            print("Battle: {0} \n vs \n {1} ".format(player.player_data(), new_enemy.enemy_data()))

    elif state == "rest":
        print("You sit and rest for a moment; the sun beams down and you feel well\n")

    elif state == "craft":
        print("You pull out a hammer and start getting creative\n")

    elif state == "trade":
        print("You put on your haggling hat and start looking for deals\n")

    else:
        print("You sit on a rock, and ponder the mysteries of life\n")


if __name__ == "__main__":
    print("Enter your name")
    player_name = input("~>")
    print("\nLet's get going {0}".format(player_name))
    player = PlayerCharacter(player_name, "state", 1, 1, 2, 1)
    main()