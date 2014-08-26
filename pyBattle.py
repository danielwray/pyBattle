#!/usr/bin/env python3

__Version__ = '0.0.3'
__status__ = 'Prototype'

'''
pyBattle refactor
The code became to much of a mess - I couldn't take it anymore
'''

from random import randint


# classes
class Characters(object):
    """
    Character class
    Contains properties of game characters (character objects)
    - name, health stats, state, levels, items...
    contains character related functions
    - character_health, states (normal, fighting, crafting et al), character creation...
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

    def game_state(self, new_state):
        self.state = new_state
        if self.state == " ":
            print("...\n")

        elif self.state == "fight":
            fight_active = True
            battling = True
            p_character = PlayerCharacter()
            e_character = EnemyCharacter("Goblin", randint(10, 100), randint(1, 3), randint(1, 3),
                                         {"Sword": "A badly forged goblin sword, made from old iron."})

            enemy_stats = e_character.new_enemy()
            print("You stumble upon an fierce {0}\n".format(e_character.name))
            for i in sorted(enemy_stats):
                print(i, enemy_stats[i])

            print(p_character.name, p_character.cur_health)

            player_health = p_character.cur_health
            enemy_health = e_character.cur_health
            enemy_min_health = e_character.min_health

            while fight_active:
                dice_roll = Dice()
                print("Do you wish to fight, or try to run? ")
                command = PlayerInput.input_parser()
                if command == "fight":
                    print("You secure your armour, draw your weapon, and give pray to the gods...")
                    while battling:
                        if dice_roll.roll_comparison() == "attack":
                            print("Attacking\n")
                            enemy_health -= p_character.skill_fighting * randint(1, 6)
                            print("The enemy has {0} health remaining".format(enemy_health))
                            if enemy_health <= enemy_min_health:
                                print("You win\n")
                                return False
                            else:
                                break
                        elif dice_roll.roll_comparison() == "defend":
                            print("Enemy Attacking\n")
                            player_health -= e_character.skill_fighting * randint(1, 6)
                            print("You have {0} health remaining".format(enemy_health))
                            if player_health <= 1:
                                print("You lost\n")
                                return False
                            else:
                                break
                        elif dice_roll.roll_comparison() == "draw":
                            print("You both miss")
                            break
                elif command == "run":
                    print("You realise you cannot win and try to run...")
                    return False
                else:
                    print("You stand still, awestruck by your opponent...")

        elif self.state == "rest":
            rest_active = True
            print("You sit and rest for a moment; the sun beams down and you feel well\n")

        elif self.state == "craft":
            craft_active = True
            print("You pull out a hammer and start getting creative\n")

        elif self.state == "trade":
            trade_active = True
            print("You put on your haggling hat and start looking for deals\n")

        else:
            print("You sit on a rock, and ponder the mysteries of life\n")


class EnemyCharacter(object):
    def __init__(self, name, cur_health, skill_level, skill_fighting, items):
        Characters.__init__(self)
        self.name = name
        self.min_health = 1
        self.cur_health = cur_health
        self.skill_level = skill_level
        self.skill_fighting = skill_fighting
        self.item_list = items

    def new_enemy(self):
        self.name = self.name
        self.cur_health = self.cur_health
        self.skill_level = self.skill_level
        self.skill_fighting = self.skill_fighting
        self.item_list = self.item_list
        new_enemy = {"Name: ": self.name, "Health: ": self.cur_health, "Skill level: ": self.skill_level,
                     "Fight level: ": self.skill_fighting, "Items held: ": self.item_list}
        e_data_keys = new_enemy.keys()
        e_data_vals = new_enemy.values()
        return new_enemy


class PlayerCharacter(object):
    def __init__(self):
        Characters.__init__(self)
        #if name is None:
        #    self.name = self.name
        #else:
        #    self.name = input("Your name? ")
        self.name = " "
        self.min_health = 1
        self.cur_health = 100
        self.max_health = 200
        self.state = "normal"
        self.skill_level = 1
        self.skill_crafting = 1
        self.skill_fighting = 1
        self.skill_trading = 1
        self.item_list = {}

    def new_player(self):
        self.name = self.name
        self.cur_health = self.cur_health
        self.state = self.state
        self.skill_level = self.skill_level
        self.skill_crafting = self.skill_crafting
        self.skill_fighting = self.skill_fighting
        self.skill_trading = self.skill_trading
        self.item_list = self.item_list
        new_player = {"Name: ": self.name, "Health: ": self.cur_health, "Level: ": self.skill_level,
                      "items: ": self.item_list}
        p_data_keys = new_player.keys()
        p_data_values = new_player.values()
        return new_player


class Dice(object):
    def __init__(self):
        Characters.__init__(self)
        self.player_roll = randint(1, 6)
        self.enemy_roll = randint(1, 6)

    def roll_result(self):
        return self.player_roll, self.enemy_roll

    def roll_comparison(self):
        if self.player_roll > self.enemy_roll:
            return "attack"
        elif self.player_roll < self.enemy_roll:
            return "defend"
        else:
            return "draw"


class PlayerInput:
    @staticmethod
    def input_parser():
        player_input = input("~> ")
        player_output = player_input
        return player_output.lower()


def main():
    game_active = True
    char_obj = Characters()
    init_game = input("Type 'new game' to start a new game: ")

    if init_game == "new game":
        print("Welcome to pyBattle, an exercise in enlightenment, and a wannabe-programmers journey.\n")
        print("Make a character, battle monsters, capture goodies, craft items.\n")

    else:
        print("I've always wanted to be a lumberjack.")
        exit()

    while game_active:
        command = PlayerInput.input_parser()
        if command == "menu":
            print("Select a game mode: rest, fight, craft, trade.\n")
            char_obj.game_state(PlayerInput.input_parser())
        elif command == "help?":
            print(" insert game help here - read from file...")
        elif command == "quit":
            print("Goodbye")
            return False
        else:
            print("For a list of commands type 'help?'")


if __name__ == "__main__":
    main()