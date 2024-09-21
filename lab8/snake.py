import pygame
import random

pygame.init()

# Цвета
WHITE = (255, 255, 255)
BLUE = (0, 128, 255)
RED = (255, 0, 0)

# Размеры экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Размеры блока
BLOCK_SIZE = 20
# Скорость движения змейки
SPEED = 5

# Создание экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Anaconda')

# Функция для отрисовки змейки
def draw_snake(snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, BLUE, [block[0], block[1], BLOCK_SIZE, BLOCK_SIZE])

# Функция для отрисовки цели
def draw_target(target_x, target_y):
    pygame.draw.rect(screen, RED, [target_x, target_y, BLOCK_SIZE, BLOCK_SIZE])

# Основной игровой цикл
def game_loop():
    # Начальные координаты змейки
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    x_change = 0
    y_change = 0

    # Список с координатами змейки
    snake_list = []
    # Начальная длина змейки
    length_of_snake = 1
    
    print(length_of_snake)

    # Координаты цели
    target_x = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    target_y = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE

    game_over = False

    while not game_over:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -BLOCK_SIZE
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = BLOCK_SIZE
                    x_change = 0

        x += x_change
        y += y_change

        # Проверка на выход за границы экрана
        if x >= SCREEN_WIDTH or x < 0 or y >= SCREEN_HEIGHT or y < 0:
            game_over = True

        screen.fill(WHITE)

        # Отрисовка цели
        draw_target(target_x, target_y)
        # Добавление головы змейки в список координат
        snake_head = [x, y]
        snake_list.append(snake_head)
        # Удаление лишних сегментов змейки, чтобы ее длина соответствовала переменной length_of_snake
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Отрисовка змейки
        draw_snake(snake_list)

        pygame.display.update()

        # Обработка съедания цели и увеличения длины змейки
        if x == target_x and y == target_y:
            target_x = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            target_y = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            length_of_snake += 1

        pygame.time.Clock().tick(SPEED)

    pygame.quit()
    quit()

# Запуск игрового цикла
game_loop()