import pygame

def main():
    # Инициализация
    pygame.init()
    
    # Создание экрана
    screen = pygame.display.set_mode((640, 480))
    
    # Создание часов
    clock = pygame.time.Clock()
    
    # Начальные значения переменных
    radius = 15  # Радиус кисти
    mode = 'blue'  # Режим рисования (по умолчанию - синий цвет)
    points = []  # Список точек, по которым рисуется линия
    
    while True:
        
        # Получение состояния клавиш
        pressed = pygame.key.get_pressed()
        
        # Проверка удержания клавиш ALT и CTRL
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Завершение программы при закрытии окна
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return  # Завершение программы при нажатии Ctrl + W
                if event.key == pygame.K_F4 and alt_held:
                    return  # Завершение программы при нажатии Alt + F4
                if event.key == pygame.K_ESCAPE:
                    return  # Завершение программы при нажатии Esc
                
                # Обработка нажатий клавиш для выбора цвета
                if event.key == pygame.K_r:
                    mode = 'red'  # Выбор красного цвета
                elif event.key == pygame.K_g:
                    mode = 'green'  # Выбор зеленого цвета
                elif event.key == pygame.K_b:
                    mode = 'blue'  # Выбор синего цвета
                elif event.key == pygame.K_e:
                    mode = 'eraser'  # Режим ластика (белый цвет)
                elif event.key == pygame.K_c:
                    mode = 'color_select'  # Режим выбора цвета из палитры
                    
            # Обработка событий мыши
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    radius = min(200, radius + 1)  # Увеличение радиуса кисти (левая кнопка мыши)
                elif event.button == 3:
                    radius = max(1, radius - 1)  # Уменьшение радиуса кисти (правая кнопка мыши)
            
            # Обработка движения мыши
            if event.type == pygame.MOUSEMOTION:
                position = event.pos
                points = points + [position]  # Добавление новой точки в список
                points = points[-256:]  # Ограничение длины списка
                
        # Очистка экрана
        screen.fill((0, 0, 0))
  
        # Рисование линий между точками
        i = 0
        while i < len(points) - 1:
            if mode == 'eraser':
                drawLineBetween(screen, i, points[i], points[i + 1], radius, 'white')  # Ластик
            elif mode == 'color_select':
                pygame.draw.circle(screen, (255, 255, 255), points[i], radius)  # Рисование точки выбранного цвета
            else:
                drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)  # Рисование линии выбранным цветом
            i += 1
        
        # Обновление экрана
        pygame.display.flip()
        
        # Ограничение FPS
        clock.tick(60)

# Функция для рисования линии между двумя точками
def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    elif color_mode == 'eraser':
        color = (0, 0, 0)
    else:
        color = (255, 255, 255)  # Белый цвет по умолчанию
        
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

main()