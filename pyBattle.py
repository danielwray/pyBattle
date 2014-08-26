#!/usr/bin/env python3

__Version__ = '0.0.2'
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
    - damage, states (normal, fighting, crafting et al), character creations...
    """

    def __init__(self):
        self.name = " "
        self.min_health = 1
        self.cur_health = 1
        self.max_health = 200
        self.state = " "
        self.skill_level = 1
        self.skill_crafting = 1
        self.skill_fighting = 1
        self.skill_trading = 1
        self.item_list = {}

    def damage(self, target):
        pass

    def game_state(self, new_state):
        self.state = new_state
        if self.state == "normal":
            print(" ")
        elif self.state == "fight":
            fight_active = True
            print("You stumble upon an fierce enemy\n")
            spawn_enemy = EnemyCharacter()
            enemy_stats = spawn_enemy.new_enemy
            # display new enemy stats
            for i in sorted(enemy_stats):
                print(i, enemy_stats[i])

            while fight_active:
                print("Do you wish to fight, or try to run? ")
                command = PlayerInput.input_parser()
                if command == "fight":
                    dice_roll = Dice()
                    print("You secure your armour, draw your weapon, and give pray to the gods...")
                    if dice_roll.roll_comparison:
                        # insert enemy_health - character_damage here
                        # if enemy_health < 0
                        print("win")
                        return False
                    elif not dice_roll.roll_comparison:
                        # insert character_health - enemy_damage here
                        # if character_health < 0
                        print("Lose")
                        return False
                    else:
                        # print something about parrying etc
                        print("Missed")
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

    def create_player(self, player_name):
        self.name = player_name
        return PlayerCharacter.new_player(self)


class EnemyCharacter(object):
    def __init__(self):
        Characters.__init__(self)
        self.name = " "
        self.cur_health = 1
        self.skill_level = 1
        self.skill_fighting = 1
        self.item_list = {}

    @property
    def new_enemy(self):
        self.name = "Small Goblin"
        self.cur_health = randint(25, 100)
        self.skill_level = randint(1, 5) * self.skill_fighting / 2
        self.skill_fighting = randint(1, 5)
        self.item_list = {"Goblin sword": 5}
        new_enemy = {"Name: ": self.name, "Health: ": self.cur_health, "Skill level: ": self.skill_level,
                     "Fight level: ": self.skill_fighting, "Items held: ": self.item_list}
        e_data_keys = new_enemy.keys()
        e_data_vals = new_enemy.values()
        return new_enemy


class PlayerCharacter(object):
    def __init__(self):
        Characters.__init__(self)
        self.name = " "
        self.min_health = 1
        self.cur_health = 1
        self.max_health = 200
        self.state = "normal"
        self.skill_level = 1
        self.skill_crafting = 1
        self.skill_fighting = 1
        self.skill_trading = 1
        self.item_list = {}

    def new_player(self, level, c_level, f_level, s_level, i_list):
        self.cur_health = 100
        self.state = "normal"
        self.skill_level = level
        self.skill_crafting = c_level
        self.skill_fighting = f_level
        self.skill_trading = s_level
        self.item_list = i_list
        return self.name, self.cur_health, self.state, self.skill_trading, self.item_list


class Dice(object):
    def __init__(self):
        Characters.__init__(self)
        self.player_roll = randint(2, 12)
        self.enemy_roll = randint(1, 2)

    def roll_result(self):
        return self.player_roll, self.enemy_roll

    def roll_comparison(self):
        if self.player_roll > self.enemy_roll:
            return True
        elif self.player_roll < self.enemy_roll:
            return False
        else:
            return "tie"


class PlayerInput:
    @staticmethod
    def input_parser():
        player_input = input("~> ")
        player_output = player_input
        return player_output.lower()


def main():
    game_active = True
    char_obj = Characters()

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