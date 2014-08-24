#!/usr/bin/env python3

__Version__ = '0.0.4'
__status__ = 'Prototype'

import random


# battle against an enemy of a random level
# - win to get coins and buy equipment - equipment increases health points, and damage points
#   - buy weapons (dp+), and armour/shields (hp+)
#       - sword, axe, spear, or mace
#       - leather, chain mail, plate armour, shield
# - lose and start from scratch

class Enemy:
    @property
    def enemy_name(self):
        name_list = ("Goblin", "Troll", "Bandit", "Man at Arms", "Knight", "House Guard", "Elite Guard",
        "Giant", "Dragon")
        return "Your opponent is an {0}". format(random.choice(name_list))
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
        return "Items to loot: {0} & {1} coins".format(random.choice(items), coins)

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

class Current_Player:
    def __init__(self, p_name, p_hp):
        self.player_name = p_name
        self.player_hp = p_hp
    @property
    def current_player_data(self):
        current_name = self.player_name
        current_hp = self.player_hp
        return "{0}, {1}".format(current_name, current_hp)

class Current_Enemy:
    def __init__(self, e_name, e_hp, e_loot):
        self.enemy_name = e_name
        self.enemy_hp = e_hp
        self.enemy_loot = e_loot
    @property
    def current_enemy_data(self):
        current_name = self.enemy_name
        current_hp = self.enemy_hp
        current_loot = self.enemy_loot
        return "{0}, {1}".format(current_name, current_loot)

class Dice:
    @property
    def dice_data(self):
        dice_result = random.randint(1, 6)
        return dice_result

def main():
    # game intro
    print ("|| Welcome to pyBattle, the most awe-inspiring game ever developed!||\n")

    game_active = True
    player_class = Player()
    enemy_class = Enemy()
    dice_class = Dice()
    current_player_class = Current_Player(player_class.player_name, player_class.player_hp)
    current_enemy_class = Current_Enemy(enemy_class.enemy_name, enemy_class.enemy_hp, enemy_class.enemy_items)

    print (current_player_class.player_name)

    # game loop
    while game_active == True:
        __current_player = current_player_class.current_player_data
        __current_enemy = current_enemy_class.current_enemy_data
        __yes_list = ("Y", "YES", "SURE", "ATTACK", "FIGHT", "HIT")
        __no_list = ("N", "NO", "NOPE", "DEFEND", "SHIELD")
        __quit_list = ("EXIT", "QUIT", "END")
        __player_fight_input = input("Do you want to enter the fighting pit? \n")
        __player_input_upper = __player_fight_input.upper()
        __fight_active = True
        if __player_input_upper in __yes_list:
            current_enemy_class = Current_Enemy(enemy_class.enemy_name, enemy_class.enemy_hp, enemy_class.enemy_items)
            print (__current_enemy)
            __enemy_health = current_enemy_class.enemy_hp
            __player_health = current_player_class.player_hp
            __enemy_remaining_health = __enemy_health
            __player_remaining_health = __player_health
            # battle system
            while __fight_active == True:
                __player_attack = player_class.player_dp
                __enemy_attack = enemy_class.enemy_dp
                __player_attack_input = input("Do you wish to attack?")
                __player_attack_input_upper = __player_attack_input.upper()
                if  __enemy_remaining_health < 0:
                    print ("You win")
                    __fight_active = False
                elif __player_remaining_health < 0:
                    print ("You lose")
                    __fight_active = False
                else:
                    # attack loop
                    if __player_attack_input_upper in __yes_list:
                            __curret_dice = dice_class.dice_data
                            if 4 < __curret_dice < 6:
                                # enemy loses health
                                __enemy_remaining_health = __enemy_remaining_health - __player_attack
                                print ("Enemy hit")
                            elif __curret_dice < 4:
                                # player loses health
                                __player_remaining_health = __player_remaining_health - __enemy_attack
                                print ("You are hit")
                            elif __curret_dice > 5:
                                # enemy defends and gains health
                                __enemy_add_health = random.randint(0, 20)
                                __enemy_remaining_health = __enemy_remaining_health + __enemy_add_health
                                print ("Enemy defended, and gained health")
                            else:
                                print ("Missed")
                    # defend loop
                    elif __player_attack_input_upper in __no_list:
                        if __curret_dice > 4:
                            # player defends and gains health
                            print ("You defend")
                            __player_add_health = random.randint(0, 20)
                            __player_remaining_health = __player_remaining_health + __player_add_health
                        else:
                            # player loses health
                            __player_remaining_health = __player_remaining_health - __enemy_attack
                            print ("You failed to defend")
        elif __player_input_upper in __no_list:
            print ("Would you like to change your offensive, and/ or defensive setup?")
            if __player_attack_input_upper in __yes_list:
                pass
            elif __player_attack_input_upper in __no_list:
                pass
            else:
                break
        elif __player_input_upper in __quit_list:
            print ("The tales will recall your name")
            exit()
        else:
            pass

if __name__ == "__main__":
    main()