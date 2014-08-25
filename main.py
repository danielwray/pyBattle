#!/usr/bin/env python3

__Version__ = '0.0.4'
__status__ = 'Prototype'

import random


class Enemy:
    @property
    def enemy_name(self):
        name_list = ("Goblin", "Troll", "Bandit", "Man at Arms", "Knight", "House Guard", "Elite Guard",
                     "Giant", "Dragon")
        return random.choice(name_list)

    @property
    def enemy_hp(self):
        hp = random.randint(10, 120)
        return hp

    @property
    def enemy_dp(self):
        dp = random.randint(0, 12)
        return dp

    @property
    def enemy_items(self):
        items = ("axe", "sword", "shield", "helmet", "leather armour")
        coins = random.randint(0, 12)
        return random.choice(items), coins


class Player:
    @property
    def player_name(self):
        name = input("Enter your name: ")
        return "{0}, the bard's will tell tales of your bravery!".format(name)

    @property
    def player_hp(self):
        hp = 125
        return hp

    @property
    def player_dp(self):
        dp = random.randint(0, 36)
        return dp

    @property
    def player_items(self):
        items = ()
        coins = 0
        return items, coins


class CurrentPlayer:
    def __init__(self, p_name, p_hp):
        self.player_name = p_name
        self.player_hp = p_hp

    @property
    def current_player_data(self):
        current_name = self.player_name
        current_hp = self.player_hp
        return current_name, current_hp


class CurrentEnemy:
    def __init__(self, e_name, e_hp, e_loot):
        self.enemy_name = e_name
        self.enemy_hp = e_hp
        self.enemy_loot = e_loot

    @property
    def current_enemy_data(self):
        current_name = self.enemy_name
        current_hp = self.enemy_hp
        current_loot = self.enemy_loot
        return current_name, current_loot


class Dice:
    @property
    def dice_data(self):
        dice_result = random.randint(1, 6)
        return dice_result


def main():
    # game intro
    print("|| Welcome to pyBattle, the most awe-inspiring game ever developed!||\n")

    game_active = True
    player_class = Player()
    enemy_class = Enemy()
    dice_class = Dice()
    current_player_class = CurrentPlayer(player_class.player_name, player_class.player_hp)
    current_enemy_class = CurrentEnemy(enemy_class.enemy_name, enemy_class.enemy_hp, enemy_class.enemy_items)
    current_dice = dice_class.dice_data

    print(current_player_class.player_name)

    # game loop
    while game_active:
        current_enemy = current_enemy_class.current_enemy_data
        yes_list = ("Y", "YES", "SURE", "ATTACK", "FIGHT", "HIT")
        no_list = ("N", "NO", "NOPE", "DEFEND", "SHIELD")
        quit_list = ("EXIT", "QUIT", "END")
        player_fight_input = input("Do you want to enter the fighting pit? \n")
        player_input_upper = player_fight_input.upper()
        fight_active = True
        if player_input_upper in yes_list:
            print(current_enemy)
            enemy_health = current_enemy_class.enemy_hp
            player_health = current_player_class.player_hp
            enemy_remaining_health = enemy_health
            player_remaining_health = player_health
            # battle system
            while fight_active:
                player_attack = player_class.player_dp
                enemy_attack = enemy_class.enemy_dp
                player_attack_input = input("Do you wish to attack?")
                player_attack_input_upper = player_attack_input.upper()
                # player loses
                if enemy_remaining_health < 0:
                    print("You win")
                    fight_active = False
                # player wins
                elif player_remaining_health < 0:
                    print("You lose")
                    fight_active = False
                else:
                    # attack loop
                    if player_attack_input_upper in yes_list:
                        current_dice = dice_class.dice_data
                        if 4 < current_dice < 6:
                            # enemy loses health
                            enemy_remaining_health = enemy_remaining_health - player_attack
                            print("Enemy hit")
                        elif current_dice < 4:
                            # player loses health
                            player_remaining_health = player_remaining_health - enemy_attack
                            print("You are hit")
                        elif current_dice > 5:
                            # enemy defends and gains health
                            enemy_add_health = random.randint(0, 10)
                            enemy_remaining_health = enemy_remaining_health + enemy_add_health
                            print("Enemy defended, and gained health")
                        else:
                            print("Missed")
                    # defend loop
                    elif player_attack_input_upper in no_list:
                        if current_dice > 4:
                            # player defends and gains health
                            print("You defend")
                            player_add_health = random.randint(0, 20)
                            player_remaining_health = player_remaining_health + player_add_health
                        else:
                            # player loses health
                            player_remaining_health = player_remaining_health - enemy_attack
                            print("You failed to defend")
        elif player_input_upper in no_list:
            print("Would you like to change your offensive, and/ or defensive setup?")
            if player_attack_input_upper in yes_list:
                pass
            elif player_attack_input_upper in no_list:
                pass
            else:
                break
        elif player_input_upper in quit_list:
            print("The tales will recall your name")
            exit()
        else:
            pass


if __name__ == "__main__":
    main()
