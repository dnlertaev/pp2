import pygame
import random

pygame.init()

WHITE = (255, 255, 255)
BLUE = (0, 128, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BLOCK_SIZE = 20
SPEED = 5

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Anaconda')

def draw_snake(snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, BLUE, [block[0], block[1], BLOCK_SIZE, BLOCK_SIZE])

def draw_target(target_x, target_y, is_big=False):
    if is_big:
        pygame.draw.rect(screen, GREEN, [target_x, target_y, BLOCK_SIZE * 3, BLOCK_SIZE * 3])
    else:
        pygame.draw.rect(screen, RED, [target_x, target_y, BLOCK_SIZE, BLOCK_SIZE])

def check_collision(x, y, target_x, target_y, is_big):
    if is_big:
        return target_x <= x < target_x + BLOCK_SIZE * 3 and target_y <= y < target_y + BLOCK_SIZE * 3
    else:
        return target_x == x and target_y == y

def game_loop():
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    x_change = 0
    y_change = 0

    snake_list = []
    length_of_snake = 1

    target_x = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    target_y = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE

    big_target_x = -100
    big_target_y = -100
    big_target_exists = False
    big_target_timer = 0
    big_target_duration = 7 * SPEED * 1000  # 7 seconds
    big_target_visible_time = 0

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

        if x >= SCREEN_WIDTH or x < 0 or y >= SCREEN_HEIGHT or y < 0:
            game_over = True

        screen.fill(WHITE)

        draw_target(target_x, target_y)
        if big_target_exists:
            draw_target(big_target_x, big_target_y, is_big=True)

        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        draw_snake(snake_list)

        pygame.display.update()

        if x == target_x and y == target_y:
            target_x = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            target_y = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            length_of_snake += 1

        if check_collision(x, y, big_target_x, big_target_y, big_target_exists):
            big_target_exists = False
            length_of_snake += 3

        if not big_target_exists:
            if pygame.time.get_ticks() - big_target_visible_time > big_target_duration:
                big_target_x = round(random.randrange(0, SCREEN_WIDTH - (BLOCK_SIZE * 3)) / BLOCK_SIZE) * BLOCK_SIZE
                big_target_y = round(random.randrange(0, SCREEN_HEIGHT - (BLOCK_SIZE * 3)) / BLOCK_SIZE) * BLOCK_SIZE
                big_target_exists = True
                big_target_timer = pygame.time.get_ticks()
                big_target_visible_time = pygame.time.get_ticks()

        pygame.time.Clock().tick(SPEED)

    pygame.quit()
    quit()

game_loop()
