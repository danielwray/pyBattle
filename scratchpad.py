#!/usr/bin/env python3

__Version__ = '0.0.1'
__status__ = 'Prototype'

from random import randint


class Character:
    def __init__(self):
        self.name = " "
        self.hp = 1

    def damage(self, target):
        damage = randint(0, self.hp)
        target.hp = target.hp - damage
        if damage == 0:
            print ("Attack repelled")
        else:
            print ("Attack landed {0} points of damage".format(damage))
        return target.hp <= 0


class Enemy:
    def __init__(self, Player):
        Character.__init__(self)
        self.name = "Test Creature"
        self.hp = randint(10, Player.hp)

class Player:
    def __init__(self):
        Character.__init__(self)
        self.state = "normal"
        self.name = input("Your name? ")
        self.hp = 20
        self.hp_max = 25
    def status_change(self):
        self.state = input("fight? ")
    def attack(self):
        if self.state == "fight":
            self.enemy_attacks()
    def enemy_attacks(self):
        if self.target.damage(self):
            print ("test")

def main():
    run = Player()
    run.status_change()

if __name__ == "__main__":
    main()