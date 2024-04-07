import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
BG_COLOR = (255, 255, 255)  # White

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Paint App")

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Shapes
class Shape:
    def __init__(self):
        self.points = []

    def draw(self, surface):
        pass

class Square(Shape):
    def draw(self, surface):
        if len(self.points) == 2:
            rect = pygame.Rect(self.points[0], self.points[1])
            pygame.draw.rect(surface, BLACK, rect, 2)

class RightTriangle(Shape):
    def draw(self, surface):
        if len(self.points) == 2:
            rect = pygame.Rect(self.points[0], self.points[1])
            pygame.draw.polygon(surface, BLACK, [(rect.left, rect.bottom), (rect.right, rect.bottom), (rect.left, rect.top)], 2)

class EquilateralTriangle(Shape):
    def draw(self, surface):
        if len(self.points) == 2:
            x0, y0 = self.points[0]
            x1, y1 = self.points[1]
            width = abs(x1 - x0)
            height = abs(y1 - y0)
            pygame.draw.polygon(surface, BLACK, [(x0 + width // 2, y0), (x0, y1), (x1, y1)], 2)

class Rhombus(Shape):
    def draw(self, surface):
        if len(self.points) == 2:
            x0, y0 = self.points[0]
            x1, y1 = self.points[1]
            pygame.draw.polygon(surface, BLACK, [(x0 + (x1 - x0) // 2, y0), (x0, y0 + (y1 - y0) // 2), (x0 + (x1 - x0) // 2, y1), (x1, y0 + (y1 - y0) // 2)], 2)

class FreeLine(Shape):
    def draw(self, surface):
        if len(self.points) > 1:
            pygame.draw.lines(surface, BLACK, False, self.points, 2)

# Main function
def main():
    shapes = []
    current_shape = None
    drawing = False
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    if pygame.key.get_pressed()[pygame.K_s]:  # Draw square
                        current_shape = Square()
                    elif pygame.key.get_pressed()[pygame.K_r]:  # Draw right triangle
                        current_shape = RightTriangle()
                    elif pygame.key.get_pressed()[pygame.K_e]:  # Draw equilateral triangle
                        current_shape = EquilateralTriangle()
                    elif pygame.key.get_pressed()[pygame.K_h]:  # Draw rhombus
                        current_shape = Rhombus()
                    else:  # Draw free line by default
                        drawing = True
                        current_shape = FreeLine()
                    shapes.append(current_shape)
                    current_shape.points.append(event.pos)
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # Left mouse button
                    if not drawing:
                        current_shape.points.append(event.pos)
                    drawing = False
                    current_shape = None
            elif event.type == pygame.MOUSEMOTION:
                if drawing:
                    current_shape.points.append(event.pos)

        screen.fill(BG_COLOR)

        # Draw shapes
        for shape in shapes:
            shape.draw(screen)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()