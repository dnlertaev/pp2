import pygame
import os

pygame.init()

# Установка размеров окна
width, height = 700, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Music player")  # Установка заголовка окна

# Загрузка изображения фона и его масштабирование
background_image = pygame.image.load("lab7/images/player.png").convert()
background_image = pygame.transform.scale(background_image, (width, height))

# Создание списка путей к файлам музыки
music_files = [os.path.join("lab7/music", filename) for filename in os.listdir("lab7/music") if filename.endswith(".mp3")]
current_track = 0  # Индекс текущего трека

# Функция для проигрывания музыки
def play_music():
    pygame.mixer.music.load(music_files[current_track])
    pygame.mixer.music.play()

# Функция для остановки музыки
def stop_music():
    pygame.mixer.music.stop()

# Функция для переключения на следующий трек
def next_track():
    global current_track
    current_track = (current_track + 1) % len(music_files)
    play_music()

# Функция для переключения на предыдущий трек
def previous_track():
    global current_track
    current_track = (current_track - 1) % len(music_files)
    play_music()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Проверка на закрытие окна
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Пробел для паузы/воспроизведения музыки
                if pygame.mixer.music.get_busy():
                    stop_music()
                else:
                    play_music()
            elif event.key == pygame.K_RIGHT:  # Стрелка вправо для перехода к следующему треку
                next_track()
            elif event.key == pygame.K_LEFT:  # Стрелка влево для перехода к предыдущему треку
                previous_track()

    # Отображение фона
    screen.blit(background_image, (0, 0))
    pygame.display.update()

pygame.quit()
