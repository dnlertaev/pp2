import pygame
import sys
import random
import time
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set the frame rate
FPS = 60
FramePerSec = pygame.time.Clock()

# Colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Other variables in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 3  # Initial speed of sprites
SCORE = 0  # Initial score value
COIN_SPEED_INCREASE_THRESHOLD = 5  # Threshold for speed increase after collecting coins
MAX_COINS = 2  # Maximum number of coins on screen
ENEMY_COUNT = 2  # Maximum number of enemy cars on screen
COIN_SIZE_FACTOR = 4  # Reduce coin size by a factor of 4
SPEED_INCREMENT = 0.1  # Minor speed increase after every 5 collected coins

# Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Background image
background = pygame.image.load("lab8/images/AnimatedStreet.png")

# Screen
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


class Enemy(pygame.sprite.Sprite):
    """Class to create enemy cars"""
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("lab8/images/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        """Method to move the enemy car"""
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    """Class to create the player's car"""
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("lab8/images/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        """Method to move the player's car"""
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)


class Coin(pygame.sprite.Sprite):
    """Class to create coins"""
    def __init__(self):
        super().__init__()
        self.original_image = pygame.image.load("lab9/images/coin.png")
        self.image = pygame.transform.scale(self.original_image, (self.original_image.get_width() // COIN_SIZE_FACTOR, self.original_image.get_height() // COIN_SIZE_FACTOR))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        """Method to move the coin"""
        global SCORE, SPEED
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


# Set sprites
P1 = Player()

# Create sprite groups
enemies = pygame.sprite.Group()
coins = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)

# Add a new event for speed increase at a certain interval
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Game loop
while True:
    # Check all events happening in the game
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5  # Increase speed at certain interval
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0, 0))  # Draw background image on screen
    scores = font_small.render("Score: " + str(SCORE), True, BLACK)  # Show score on screen
    DISPLAYSURF.blit(scores, (10, 10))  # Show score on screen

    # Move and redraw all sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # Create coins
    if len(coins) < MAX_COINS and random.randint(0, 100) < 2:
        coin = Coin()
        while pygame.sprite.spritecollideany(coin, enemies):
            coin.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        all_sprites.add(coin)
        coins.add(coin)

    # Handle collision between player and coin
    if pygame.sprite.spritecollideany(P1, coins):
        SCORE += 1
        coins.sprites()[0].kill()  # Remove collected coin

    # Create enemy cars
    if len(enemies) < ENEMY_COUNT and random.randint(0, 100) < 2:
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)

    # Handle collision between player and enemy car
    if pygame.sprite.spritecollideany(P1, enemies):
        time.sleep(0.5)
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Track coin counter and increase speed
    if SCORE % COIN_SPEED_INCREASE_THRESHOLD == 0 and SCORE != 0:
        SPEED += SPEED_INCREMENT  # Minor speed increase

    pygame.display.update()
    FramePerSec.tick(FPS)  # Set game FPS
