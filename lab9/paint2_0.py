import pygame  # Импорт библиотеки Pygame для создания графического интерфейса
import sys  # Импорт модуля sys для взаимодействия с системными функциями
import math  # Импорт модуля math для математических операций

# Инициализация Pygame
pygame.init()

# Определение размеров экрана
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
BG_COLOR = (255, 255, 255)  # Белый цвет для фона

# Создание экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Paint App")  # Заголовок окна приложения

# Определение цветов
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Определение форм
class Shape:
    def __init__(self):
        self.points = []

    def draw(self, surface):
        pass

# Определение квадрата
class Square(Shape):
    def draw(self, surface):
        if len(self.points) == 2:
            rect = pygame.Rect(self.points[0], self.points[1])
            pygame.draw.rect(surface, BLACK, rect, 2)

# Определение прямоугольного треугольника
class RightTriangle(Shape):
    def draw(self, surface):
        if len(self.points) == 2:
            rect = pygame.Rect(self.points[0], self.points[1])
            pygame.draw.polygon(surface, BLACK, [(rect.left, rect.bottom), (rect.right, rect.bottom), (rect.left, rect.top)], 2)

# Определение равностороннего треугольника
class EquilateralTriangle(Shape):
    def draw(self, surface):
        if len(self.points) == 2:
            x0, y0 = self.points[0]
            x1, y1 = self.points[1]
            width = abs(x1 - x0)
            height = abs(y1 - y0)
            pygame.draw.polygon(surface, BLACK, [(x0 + width // 2, y0), (x0, y1), (x1, y1)], 2)

# Определение ромба
class Rhombus(Shape):
    def draw(self, surface):
        if len(self.points) == 2:
            x0, y0 = self.points[0]
            x1, y1 = self.points[1]
            pygame.draw.polygon(surface, BLACK, [(x0 + (x1 - x0) // 2, y0), (x0, y0 + (y1 - y0) // 2), (x0 + (x1 - x0) // 2, y1), (x1, y0 + (y1 - y0) // 2)], 2)

# Определение свободной линии
class FreeLine(Shape):
    def draw(self, surface):
        if len(self.points) > 1:
            pygame.draw.lines(surface, BLACK, False, self.points, 2)

# Основная функция
def main():
    shapes = []  # Список для хранения всех нарисованных форм
    current_shape = None  # Текущая форма, которую пользователь рисует
    drawing = False  # Флаг, указывающий, идет ли рисование в данный момент
    running = True  # Флаг, указывающий, продолжается ли выполнение программы

    while running:
        for event in pygame.event.get():  # Обработка всех событий Pygame
            if event.type == pygame.QUIT:  # Если происходит выход из приложения
                running = False  # Установка флага "выход"
            elif event.type == pygame.MOUSEBUTTONDOWN:  # Если нажата кнопка мыши
                if event.button == 1:  # Если нажата левая кнопка мыши
                    if pygame.key.get_pressed()[pygame.K_s]:  # Если нажата клавиша 'S'
                        current_shape = Square()  # Создание нового квадрата
                    elif pygame.key.get_pressed()[pygame.K_r]:  # Если нажата клавиша 'R'
                        current_shape = RightTriangle()  # Создание нового прямоугольного треугольника
                    elif pygame.key.get_pressed()[pygame.K_e]:  # Если нажата клавиша 'E'
                        current_shape = EquilateralTriangle()  # Создание нового равностороннего треугольника
                    elif pygame.key.get_pressed()[pygame.K_h]:  # Если нажата клавиша 'H'
                        current_shape = Rhombus()  # Создание нового ромба
                    else:  # Если не нажата ни одна из специальных клавиш
                        drawing = True  # Установка флага "рисование" в True
                        current_shape = FreeLine()  # Создание новой свободной линии
                    shapes.append(current_shape)  # Добавление текущей формы в список форм
                    current_shape.points.append(event.pos)  # Добавление начальной точки рисования
            elif event.type == pygame.MOUSEBUTTONUP:  # Если кнопка мыши отпущена
                if event.button == 1:  # Если отпущена левая кнопка мыши
                    if not drawing:  # Если рисование завершено
                        current_shape.points.append(event.pos)  # Добавление конечной точки рисования
                    drawing = False  # Установка флага "рисование" в False
                    current_shape = None  # Обнуление текущей формы
            elif event.type == pygame.MOUSEMOTION:  # Если происходит движение мыши
                if drawing:  # Если идет рисование
                    current_shape.points.append(event.pos)  # Добавление точки рисования

        screen.fill(BG_COLOR)  # Заполнение экрана цветом фона

        # Отрисовка всех созданных форм
        for shape in shapes:
            shape.draw(screen)

        pygame.display.flip()  # Обновление экрана

    pygame.quit()  # Выход из Pygame
    sys.exit()  # Завершение программы

# Запуск основной функции, если программа запущена напрямую (а не импортирована)
if __name__ == "__main__":
    main()

# S - квадртаты
# R - треугольник