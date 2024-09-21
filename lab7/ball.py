import pygame
import sys

# Инициализация Pygame
pygame.init()

# Установка размеров окна
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Football")  # Установка заголовка окна

# Загрузка изображения футбольного поля и его масштабирование
background_image = pygame.image.load("lab7/images/football-field.jpg").convert()
background_image = pygame.transform.scale(background_image, (width, height))

# Загрузка изображения мяча и его масштабирование
ball_image = pygame.image.load("lab7/images/ball.png").convert_alpha()
ball_image = pygame.transform.scale(ball_image, (100, 100))

# Получение прямоугольника, содержащего мяч, и его центрирование в окне
ball_rect = ball_image.get_rect(center=(width // 2, height // 2))

# Установка скорости перемещения мяча
velocity = 20

running = True

while running:
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:  # Проверка на закрытие окна
            running = False
            
        elif event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_UP:  # Проверка на нажатие клавиши "Вверх"
                if ball_rect.top - velocity >= 0:
                    ball_rect.y -= velocity
            elif event.key == pygame.K_DOWN:  # Проверка на нажатие клавиши "Вниз"
                if ball_rect.bottom + velocity <= height:
                    ball_rect.y += velocity
            elif event.key == pygame.K_LEFT:  # Проверка на нажатие клавиши "Влево"
                if ball_rect.left - velocity >= 0:
                    ball_rect.x -= velocity
            elif event.key == pygame.K_RIGHT:  # Проверка на нажатие клавиши "Вправо"
                if ball_rect.right + velocity <= width:
                    ball_rect.x += velocity

    # Отображение фонового изображения на экране
    screen.blit(background_image, (0, 0))

    # Отображение изображения мяча на экране с учетом его прямоугольника
    screen.blit(ball_image, ball_rect)

    pygame.display.flip()  # Обновление экрана

# Выход из игрового цикла
pygame.quit()
sys.exit()
