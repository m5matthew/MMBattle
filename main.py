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
        self.screen = graphics.Screen(800, 600)
        pg.display.flip()

    def start_battle(self):
        screen = self.screen
        attackIcon = graphics.Icon('images/attack.png', screen)
        fireballIcon = graphics.Icon('images/fireball.png', screen)
        monsterTurn = False
        playerTurn = True

        while not self.game_over():

            if screen.currMoving:  
                screen.currMoving.move()
                time.sleep(1/100000000)
                pg.display.flip()
            
            elif monsterTurn:
                # If monster is not dead, monster attacks mage
                if not self.monster.is_dead():
                    screen.update_health(self.mage.hp, self.monster.hp)
                    screen.refresh()
                    pg.display.flip()
                    self.monster.attack(self.mage)
                    screen.currMoving = attackIcon
                    attackIcon.place_right()
                monsterTurn = False

            elif not monsterTurn and not playerTurn:
                
                screen.update_health(self.mage.hp, self.monster.hp)
                screen.refresh()
                pg.display.flip()

                self.print_stats()
                print("")

                playerTurn = True

            events = pg.event.get()
            for event in events:

                # Mage's move
                if event.type == pg.QUIT:
                    pg.quit()   
                elif event.type == pg.KEYDOWN and not screen.currMoving:
                    if event.key == pg.K_0:
                        self.mage.attack(self.monster)
                        screen.currMoving = attackIcon
                        attackIcon.place_left()
                    elif event.key == pg.K_1:
                        self.mage.fireball(self.monster)
                        screen.currMoving = fireballIcon
                        fireballIcon.place_left()
                    elif event.key == pg.K_2:
                        self.mage.heal(random.randint(5, 10))
                    elif event.key == pg.K_3:
                        self.mage.mana += 10
                    else:
                        print("ERROR:Incorrect Input detected: ", event.key)
                        break
                    
                    playerTurn = False
                    monsterTurn = True 

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

mymage = game.Mage("Ryan", 100, 2)
randommonster = game.Monster()

mybattle = Battle(mymage, randommonster)
# while True:
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             break
mybattle.start_battle()
