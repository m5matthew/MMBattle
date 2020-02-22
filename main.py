import pygame as pg
import graphics
import game
import random
import time


class Battle:
    def __init__(self, mage, monster):
        self.mage = mage
        self.monster = monster
        self.print_stats()

    def start_battle(self):

        attackIcon = graphics.Icon('images/attack.png', screen)

        while not self.game_over():
            print("What would you like to do?")
            print("0 --> normal attack (0 mana)")
            print("1 --> fireball (-10 mana)")
            print("2 --> heal between 5 to 30 hp (-10 mana)")
            print("3 --> skip turn (+10 mana)")
            mage_move = int(input())

            # Mage's move
            if mage_move == 0:
                self.mage.attack(self.monster)
                attackIcon.move_right()
            elif mage_move == 1:
                self.mage.fireball(self.monster)
            elif mage_move == 2:
                self.mage.heal(random.randint(5, 10))
            elif mage_move == 3:
                self.mage.mana += 10

            time.sleep(1)

            # If monster is not dead, monster attacks mage
            if not self.monster.is_dead():
                self.monster.attack(self.mage)
                attackIcon.move_left()
            
            screen.update_health(self.mage.hp, self.monster.hp)
            screen.refresh()
            pg.display.flip()

            self.print_stats()
            print("")

    def game_over(self):

        if self.mage.is_dead() or self.monster.is_dead():
            if not self.mage.is_dead():
                print(self.mage.name, "wins!")
            elif self.mage.is_dead() and self.monster.is_dead():
                print("Tie!")
            elif self.monster.is_dead():
                print(self.monster.name, "wins!")
            print("Game over. Thanks for playing!")
            return True
        else:
            return False

    def print_stats(self):
        print(self.mage)
        print(self.monster)


# Initialize graphics
pg.init()
screen = graphics.Screen(800, 600)
pg.display.flip()

mymage = game.Mage("Ryan", 50, 2)
randommonster = game.Monster()

mybattle = Battle(mymage, randommonster)
mybattle.start_battle()
