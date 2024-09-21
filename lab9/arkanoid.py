import pygame  # Импорт библиотеки Pygame для создания игры
import random  # Импорт модуля random для генерации случайных чисел
import sys  # Импорт модуля sys для взаимодействия с системой

pygame.init()  # Инициализация Pygame

# Размеры окна и параметры кадров
W, H = 1200, 800  # Ширина и высота окна
FPS = 60  # Количество кадров в секунду

# Создание экрана
screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)  # Создание окна с заданными размерами
clock = pygame.time.Clock()  # Создание объекта Clock для отслеживания времени
done = False  # Флаг для проверки окончания игры
bg = (0, 0, 0)  # Цвет фона (черный)

# Начальный экран игры
start_font = pygame.font.SysFont('comicsansms', 60)  # Создание объекта шрифта для начального экрана
start_text = start_font.render('Нажмите Пробел, чтобы начать', True, (255, 255, 255))  # Создание текста начального экрана
start_text_rect = start_text.get_rect()  # Получение прямоугольника, содержащего текст
start_text_rect.center = (W // 2, H // 2)  # Центрирование текста по центру окна

start = False  # Флаг для отслеживания начала игры

# Ожидание начала игры
while not start:
    for event in pygame.event.get():  # Получение событий из очереди событий
        if event.type == pygame.QUIT:  # Если произошло событие выхода из игры
            pygame.quit()  # Завершение работы Pygame
            quit()  # Завершение работы программы
        if event.type == pygame.KEYDOWN:  # Если была нажата клавиша
            if event.key == pygame.K_SPACE:  # Если нажата клавиша "Пробел"
                start = True  # Установка флага начала игры в True

    screen.fill(bg)  # Заполнение экрана цветом фона
    screen.blit(start_text, start_text_rect)  # Отображение текста начального экрана
    pygame.display.flip()  # Обновление экрана
    clock.tick(FPS)  # Ограничение частоты кадров

# Основной код игры начинается после начала игры

# Настройки ракетки
paddleW = 150  # Ширина ракетки
paddleH = 25  # Высота ракетки
paddleSpeed = 20  # Скорость перемещения ракетки
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)  # Создание объекта прямоугольника для ракетки

# Настройки мяча
ballRadius = 20  # Радиус мяча
ballSpeed = 6  # Скорость мяча
ball_rect = int(ballRadius * 2 ** 0.5)  # Ширина и высота мяча
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)  # Создание объекта прямоугольника для мяча
dx, dy = 1, -1  # Скорость и направление движения мяча

# Счет игры
game_score = 0  # Переменная для хранения счета игры
game_score_fonts = pygame.font.SysFont('comicsansms', 40)  # Создание объекта шрифта для отображения счета
game_score_rect = game_score_fonts.render(f'Ваш счет: {game_score}', True, (0, 0, 0)).get_rect(center=(210, 20))  # Создание текста счета

# Звук столкновения
collision_sound = pygame.mixer.Sound('lab9/audio/catch.mp3')  # Загрузка звукового файла

# Функция для обнаружения столкновений
def detect_collision(dx, dy, ball, rect):
    # Расчет расстояния между мячом и прямоугольником
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    # Определение направления движения мяча после столкновения с прямоугольником
    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    if delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy  # Возврат скорости и направления движения мяча

# Настройки блоков
block_list = [pygame.Rect(10 + 120 * i, 50 + 70 * j, 100, 50) for i in range(10) for j in range(4)]  # Создание списка прямоугольников для блоков
color_list = [(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)) for i in range(10) for j in range(4)]  # Создание списка цветов для блоков

