import pygame  # Импорт библиотеки Pygame
import random  # Импорт модуля random для генерации случайных чисел

pygame.init()  # Инициализация Pygame

WHITE = (255, 255, 255)  # Определение цвета белого в формате RGB
BLUE = (0, 128, 255)  # Определение цвета синего в формате RGB
RED = (255, 0, 0)  # Определение цвета красного в формате RGB
GREEN = (0, 255, 0)  # Определение цвета зеленого в формате RGB

SCREEN_WIDTH = 800  # Определение ширины экрана
SCREEN_HEIGHT = 600  # Определение высоты экрана

BLOCK_SIZE = 20  # Определение размера блока
SPEED = 5  # Определение скорости игры

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Создание экрана для отображения игры
pygame.display.set_caption('Anaconda')  # Установка заголовка окна игры

def draw_snake(snake_list):  # Функция отрисовки змеи на экране
    for block in snake_list:
        pygame.draw.rect(screen, BLUE, [block[0], block[1], BLOCK_SIZE, BLOCK_SIZE])

def draw_target(target_x, target_y, is_big=False):  # Функция отрисовки целей на экране
    if is_big:
        pygame.draw.rect(screen, GREEN, [target_x, target_y, BLOCK_SIZE * 3, BLOCK_SIZE * 3])  # Отрисовка большой цели
    else:
        pygame.draw.rect(screen, RED, [target_x, target_y, BLOCK_SIZE, BLOCK_SIZE])  # Отрисовка маленькой цели

def check_collision(x, y, target_x, target_y, is_big):  # Функция проверки столкновений между объектами
    if is_big:  # Если проверяется столкновение с большой целью
        return target_x <= x < target_x + BLOCK_SIZE * 3 and target_y <= y < target_y + BLOCK_SIZE * 3
    else:  # Если проверяется столкновение с маленькой целью
        return target_x == x and target_y == y

def game_loop():  # Основная функция игрового цикла
    x = SCREEN_WIDTH / 2  # Начальная координата X для змеи
    y = SCREEN_HEIGHT / 2  # Начальная координата Y для змеи
    x_change = 0  # Изменение координаты X для движения змеи
    y_change = 0  # Изменение координаты Y для движения змеи

    snake_list = []  # Список для хранения координат блоков змеи
    length_of_snake = 1  # Начальная длина змеи

    target_x = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE  # Координата X для цели
    target_y = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE  # Координата Y для цели

    big_target_x = -100  # Начальная координата X для большой цели
    big_target_y = -100  # Начальная координата Y для большой цели
    big_target_exists = False  # Флаг, указывающий, существует ли большая цель
    big_target_timer = 0  # Таймер для отображения большой цели
    big_target_duration = 7 * SPEED * 1000  # Продолжительность отображения большой цели (7 секунд)
    big_target_visible_time = 0  # Время последнего отображения большой цели

    game_over = False  # Флаг, указывающий на окончание игры

    while not game_over:  # Главный игровой цикл
        
        for event in pygame.event.get():  # Обработка событий
            
            if event.type == pygame.QUIT:  # Если событие - выход из игры
                game_over = True
            elif event.type == pygame.KEYDOWN:  # Если событие - нажатие клавиши
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

        x += x_change  # Обновление координаты X змеи
        y += y_change  # Обновление координаты Y змеи

        if x >= SCREEN_WIDTH or x < 0 or y >= SCREEN_HEIGHT or y < 0:  # Если змея столкнулась с границами экрана
            game_over = True

        screen.fill(WHITE)  # Заполнение экрана белым цветом

        draw_target(target_x, target_y)  # Отрисовка цели
        if big_target_exists:  # Если существует большая цель
            draw_target(big_target_x, big_target_y, is_big=True)  # Отрисовка большой цели

        snake_head = [x, y]
        snake_list.append(snake_head)  # Добавление головы змеи в список координат
        if len(snake_list) > length_of_snake:
            del snake_list[0]  # Удаление последнего блока змеи, если ее длина больше, чем нужно

        draw_snake(snake_list)  # Отрисовка змеи на экране

        pygame.display.update()  # Обновление экрана

        if x == target_x and y == target_y:  # Если змея достигла маленькой цели
            target_x = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            target_y = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            length_of_snake += 1  # Увеличение длины змеи

        if check_collision(x, y, big_target_x, big_target_y, big_target_exists):  # Если змея столкнулась с большой целью
            big_target_exists = False
            length_of_snake += 3  # Увеличение длины змеи на 3 блока

        if not big_target_exists:  # Если большая цель не существует
            if pygame.time.get_ticks() - big_target_visible_time > big_target_duration:  # Если прошло достаточно времени с момента последнего отображения большой цели
                big_target_x = round(random.randrange(0, SCREEN_WIDTH - (BLOCK_SIZE * 3)) / BLOCK_SIZE) * BLOCK_SIZE
                big_target_y = round(random.randrange(0, SCREEN_HEIGHT - (BLOCK_SIZE * 3)) / BLOCK_SIZE) * BLOCK_SIZE
                big_target_exists = True  # Установка флага существования большой цели
                big_target_timer = pygame.time.get_ticks()  # Запись времени отображения большой цели
                big_target_visible_time = pygame.time.get_ticks()

        pygame.time.Clock().tick(SPEED)  # Установка скорости обновления экрана

    pygame.quit()  # Завершение работы Pygame
    quit()  # Завершение работы программы

game_loop()  # Запуск игрового цикла
