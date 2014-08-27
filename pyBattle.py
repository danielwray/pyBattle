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
            e_character = EnemyCharacter()

            print("You stumble upon a fierce {0}\n".format(e_character.name))

            p_health = p_character.player_health
            p_min_health = p_character.min_health
            e_health = e_character.enemy_health
            e_min_health = e_character.min_health

            while fight_active:
                dice_roll = Dice()
                print("Do you wish to fight, or try to run? ")
                command = PlayerInput.input_parser()
                if command == "fight":
                    print("You secure your armour, draw your weapon, and give pray to the gods...")
                    while battling:
                        if dice_roll.roll_comparison() == "attack":
                            print("Attacking\n")
                            player_damage = p_character.skill_fighting * randint(1, 10)
                            e_health -= player_damage
                            print(player_damage)
                            print("The enemy has {0} health remaining\n".format(e_health))
                            if e_health <= e_min_health:
                                print("You win\n")
                                return False
                            else:
                                break
                        elif dice_roll.roll_comparison() == "defend":
                            print("Enemy Attacking\n")
                            enemy_damage = e_character.skill_fighting * randint(1, 10)
                            p_health -= enemy_damage
                            print(enemy_damage)
                            print("You have {0} health remaining".format(p_health))
                            if p_health <= p_min_health:
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
    def __init__(self):
        Characters.__init__(self)
        self.name = self.name
        self.min_health = 1
        self.enemy_health = 50
        self.skill_level = 2
        self.skill_fighting = 2
        self.item_list = {}

    @property
    def enemy_name(self):
        self.name = self.name
        return self.name

    @property
    def enemy_cur_health(self):
        self.enemy_health = self.enemy_health
        return self.enemy_health



class PlayerCharacter(object):
    def __init__(self):
        Characters.__init__(self)
        self.name = self.name
        self.min_health = 1
        self.cur_health = 50
        self.max_health = 200
        self.state = "normal"
        self.skill_level = self.skill_level
        self.skill_crafting = self.skill_crafting
        self.skill_fighting = self.skill_fighting
        self.skill_trading = self.skill_trading
        self.item_list = {"Iron Sword": "An old, rusted sword", "Satchel": "Old leather satchel"}

    @property
    def player_name(self):
        new_name = "Generic Hero"
        assert isinstance(new_name, str)
        self.name = new_name
        return self.name

    @property
    def player_min_health(self):
        return "min health working"

    @property
    def player_health(self):
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
    init_game = input("Type 'new game' to start a new game: ")

    if init_game == "new game":
        print("Welcome to pyBattle, an exercise in enlightenment, and a wannabe-programmers journey.\n")
        print("Make a character, battle monsters, capture goodies, craft items.\n")
    else:
        print("I've always wanted to be a lumberjack.")
        exit()

    while game_active:
        char_obj = Characters()
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