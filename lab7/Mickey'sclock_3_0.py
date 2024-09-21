import pygame
import sys
import datetime

from datetime import datetime

# Установка размеров окна
weight, height = 600, 600
screen = pygame.display.set_mode((weight, height))

# Установка заголовка окна
pygame.display.set_caption("Mickey's clock")

# Загрузка изображения часов и их масштабирование
mickeysclock = pygame.image.load("lab7/images/main-clock.png").convert_alpha()
mickeysclock = pygame.transform.scale(mickeysclock, (weight, height))

# Загрузка изображений стрелок
righthand = pygame.image.load("lab7/images/right-hand.png").convert_alpha()
lefthand = pygame.image.load("lab7/images/left-hand.png").convert_alpha()

# Получение прямоугольников для каждого изображения
clock_rect = mickeysclock.get_rect()
min_rect = righthand.get_rect()
sec_rect = lefthand.get_rect()

# Создание масок для стрелок
righthand_mask = pygame.mask.from_surface(righthand)
lefthand_mask = pygame.mask.from_surface(lefthand)

# Функция для отображения часов
def our_clock():
    # Заполнение экрана белым цветом
    screen.fill((255, 255, 255))

    # Расчет координат для отображения часов по центру экрана
    clock_x = (weight - clock_rect.width) // 2
    clock_y = (height - clock_rect.height) // 2

    # Отображение изображения часов на экране
    screen.blit(mickeysclock, (clock_x, clock_y))

    # Получение текущего времени
    time = datetime.now()

    # Вычисление угла для секундной и минутной стрелок
    sec_angle = (time.second / 60) * 360
    min_angle = ((time.minute + (time.second / 60)) / 60) * 360

    # Корректировка углов для соответствия направлению стрелок на часах
    sec_angle = 90 - sec_angle
    min_angle = 90 - min_angle

    # Вычисление координат для отображения стрелок
    min_x = clock_x + clock_rect.width // 2 - min_rect.width // 2
    min_y = clock_y + clock_rect.height // 2 - min_rect.height // 2
    sec_x = clock_x + clock_rect.width // 2 - sec_rect.width // 2
    sec_y = clock_y + clock_rect.height // 2 - sec_rect.height // 2

    # Поворот и отображение минутной стрелки
    rotated_min = pygame.transform.rotate(righthand, min_angle)
    min_offset = (min_x + min_rect.width / 2 - rotated_min.get_rect().width / 2,
                  min_y + min_rect.height / 2 - rotated_min.get_rect().height / 2)
    screen.blit(rotated_min, min_offset)

    # Поворот и отображение секундной стрелки
    rotated_sec = pygame.transform.rotate(lefthand, sec_angle)
    sec_offset = (sec_x + sec_rect.width / 2 - rotated_sec.get_rect().width / 2,
                  sec_y + sec_rect.height / 2 - rotated_sec.get_rect().height / 2)
    screen.blit(rotated_sec, sec_offset)

    # Обновление экрана
    pygame.display.flip()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    our_clock()  # Вызов функции для отображения часов

pygame.quit()
sys.exit()
