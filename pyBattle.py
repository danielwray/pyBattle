#!/usr/bin/env python3

__Version__ = '0.0.5'
__status__ = 'Prototype'


from random import randint
from random import choice
import time


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
    item_list = {}

    def __init__(self, name, enemy_health, skill_level, fighting, item_list):
        self.name = name
        self.cur_health = enemy_health
        self.skill_level = skill_level
        self.fighting = fighting
        self.item_list = item_list


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
    max_health = 999
    level = 1
    crafting = 1
    fighting = 2
    trading = 1
    item_list = {'Iron Sword': 'An old, rusted sword', 'Satchel': 'Old leather satchel'}

    def __init__(self, name):
        self.name = name
        self.cur_health = self.cur_health


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
    init_game = input('Type new game to start a new game: ')

    if init_game == 'new game':
        print('Welcome to pyBattle, an exercise in enlightenment, and a wannabe-programmers journey.\n')
        print('Make a character, battle monsters, capture goodies, craft items.\n')
        print('type menu to bring up the available activities.\n')
    else:
        print('Ive always wanted to be a lumberjack.')
        exit()

    while game_active:
        game_mode = game_state
        command = PlayerInput.input_parser()
        if command == 'menu':
            print('Select a game mode: rest, fight, craft, trade.\n')
            game_mode(PlayerInput.input_parser())
        elif command == 'help?':
            print(' insert game help here - read from file...')
        elif command == 'quit':
            print('Goodbye')
            return False
        else:
            print('For a list of commands type help?')


def game_state(state):
    delay = time
    if state == ' ':
        print('...\n')

    elif state == 'fight':
        print('You are drawn into battle!\n')
        battle_active = True
        e_dat = enemy_data()
        e_dat_name = e_dat.get('Name')
        e_dat_health = e_dat.get('Health')
        e_dat_level = e_dat.get('Level')
        e_dat_fight_level = e_dat.get('Fight level')
        e_dat_items = e_dat.get('Items')
        new_enemy = EnemyCharacter(e_dat_name, e_dat_health, e_dat_level, e_dat_fight_level, e_dat_items)
        roll = Die()
        d_counter = 0
        p_counter = 0
        e_counter = 0

        print('Battle stats: \n{0} \nvs \na {1}\n'.format(player.name, new_enemy.name))
        print('{0} health {1} | {2} health {3}'.format(player.name, player.cur_health,
                                                       new_enemy.name, new_enemy.cur_health))
        print('{0} carries: {1} | {2} carries: {3}\n'.format(player.name, ", ".join(player.item_list),
                                                             new_enemy.name, new_enemy.item_list))
        delay.sleep(2)

        while battle_active:
            roll_data = roll.roll_comparison()
            player_attack_damage = roll.player_roll
            enemy_attack_damage = roll.enemy_roll
            if new_enemy.cur_health == 0:
                # player wins if enemy health 0
                delay.sleep(1)
                print('\n{0} wins the battle'.format(player.name))
                print('{0} won in {1} moves\n'.format(player.name, p_counter))
                print('{0} drops {1}'.format(e_dat_name, e_dat_items))
                add_to_inventory = player.item_list
                add_to_inventory[new_enemy.item_list] = 'Looted item'
                print('{0} now carries {1}'.format(player.name, ', '.join(player.item_list)))
                return False
            elif player.cur_health == 0:
                # enemy wins if player health 0
                delay.sleep(1)
                print('\nThe {0} wins the battle'.format(new_enemy.name))
                print('{0} won in {1} moves'.format(new_enemy.name, e_counter))
                return False
            elif new_enemy.cur_health == 0 and player.cur_health == 0:
                # draw if enemy health and player health 0
                delay.sleep(1)
                print('Draw!')
                return False
            else:
                if roll_data == 0:
                    delay.sleep(1)
                    print(roll.roll_result())
                    print('Attacking')
                    new_enemy.cur_health -= player.fighting * player_attack_damage
                    if new_enemy.cur_health < 1:
                        new_enemy.cur_health = 0
                    print('Enemy has {0} health remaining\n'.format(new_enemy.cur_health))
                    p_counter += 1
                    pass
                elif roll_data == 1:
                    delay.sleep(1)
                    print(roll.roll_result())
                    print('Defending')
                    player.cur_health -= new_enemy.fighting * enemy_attack_damage
                    if player.cur_health < 1:
                        player.cur_health = 0
                    print('Player has {0} health remaining\n'.format(player.cur_health))
                    e_counter += 1
                    pass
                else:
                    delay.sleep(1)
                    print(roll.roll_result())
                    print('Draw!\n')
                    d_counter += 1
                    pass

    elif state == 'rest':
        print('You sit and rest for a moment; weary of your past adventures you start to recover from your wounds.\n')
        print('Your current health level is {0}'.format(player.cur_health))
        recover = int(input('Enter the duration of time you rest for: '))
        if recover > 3:
            delay.sleep(recover)
            player.cur_health = 100
        else:
            print('Uh oh!')

    elif state == 'craft':
        print('You pull out a hammer and start getting creative.\n')
        print('Your current crafting level is {0}'.format(player.crafting))

    elif state == 'trade':
        print('You put on your haggling hat and start looking for deals.\n')
        print('Your current trading level is {0}'.format(player.trading))

    else:
        print('You sit on a rock, and ponder the mysteries of life.\n')


# make this into a class so I can call the separate data returns to enter into enemy instances.
def enemy_data():
    enemy_name_data = ['small goblin', 'angry goblin', 'warrior goblin', 'berserk goblin', 'king goblin',
                       'mediocre orc', 'slightly less mediocre, and more smelly orc', 'orc leader', 'thief',
                       'escaped prisoner', 'outlaw', 'deserting soldier', 'trained man-at-arms', 'landed knight',
                       'knight', 'turnip']
    enemy_name_rand = choice(list(enemy_name_data))
    enemy_health_data = randint(10, 50)
    enemy_skill_data = randint(1, 10)
    enemy_fighting_data = randint(1, 3)
    enemy_item_data = ('An old rusted axe', 'Old leather jerkin')
    enemy_item_rand = choice(list(enemy_item_data))

    return {'Name': ''.join(enemy_name_rand), 'Health': enemy_health_data, 'Level': enemy_skill_data,
            'Fight level': enemy_fighting_data, 'Items': enemy_item_rand}


if __name__ == '__main__':
    print('Enter your name')
    player_name = input('~>')
    print('\nLets get going, {0}'.format(player_name))
    player = PlayerCharacter(player_name)
    main()