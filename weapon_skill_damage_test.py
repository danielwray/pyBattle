#!/usr/bin/env python3

__Version__ = '0.0.1'
__status__ = 'Prototype'

import random


def main():
    my_weapons = {"Basic Sword": 1, "Castle Forged Sword": 5, "Dane Axe": 7}
    my_skill = 2
    my_target = 100

    # select a value from the weapons list
    select_weapon = input("Select your weapon from the list\n{0}\n~> ".format('| '.join(my_weapons)))
    if select_weapon in my_weapons:
        weapon_choice = select_weapon
        weapon_choice = my_weapons[weapon_choice]
        print(select_weapon)

    while my_target > 1:
        # attack damage is equal to weapon value divided by random int times the skill level
        attack_damage = round(weapon_choice / random.randint(1, 3) * my_skill)
        my_target -= attack_damage
        print('my_target has {0} hp left, my_weapon did {1} dp'.format(my_target, attack_damage))


if __name__ == "__main__":
    main()