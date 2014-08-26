#!/usr/bin/env python3

__Version__ = '0.0.1'
__status__ = 'Prototype'


''' pyBattle refactor

    The code became to much of a mess - I couldn't take it anymore
'''

from random import randint


# classes
class Characters(object):
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

    def damage(self, target):
        pass

    def status(self, new_state):
        self.state = new_state
        if self.state == "normal":
            print("The situation doesn't require any thought")
        elif self.state == "fight":
            print("An enemy appears out of the mist")
            self.name = "Crazy one-eyed Goblin King"
            return EnemyCharacter.new_enemy(self)
        elif self.state == "resting":
            print("You sit and rest for a moment; the sun beams down and you feel well")
        elif self.state == "crafting":
            print("You pull out a hammer and start getting creative")
        elif self.state == "trading":
            print("You put on your haggling hat and start looking for deals")
        else:
            print("You sit on a rock and ponder the mysteries of life")

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

    def new_enemy(self):
        self.cur_health = randint(25, 100)
        self.skill_level = randint(1, 5)
        self.skill_fighting = randint(1, 5)
        return self.name, self.cur_health, self.skill_level, self.skill_fighting


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

    def new_player(self):
        self.cur_health = 100
        self.state = "normal"
        return self.name, self.cur_health, self.state, self.skill_trading


def main():
    create_player = Characters()
    player_change_state = Characters()
    player_input = input("->> ")

    if player_input == "stat":
        player_input = input("->>")
        print(player_change_state.status(player_input))
    else:
        player_input = input("->>")
        print(create_player.create_player(player_input))

if __name__ == "__main__":
    main()