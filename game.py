import random


class Character:

    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power

    def lose_hp(self, amt):
        self.hp -= amt

    def is_dead(self):
        if self.hp <= 0:
            return True
        else:
            return False

    def attack(self, opponent):
        print(self.name, "attacks", opponent.name, "for", str(self.power), "damage!")
        opponent.lose_hp(self.power)


class Mage(Character):

    def __init__(self, name, hp=100, power=1, mana=100):
        super().__init__(name, hp, power)
        self.mana = mana

    def fireball(self, opponent):
        if self.mana >= 10:
            print(self.name, "casts fireball!")
            opponent.lose_hp(20)
            self.mana -= 10

    def heal(self, amt):
        if self.mana >= 10:
            print(self.name, "healing for", str(amt), "hp")
            self.hp += amt
            self.mana -= 10

    def __str__(self):
        return self.name + " has " + str(self.hp) + "HP" + " and " + str(self.mana) + "MP"


class Monster(Character):

    def __init__(self, name="Monster", hp=random.randint(1,100)):
        super().__init__(name, hp, 10)

    def critical_hit(self, opponent):
        opponent.hp -= 2*self.power

    def __str__(self):
        return self.name + " has " + str(self.hp) + "HP"


