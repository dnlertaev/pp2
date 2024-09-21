import pygame  # Импорт библиотеки Pygame для создания графического интерфейса
import sys  # Импорт модуля sys для взаимодействия с системными функциями
import random  # Импорт модуля random для генерации случайных чисел
import time  # Импорт модуля time для управления временем выполнения
from pygame.locals import *  # Импорт констант Pygame для удобного доступа к ним

# Инициализация Pygame
pygame.init()

# Установка частоты кадров
FPS = 60
FramePerSec = pygame.time.Clock()

# Определение цветов
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Другие переменные в программе
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 3  # Начальная скорость спрайтов
SCORE = 0  # Начальное значение счета
COIN_SPEED_INCREASE_THRESHOLD = 5  # Порог для увеличения скорости после сбора монет
MAX_COINS = 1  # Максимальное количество монет на экране
ENEMY_COUNT = 1  # Максимальное количество вражеских машин на экране
COIN_SIZE_FACTOR = 8  # Уменьшение размера монеты в COIN_SIZE_FACTOR раз
SPEED_INCREMENT = 0.05  # Незначительное увеличение скорости после каждых 5 собранных монет

# Шрифты
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Фоновое изображение
background = pygame.image.load("lab8/images/AnimatedStreet.png")

# Экран
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

# Класс Enemy для создания вражеских машин
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("lab8/images/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        """Метод для перемещения вражеской машины"""
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Класс Player для создания машины игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("lab8/images/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        """Метод для перемещения машины игрока"""
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)
                
        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            # Если край экрана достигнут, завершаем игру
            time.sleep(0.5)
            DISPLAYSURF.fill(RED)
            DISPLAYSURF.blit(game_over, (30, 250))
            pygame.display.update()
            time.sleep(2)
            pygame.quit()
            sys.exit()

# Класс Coin для создания монет
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.original_image = pygame.image.load("lab9/images/coin.png")
        self.image = pygame.transform.scale(self.original_image, (self.original_image.get_width() // COIN_SIZE_FACTOR, self.original_image.get_height() // COIN_SIZE_FACTOR))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        """Метод для перемещения монеты"""
        global SCORE, SPEED
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Создание спрайтов
P1 = Player()

# Создание групп спрайтов
enemies = pygame.sprite.Group()
coins = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)

# Добавление нового события для увеличения скорости через определенный интервал
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Игровой цикл
while True:
    # Проверка всех событий, происходящих в игре
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5  # Увеличение скорости через определенный интервал
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0, 0))  # Отрисовка фонового изображения на экране
    scores = font_small.render("Score: " + str(SCORE), True, BLACK)  # Отображение счета на экране
    DISPLAYSURF.blit(scores, (10, 10))  # Отображение счета на экране

    # Перемещение и перерисовка всех спрайтов
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # Создание монет
    if len(coins) < MAX_COINS and random.randint(0, 100) < 2:
        coin = Coin()
        while pygame.sprite.spritecollideany(coin, enemies):
            coin.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        all_sprites.add(coin)
        coins.add(coin)

    # Обработка столкновения между игроком и монетой
    if pygame.sprite.spritecollideany(P1, coins):
        SCORE += 1
        coins.sprites()[0].kill()  # Удаление собранной монеты

    # Создание вражеских машин
    if len(enemies) < ENEMY_COUNT and random.randint(0, 100) < 2:
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)

    # Обработка столкновения между игроком и вражеской машиной
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

    # Отслеживание счетчика монет и увеличение скорости
    if SCORE % COIN_SPEED_INCREASE_THRESHOLD == 0 and SCORE != 0:
        SPEED += SPEED_INCREMENT  # Незначительное увеличение скорости

    pygame.display.update()
    FramePerSec.tick(FPS)  # Установка FPS игры
   
   #self.image = pygame.transform.rotate(self.image, 180)