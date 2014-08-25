#!/usr/bin/env python3

__Version__ = '0.0.1'
__status__ = 'Prototype'


''' pyBattle refactor

    The code became to much of a mess - I couldn't take it anymore
'''

from random import randint


# classes
class CharacterStats:
    def __init__(self):
        self.name = " "
        self.min_health = 1
        self.current_health = 1
        self.max_health = 1
        # states - normal, fighting, resting, crafting, trading
        self.state = "normal"

    def damage(self, target):
        pass

    def new_character(self, type):
        if type == "enemy":
            enemy_name = ""
            enemy_current_health = self.current_health
            enemy_state = self.state
            return enemy_name, enemy_current_health, enemy_state
        elif type == "player":
            player_name = self.name
            player_current_health = self.current_health
            player_state = self.state
            return player_name, player_current_health, player_state
        else:
            return "Some kind of awful creature has spawned forth and leaped into the infinite pit of doom"

def main():
    new_character = CharacterStats()
    character_type = input("player or enemy? ")

    print(new_character.new_character(character_type))

if __name__ == "__main__":
    main()