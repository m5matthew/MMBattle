import pygame

CHARACTER_SIZE = 200
ICON_SIZE = 100

class Screen:
    def __init__(self, width, height):

        # init screen
        self.maxHealth = 100
        self.width = width
        self.height = height
        self.backgroundColor = 255, 255, 255
        self.screen = pygame.display.set_mode((width, height))
        self.currMoving= None 

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
        icon = pygame.transform.scale(icon, (ICON_SIZE, ICON_SIZE))
        self.icon = icon
        self.rect = icon.get_rect()
        self.rect.y = screen.height / 2
        self.screen = screen
        self.direction = 'RIGHT'
        self.movingLeft = True 
    

    def place_left(self):
        if self.direction != 'RIGHT':
            self.direction = 'RIGHT'
            self.icon = pygame.transform.flip(self.icon, True, False)
        self.rect.x = CHARACTER_SIZE
    
    def place_right(self):
        if self.direction != 'LEFT':
            self.direction = 'LEFT'
            self.icon = pygame.transform.flip(self.icon, True, False)
        self.rect.x = self.screen.width - CHARACTER_SIZE - ICON_SIZE

    def move(self):
        if self.direction == 'LEFT':
            self.move_left()
        elif self.direction == 'RIGHT':
            self.move_right()

    # Moves icon 1 unit to left; stops moving once icon reaches right side
    def move_left(self):
        if self.rect.x < CHARACTER_SIZE:
            self.screen.currMoving = None 
            self.screen.refresh()
        else:
            self.screen.refresh()
            self.rect = self.rect.move([-3,0])
            self.screen.add_img(self.icon, self.rect)

    # Moves icon 1 unit to right; stops moving once icon reaches left side
    def move_right(self):
        if self.rect.right > self.screen.width - CHARACTER_SIZE:
            self.screen.currMoving = None
            self.screen.refresh()
        else:
            self.screen.refresh()
            self.rect = self.rect.move([3,0])
            self.screen.add_img(self.icon, self.rect)
