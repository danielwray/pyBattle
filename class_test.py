#!/usr/bin/env python3


class Characters(object):
    name = ''
    health = 1
    strength = 1
    trade = 1
    level = 1
    attributes = []

    def __init__(self, name):
        assert self.valid_name(name)
        self.name = name

    def character_attr(self):
        return self.attributes

    @staticmethod
    def valid_name(name):
        if bool(name) and type(name) == str:
            return True
        else:
            return False


def main():
    name = ''

    while not Characters.valid_name(name):
        name = input("Your name? ")

    player = Characters(name)

    print(player.name, player.health, player.attributes)

if __name__ == "__main__":
    main()