# Экран проигрыша
losefont = pygame.font.SysFont('comicsansms', 40)  # Создание объекта шрифта для отображения текста проигрыша
losetext = losefont.render('Конец игры', True, (255, 255, 255))  # Создание текста проигрыша
losetextRect = losetext.get_rect(center=(W // 2, H // 2))  # Создание прямоугольника для текста проигрыша

# Экран победы
winfont = pygame.font.SysFont('comicsansms', 40)  # Создание объекта шрифта для отображения текста победы
wintext = winfont.render('Победа!', True, (0, 0, 0))  # Создание текста победы
wintextRect = wintext.get_rect(center=(W // 2, H // 2))  # Создание прямоугольника для текста победы

# Функция меню паузы
def pause_menu():
    pause_font = pygame.font.SysFont('comicsansms', 60)  # Создание объекта шрифта для отображения текста паузы
    pause_text = pause_font.render('Пауза', True, (255, 255, 255))  # Создание текста паузы
    pause_text_rect = pause_text.get_rect(center=(W // 2, H // 2))  # Создание прямоугольника для текста паузы

    screen.fill(bg)  # Заполнение экрана цветом фона
    screen.blit(pause_text, pause_text_rect)  # Отображение текста паузы
    pygame.display.flip()  # Обновление экрана

    while True:
        for event in pygame.event.get():  # Получение событий из очереди событий
            if event.type == pygame.QUIT:  # Если произошло событие выхода из игры
                pygame.quit()  # Завершение работы Pygame
                quit()  # Завершение работы программы
            if event.type == pygame.KEYDOWN:  # Если была нажата клавиша
                if event.key == pygame.K_SPACE:  # Если нажата клавиша "Пробел"
                    return  # Возврат к игре
                elif event.key == pygame.K_s:  # Если нажата клавиша "S"
                    settings_menu()  # Переход к меню настроек

# Функция меню настроек
def settings_menu():
    paddle_speed_text = menu_font.render(f'Скорость ракетки: {paddleSpeed}', True, (255, 255, 255))  # Создание текста скорости ракетки
    paddle_speed_rect = paddle_speed_text.get_rect(center=(W // 2, H // 2 - 100))  # Создание прямоугольника для текста скорости ракетки

    ball_speed_text = menu_font.render(f'Скорость мяча: {ballSpeed}', True, (255, 255, 255))  # Создание текста скорости мяча
    ball_speed_rect = ball_speed_text.get_rect(center=(W // 2, H // 2))  # Создание прямоугольника для текста скорости мяча

    # Дополнительные настройки могут быть добавлены здесь

    screen.fill(bg)  # Заполнение экрана цветом фона
    screen.blit(paddle_speed_text, paddle_speed_rect)  # Отображение текста скорости ракетки
    screen.blit(ball_speed_text, ball_speed_rect)  # Отображение текста скорости мяча
    pygame.display.flip()  # Обновление экрана

    while True:
        for event in pygame.event.get():  # Получение событий из очереди событий
            if event.type == pygame.QUIT:  # Если произошло событие выхода из игры
                pygame.quit()  # Завершение работы Pygame
                quit()  # Завершение работы программы
            if event.type == pygame.KEYDOWN:  # Если была нажата клавиша
                if event.key == pygame.K_ESCAPE:  # Если нажата клавиша "Esc"
                    return  # Возврат к игре
                elif event.key == pygame.K_UP:  # Если нажата клавиша "Вверх"
                    increase_paddle_speed()  # Увеличение скорости ракетки
                elif event.key == pygame.K_DOWN:  # Если нажата клавиша "Вниз"
                    decrease_paddle_speed()  # Уменьшение скорости ракетки
                elif event.key == pygame.K_LEFT:  # Если нажата клавиша "Влево"
                    decrease_ball_speed()  # Уменьшение скорости мяча
                elif event.key == pygame.K_RIGHT:  # Если нажата клавиша "Вправо"
                    increase_ball_speed()  # Увеличение скорости мяча

# Увеличение скорости ракетки
def increase_paddle_speed():
    global paddleSpeed  # Объявление глобальной переменной
    paddleSpeed += 1  # Увеличение скорости ракетки на 1

# Уменьшение скорости ракетки
def decrease_paddle_speed():
    global paddleSpeed  # Объявление глобальной переменной
    paddleSpeed -= 1  # Уменьшение скорости ракетки на 1
    if paddleSpeed < 0:  # Если скорость ракетки стала меньше 0
        paddleSpeed = 0  # Установка скорости ракетки в 0

# Увеличение скорости мяча
def increase_ball_speed():
    global ballSpeed  # Объявление глобальной переменной
    ballSpeed += 1  # Увеличение скорости мяча на 1

# Уменьшение скорости мяча
def decrease_ball_speed():
    global ballSpeed  # Объявление глобальной переменной
    ballSpeed -= 1  # Уменьшение скорости мяча на 1
    if ballSpeed < 1:  # Если скорость мяча стала меньше 1
        ballSpeed = 1  # Установка скорости мяча в 1

menu_font = pygame.font.SysFont('comicsansms', 60)  # Создание объекта шрифта для текста меню

# Главное меню
def main_menu():
    menu_text = menu_font.render('Главное меню', True, (255, 255, 255))  # Создание текста главного меню
    menu_text_rect = menu_text.get_rect(center=(W // 2, H // 2 - 100))  # Создание прямоугольника для текста главного меню

    start_text = menu_font.render('Нажмите Пробел, чтобы начать', True, (255, 255, 255))  # Создание текста начала игры
    start_text_rect = start_text.get_rect(center=(W // 2, H // 2))  # Создание прямоугольника для текста начала игры

    settings_text = menu_font.render('Нажмите S для настроек', True, (255, 255, 255))  # Создание текста настроек
    settings_text_rect = settings_text.get_rect(center=(W // 2, H // 2 + 100))  # Создание прямоугольника для текста настроек

    screen.fill(bg)  # Заполнение экрана цветом фона
    screen.blit(menu_text, menu_text_rect)  # Отображение текста главного меню
    screen.blit(start_text, start_text_rect)  # Отображение текста начала игры
    screen.blit(settings_text, settings_text_rect)  # Отображение текста настроек
    pygame.display.flip()  # Обновление экрана

    while True:
        for event in pygame.event.get():  # Получение событий из очереди событий
            if event.type == pygame.QUIT:  # Если произошло событие выхода из игры
                pygame.quit()  # Завершение работы Pygame
                quit()  # Завершение работы программы
            if event.type == pygame.KEYDOWN:  # Если была нажата клавиша
                if event.key == pygame.K_SPACE:  # Если нажата клавиша "Пробел"
                    return  # Начать игру
                elif event.key == pygame.K_s:  # Если нажата клавиша "S"
                    settings_menu()  # Переход к меню настроек

main_menu()  # Вызов функции главного меню

# Основной игровой цикл
while not done:
    for event in pygame.event.get():  # Получение событий из очереди событий
        if event.type == pygame.QUIT:  # Если произошло событие выхода из игры
            done = True  # Установка флага окончания игры в True

    keys = pygame.key.get_pressed()  # Получение состояния всех клавиш
    if keys[pygame.K_ESCAPE]:  # Если нажата клавиша "Esc"
        pause_menu()  # Открытие меню паузы

    screen.fill(bg)  # Заполнение экрана цветом фона

    # Отображение блоков, ракетки и мяча на экране
    [pygame.draw.rect(screen, color_list[color], block) for color, block in enumerate(block_list)]
    pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)
    pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius)

    ball.x += ballSpeed * dx  # Обновление позиции мяча по оси X
    ball.y += ballSpeed * dy  # Обновление позиции мяча по оси Y

    # Обработка столкновений мяча с границами экрана
    if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
        dx = -dx
    if ball.centery < ballRadius + 50:
        dy = -dy

    # Обработка столкновений мяча с ракеткой
    if ball.colliderect(paddle) and dy > 0:
        dy = -dy
        collision_sound.play() 
        
        
    # Обработка столкновений мяча с блоками
    for block in block_list:
        if ball.colliderect(block):
            block_list.remove(block)
            dy = -dy
            collision_sound.play()  # Воспроизведение звука столкновения
            game_score += 1  # Увеличение счета игры

    # Обновление текста счета игры
    game_score_rect = game_score_fonts.render(f'Ваш счет: {game_score}', True, (0, 0, 0)).get_rect(center=(210, 20))
    
    
  
    if len(block_list) == 0:  # Если все блоки сломаны
        screen.fill((255, 255, 255))  # Заполнение экрана белым цветом
        screen.blit(wintext, wintextRect)  # Отображение текста победы
        pygame.display.flip()  # Обновление экрана
        pygame.time.delay(3000)  # Задержка перед завершением игры
        done = True  # Установка флага окончания игры в True

    if ball.bottom > H:  # Если мяч коснулся нижней границы окна
        screen.fill((255, 255, 255))  # Заполнение экрана белым цветом
        screen.blit(losetext, losetextRect)  # Отображение текста проигрыша
        pygame.display.flip()  # Обновление экрана
        pygame.time.delay(3000)  # Задержка перед завершением игры
        done = True  # Установка флага окончания игры в True

    # Проверка и обработка нажатий клавиш
    keys = pygame.key.get_pressed()  # Получение состояния всех клавиш
    if keys[pygame.K_LEFT] and paddle.left > 0:  # Если нажата клавиша "Влево" и ракетка не касается левой границы окна
        paddle.x -= paddleSpeed  # Сдвиг ракетки влево
    if keys[pygame.K_RIGHT] and paddle.right < W:  # Если нажата клавиша "Вправо" и ракетка не касается правой границы окна
        paddle.x += paddleSpeed  # Сдвиг ракетки вправо

    pygame.display.flip()  # Обновление экрана
    clock.tick(FPS)  # Ограничение частоты кадров

#    if game_score >= 10:  # Если счет достиг 10
#       ballSpeed += 0.007  # Увеличиваем скорость мяча