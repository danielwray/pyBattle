#!/usr/bin/env python3

__Version__ = '0.0.5'
__status__ = 'Prototype'

from random import randint
from random import choice
import time


class PlayerCharacter(object):
    """
    Character class
        - PlayerCharacter class
    Contains properties of player character (character object)
    - name, health stats, state, levels, items
    """
    name = ''
    state = ''
    min_health = 1
    cur_health = 100
    max_health = 175
    level = 1
    crafting = 1
    fighting = 1
    trading = 1
    item_list = {'A rusted sword': 2, 'An old dane axe': 4, 'A satchel': 0}
    coins = 100
    won = 0
    lost = 0
    drawn = 0

    def __init__(self, name):
        self.name = name
        self.cur_health = self.cur_health
        self.min_health = self.min_health
        self.cur_health = self.cur_health
        self.max_health = self.max_health
        self.level = self.level
        self.crafting = self.crafting
        self.fighting = self.fighting
        self.trading = self.trading
        self.item_list = self.item_list
        self.coins = self.coins
        self.won = self.won
        self.lost = self.lost
        self.drawn = self.drawn


class EnemyCharacter(object):
    """
    Character class
        - EnemyCharacter class
    Contains properties of enemy character (character object)
    - name, health stats, levels, items
    """
    name = ''
    min_health = 1
    cur_health = 1
    skill_level = 1
    fighting = 1
    # {'name' : int(value)}
    item_list = {}
    coins = 0

    def __init__(self, name, enemy_health, skill_level, fighting, item_list, coins):
        self.name = name
        self.cur_health = enemy_health
        self.skill_level = skill_level
        self.fighting = fighting
        self.item_list = item_list
        self.coins = coins


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
        return '{0} rolled: {1} | Enemy rolled: {2}'.format(player.name, self.player_roll, self.enemy_roll)

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
            return 'Error rolling die!'


class PlayerInput:
    @staticmethod
    def input_parser():
        player_input = input('~> ')
        player_output = player_input
        return player_output.lower()


def main():
    game_active = True
    init_game = input('Type "New" to start a new game: ')

    if init_game == 'new' or init_game == 'New':
        print('Welcome to pyBattle Version 0.0.5.')
        print('Create a character, battle monsters, loot items, craft weapons...\n')
    else:
        print('Ive always wanted to be a lumberjack.')
        exit()

    while game_active:
        game_mode = game_state
        print('type menu to bring up the available activities.\n')
        command = PlayerInput.input_parser()
        if command == 'menu':
            print('Select a game mode: stats, rest, fight, craft, trade.\n')
            game_mode(PlayerInput.input_parser())
        elif command == 'help?':
            print(' insert game help here - read from file...')
        elif command == 'quit':
            print('Goodbye')
            return False
        else:
            print('For a list of commands type help?')


def game_state(state):
    if state == 'stats':
        stats_system()

    elif state == 'fight':
        battle_system()

    elif state == 'rest':
        rest_system()

    elif state == 'craft':
        print('You pull out a hammer and start getting creative.\n')
        print('Your current crafting level is {0}'.format(player.crafting))

    elif state == 'trade':
        print('You put on your haggling hat and start looking for deals.\n')
        print('Your current trading level is {0}'.format(player.trading))

    else:
        print('You sit on a rock, and ponder the mysteries of life.\n')


def stats_system():
    print('{0} has won: {1} | lost: {2} | drawn: {3} | battles'.format(player.name, player.won,
                                                                       player.lost, player.drawn))
    print('{0} has {1} health points remaining'.format(player.name, player.cur_health))
    print('{0}\'s Level: {1} | '
          'Crafting: {2} | '
          'Trading: {3} | '
          'Fighting: {4}'.format(player.name, player.level, player.crafting, player.trading, player.fighting))
    print('{0} Has {1} coins'.format(player.name, player.coins))
    print('{0} Carries {1}\n'.format(player.name, ', '.join(player.item_list)))


