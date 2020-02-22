import pygame as pg
import time
import graphics

pg.init()
screen = graphics.Screen(800, 600)

# Load platform
pg.display.flip()

attackIcon = graphics.Icon('images/attack.png', screen)
attackIcon.move_left()
attackIcon.move_right()
attackIcon.move_left()


