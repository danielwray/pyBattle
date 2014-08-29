#!/usr/bin/env python3

__Version__ = '0.0.5'
__status__ = 'Prototype'

'''
pyBattle refactor
The code became to much of a mess - I couldn't take it anymore
'''

from random import randint
from random import choice
import time


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

    name = ""
    min_health = 1
    enemy_health = 20
    skill_level = 1
    skill_fighting = 1
    item_list = {}

    def __init__(self, name):
        Characters.__init__(self)
        self.name = name

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
    name = ""
    state = ""
    min_health = 1
    cur_health = 50
    max_health = 999
    level = 1
    crafting = 1
    fighting = 1
    trading = 1
    item_list = {"Iron Sword": "An old, rusted sword", "Satchel": "Old leather satchel"}

    def __init__(self, name):
        Characters.__init__(self)
        self.name = name

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
        return "{0} rolled: {1} | Enemy rolled: {2}".format(player.name, self.player_roll, self.enemy_roll)

    def roll_comparison(self):
        self.player_roll = randint(1, 6)
        self.enemy_roll = randint(1, 6)
        if self.player_roll > self.enemy_roll:
            outcome = 0
            return outcome
        elif self.player_roll < self.enemy_roll:
            outcome = 1
            return outcome
        elif self.player_roll == self.enemy_roll:
            outcome = 2
            return outcome
        else:
            return "Error rolling die!"


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
        print("You are drawn into battle!\n")
        battle_active = True
        e_dat = enemy_data()
        new_enemy = EnemyCharacter(e_dat)
        roll = Die()
        delay = time
        d_counter = 0
        p_counter = 0
        e_counter = 0

        print("Battle: \n{0} \nvs \na {1}\n".format(player.name, new_enemy.name))

        while battle_active:
            roll_data = roll.roll_comparison()
            if p_counter == 3:
                delay.sleep(1)
                print("\n{0} wins the battle.\n".format(player.name))
                return False
            elif e_counter == 3:
                delay.sleep(1)
                print("\nThe {0} wins the battle.\n".format(new_enemy.name))
                return False
            elif d_counter == 3:
                delay.sleep(1)
                print("Draw!")
                return False
            else:
                if roll_data == 0:
                    delay.sleep(1)
                    print(roll.roll_result())
                    print("Attacking\n")
                    new_enemy.cur_health -= player.skill_fighting
                    print(new_enemy.cur_health)
                    p_counter += 1
                    pass
                elif roll_data == 1:
                    delay.sleep(1)
                    print(roll.roll_result())
                    print("Defending\n")
                    player.cur_health -= new_enemy.skill_fighting
                    print(player.cur_health)
                    e_counter += 1
                    pass
                else:
                    delay.sleep(1)
                    print(roll.roll_result())
                    print("Draw!\n")
                    d_counter += 1
                    pass

    elif state == "rest":
        print("You sit and rest for a moment; the sun beams down and you feel well\n")
        print("Your current health level is {0}".format(player.cur_health))
        cheat = input("Type 'gimme' to increase health by 10 points: ")
        if cheat == "gimme":
            player.cur_health += 10
        else:
            print("Uh oh!")

    elif state == "craft":
        print("You pull out a hammer and start getting creative\n")
        print("Your current crafting level is {0}".format(player.crafting))

    elif state == "trade":
        print("You put on your haggling hat and start looking for deals\n")
        print("Your current trading level is {0}".format(player.trading))

    else:
        print("You sit on a rock, and ponder the mysteries of life\n")


# make this into a class so I can call the separate data returns to enter into enemy instances.
def enemy_data():
    enemy_name_data = ["small goblin", "angry goblin", "warrior goblin", "berserk goblin", "king goblin",
                       "mediocre orc", "slightly less mediocre, and more smelly orc", "orc leader", "thief",
                       "escaped prisoner", "outlaw", "deserting soldier", "trained man-at-arms", "landed knight",
                       "knight", "turnip"]
    enemy_name_rand = choice(list(enemy_name_data))
    enemy_health_data = randint(10, 200)
    enemy_skill_data = randint(1, 10)
    enemy_fighting_data = randint(1, 25)
    enemy_item_data = {"example 1": "weapon", "example 2": "coin", "example 3": "clothing"}
    enemy_item_rand = choice(list(enemy_item_data))

    return "".join(enemy_name_rand)


if __name__ == "__main__":
    print("Enter your name")
    player_name = input("~>")
    print("\nLet's get going {0}".format(player_name))
    player = PlayerCharacter(player_name)
    main()