def battle_system():
    command = PlayerInput()
    delay = time
    print('You are drawn into battle!\n')
    battle_active = True
    e_dat = enemy_data()
    e_dat_name = e_dat.get('Name')
    e_dat_health = e_dat.get('Health')
    e_dat_level = e_dat.get('Level')
    e_dat_fight_level = e_dat.get('Fight level')
    e_dat_items = e_dat.get('Items')
    e_coins = e_dat.get('Coins')
    new_enemy = EnemyCharacter(e_dat_name, e_dat_health, e_dat_level, e_dat_fight_level, e_dat_items, e_coins)
    roll = Die()
    d_counter = 0
    p_counter = 0
    e_counter = 0

    print('Battle stats: \n{0} \nvs \nA {1}\n'.format(player.name, new_enemy.name))
    print('{0} health {1} | {2} health {3}'.format(player.name, player.cur_health, new_enemy.name,
                                                   new_enemy.cur_health))

    weapon_selection = input('Select your weapon\nAvailable: {0}\n~> '.format(', '.join(player.item_list)))
    if weapon_selection in player.item_list:
        weapon_damage = weapon_selection
        weapon_damage = player.item_list[weapon_damage]
        print('{0} adds {1} attack points'.format(weapon_selection, weapon_damage))
    else:
        print('You don\'t posses a {0}'.format(weapon_selection))
        weapon_damage = 1

    print('{0} carries: {1} and {2} coins\n'.format(new_enemy.name, new_enemy.item_list, new_enemy.coins))
    delay.sleep(2)

    while battle_active:
        roll_data = roll.roll_comparison()
        player_attack_damage = roll.player_roll
        enemy_attack_damage = roll.enemy_roll

        # player wins if enemy health 0
        if new_enemy.cur_health == 1:
            player.won += 1
            delay.sleep(1)
            print('\n{0} wins the battle'.format(player.name))
            print('{0} won in {1} moves\n'.format(player.name, p_counter))
            print('{0} drops {1}'.format(e_dat_name, e_dat_items))
            print('Do you wish to loot the dropped items?')
            # loot enemy statement
            if command.input_parser() == 'yes':
                add_to_inventory = player.item_list
                add_to_inventory[new_enemy.item_list] = randint(1, 5)
                player.coins = player.coins + new_enemy.coins
                print('Looted items: {0}'.format(new_enemy.item_list))
                print('Looted coins: {0}'.format(new_enemy.coins))
                return False
            else:
                print('You leave the items.')
                return False

        # enemy wins if player health 0
        elif player.cur_health == 1:
            player.lost += 1
            delay.sleep(1)
            print('\nThe {0} wins the battle'.format(new_enemy.name))
            print('{0} won in {1} moves'.format(new_enemy.name, e_counter))
            return False

        # draw if enemy health and player health 0
        elif new_enemy.cur_health == 1 and player.cur_health == 1:
            player.drawn += 1
            delay.sleep(1)
            print('Draw!')
            return False

        # Attacking/ Defending loop
        else:
            # player attacks enemy
            if roll_data == 0:
                delay.sleep(1)
                print(roll.roll_result())
                print('Attacking')
                new_enemy.cur_health -= player.fighting * player_attack_damage + weapon_damage
                if new_enemy.cur_health < 1:
                    new_enemy.cur_health = 1
                print('Enemy has {0} health points remaining\n'.format(new_enemy.cur_health))
                p_counter += 1
                pass

            # enemy attacks player
            elif roll_data == 1:
                delay.sleep(1)
                print(roll.roll_result())
                print('Defending')
                player.cur_health -= new_enemy.fighting * enemy_attack_damage
                if player.cur_health < 1:
                    player.cur_health = 1
                print('Player has {0} health points remaining\n'.format(player.cur_health))
                e_counter += 1
                pass

            # no hit
            else:
                delay.sleep(1)
                print(roll.roll_result())
                print('No hits!\n')
                d_counter += 1
                pass


def rest_system():
    command = PlayerInput()
    delay = time
    print('You sit and rest for a while.\n')
    print('Your current health level is {0}\n'.format(player.cur_health))
    print('You can pay to visit a healer, or rest. What do you want to do?\n')
    heal_rest = PlayerInput.input_parser()
    if heal_rest == 'healer':
        print('enter how much coin you are willing to pay...')
        coins_to_health = int(command.input_parser())
        if coins_to_health < 101 and coin_management(coins_to_health):
            if player.cur_health < player.max_health:
                player.cur_health += coins_to_health
                player.coins -= coins_to_health
                print('Health increased to: {0}'.format(player.cur_health))
            else:
                player.cur_health = player.max_health
                print('Health is at maximum: {0}'.format(player.cur_health))
        else:
            print('You\'ll have to rest...')
    elif heal_rest == 'rest':
        try:
            recover = int(input('Enter the duration of time you wish to rest for: '))
            if recover > 0:
                delay.sleep(recover / 2)
                player.cur_health += recover
            else:
                print('You don\'t seem to feel any better for resting.')
        except ValueError:
            print('You didn\'t enter a number.')
    else:
        print('You appear to be undecided.')


def coin_management(coins_to_deduct):
    coins_available = player.coins
    if coins_to_deduct <= coins_available:
        print('You hand over your coins...')
        return True
    else:
        print('You do not have enough coins...')
        print('{0} coins available'.format(player.coins))
        return False


def enemy_data():
    enemy_name_data = ['small goblin', 'angry goblin', 'warrior goblin', 'berserk goblin', 'king goblin',
                       'mediocre orc', 'slightly less mediocre, and more smelly orc', 'orc leader', 'thief',
                       'escaped prisoner', 'outlaw', 'deserting soldier', 'trained man-at-arms',
                       'landed knight', 'knight', 'turnip']
    enemy_health_data = randint(10, 75)
    enemy_skill_data = randint(1, 6)
    enemy_fighting_data = randint(1, 3)
    enemy_item_data = {'An old rusted axe': 1, 'An old rusted sword': 1, 'An Old leather jerkin': 1,
                       'An old steel helmet': 1, 'An old pair of gauntlets': 1, 'Some old leather boots': 1,
                       'Old chain mail': 1, 'A hammer': 1, 'A single shoe': 1}
    enemy_coins_data = randint(0, 10)
    enemy_name_rand = choice(list(enemy_name_data))
    enemy_item_rand = choice(list(enemy_item_data))

    return {'Name': ''.join(enemy_name_rand), 'Health': enemy_health_data, 'Level': enemy_skill_data,
            'Fight level': enemy_fighting_data, 'Items': enemy_item_rand, 'Coins': enemy_coins_data}


if __name__ == '__main__':
    print('Enter your name')
    player_name = input('~> ')
    print('\nLets get going, {0}'.format(player_name))
    player = PlayerCharacter(player_name)
    main()