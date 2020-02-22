import pygame
import time

CHARACTER_SIZE = 200


class Screen:
    def __init__(self, width, height):

        # init screen
        self.maxHealth = 100
        self.width = width
        self.height = height
        self.backgroundColor = 255, 255, 255
        self.screen = pygame.display.set_mode((width, height))

        # init platform
        platform = pygame.image.load('images/grass.png')
        self.platform = pygame.transform.scale(platform, (width, 100))
        self.platformRect = self.platform.get_rect()
        self.platformRect.y = height / 2 + 100

        # init mage
        mage = pygame.image.load('images/mage.png')
        self.mage = pygame.transform.scale(mage,
                                           (CHARACTER_SIZE, CHARACTER_SIZE))
        self.mageRect = self.mage.get_rect()
        self.mageRect.y = height / 2 - 100
        self.mageHealth = self.maxHealth

        # init monster
        monster = pygame.image.load('images/monster.png')
        self.monster = pygame.transform.scale(monster,
                                              (CHARACTER_SIZE, CHARACTER_SIZE))
        self.monsterRect = self.monster.get_rect()
        self.monsterRect.y = height / 2 - 100
        self.monsterRect.x = width - CHARACTER_SIZE
        self.monster = pygame.transform.flip(self.monster, True, False)
        self.monsterHealth = self.maxHealth

        self.refresh()

    # Refreshes all graphics on the screen
    def refresh(self):
        self.screen.fill(self.backgroundColor)
        self.screen.blit(self.platform, self.platformRect)
        self.screen.blit(self.mage, self.mageRect)
        self.screen.blit(self.monster, self.monsterRect)
        self.draw_health()

    # Adds an image to the screen
    def add_img(self, surface, rect):
        self.screen.blit(surface, rect)

    # Draws health bars on the screen
    def draw_health(self):
        margin = 20
        screenWidth = self.width
        barHeight = 20
        barWidth = 200
        barY = self.height / 2 - 150  # right on top of mage/monster characters
        monsterBarX = screenWidth - barWidth - margin
        backgroundBarColor = (128, 128, 128)  # grey
        maxHealth = 100
        mage_health = self.mageHealth 
        monster_health = self.monsterHealth 
        maxHealth = self.maxHealth

        # draws mage health bar
        mage_health_color = (0, 255, 0)
        width = int(barWidth * mage_health / maxHealth)
        mage_health_bar = pygame.Rect(margin, barY, width, barHeight)
        mage_background_bar = pygame.Rect(margin, barY, barWidth, barHeight)
        pygame.draw.rect(self.screen, backgroundBarColor, mage_background_bar)
        pygame.draw.rect(self.screen, mage_health_color, mage_health_bar)

        # draws mage health bar
        monster_health_color = (0, 255, 0)
        width = int(barWidth * monster_health / maxHealth)
        mon_health_bar = pygame.Rect(monsterBarX, barY, width, barHeight)
        mon_background_bar = pygame.Rect(monsterBarX, barY, barWidth,
                                         barHeight)
        pygame.draw.rect(self.screen, backgroundBarColor, mon_background_bar)
        pygame.draw.rect(self.screen, monster_health_color, mon_health_bar)

    def update_health(self, mage_health, monster_health):
        self.mageHealth = mage_health
        self.monsterHealth = monster_health


class Icon:
    def __init__(self, image_name, screen):
        icon = pygame.image.load(image_name)
        icon = pygame.transform.scale(icon, (100, 100))
        self.icon = icon
        self.rect = icon.get_rect()
        self.rect.y = screen.height / 2
        self.screen = screen
        self.direction = 'RIGHT'

    # Moves Icon from left to right
    def move_left(self):

        # Switch directions if we need to
        if self.direction != 'LEFT':
            self.direction = 'LEFT'
            self.icon = pygame.transform.flip(self.icon, True, False)

        # Keep moving left until you reach left side
        left = [-5, 0]
        self.rect.x = self.screen.width - CHARACTER_SIZE
        while self.rect.left > CHARACTER_SIZE:
            self.screen.refresh()
            self.rect = self.rect.move(left)
            self.screen.add_img(self.icon, self.rect)
            pygame.display.flip()
            time.sleep(1 / 100000)
        self.screen.refresh()
        pygame.display.flip()

    # Moves Icon from right to left
    def move_right(self):
        width = self.screen.width - CHARACTER_SIZE
        if self.direction != 'RIGHT':
            self.direction = 'RIGHT'
            self.icon = pygame.transform.flip(self.icon, True, False)
        right = [5, 0]
        while self.rect.right < width:
            self.screen.refresh()
            self.rect = self.rect.move(right)
            self.screen.add_img(self.icon, self.rect)
            pygame.display.flip()
            time.sleep(1 / 100000)
        self.screen.refresh()
        pygame.display.flip()
