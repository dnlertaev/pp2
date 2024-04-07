import pygame 
import random
import sys

pygame.init()

W, H = 1200, 800
FPS = 60

screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()
done = False
bg = (0, 0, 0)

# Начальный экран игры
start_font = pygame.font.SysFont('comicsansms', 60)
start_text = start_font.render('Press Space to Start', True, (255, 255, 255))
start_text_rect = start_text.get_rect()
start_text_rect.center = (W // 2, H // 2)

start = False

while not start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Начало игры при нажатии пробела
                start = True

    screen.fill(bg)
    screen.blit(start_text, start_text_rect)
    pygame.display.flip()
    clock.tick(FPS)
    
# Основной код игры начинается после начала игры
#paddle
paddleW = 150
paddleH = 25
paddleSpeed = 20
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)

#Ball
ballRadius = 20
ballSpeed = 6
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1

#Game score
game_score = 0
game_score_fonts = pygame.font.SysFont('comicsansms', 40)
game_score_rect = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0)).get_rect(center=(210, 20))

#Catching sound
collision_sound = pygame.mixer.Sound('lab9/audio/catch.mp3')

def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    if delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy

#block settings
block_list = [pygame.Rect(10 + 120 * i, 50 + 70 * j,
        100, 50) for i in range(10) for j in range (4)]
color_list = [(random.randrange(0, 255), 
    random.randrange(0, 255),  random.randrange(0, 255))
              for i in range(10) for j in range(4)] 

#Game over Screen
losefont = pygame.font.SysFont('comicsansms', 40)
losetext = losefont.render('Game Over', True, (255, 255, 255))
losetextRect = losetext.get_rect(center=(W // 2, H // 2))

#Win Screen
winfont = pygame.font.SysFont('comicsansms', 40)
wintext = winfont.render('You win yay', True, (0, 0, 0))
wintextRect = wintext.get_rect(center=(W // 2, H // 2))

def pause_menu():
    pause_font = pygame.font.SysFont('comicsansms', 60)
    pause_text = pause_font.render('Paused', True, (255, 255, 255))
    pause_text_rect = pause_text.get_rect(center=(W // 2, H // 2))

    screen.fill(bg)
    screen.blit(pause_text, pause_text_rect)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return  # Resume the game
                elif event.key == pygame.K_s:
                    settings_menu()  # Go to the settings menu

def settings_menu():
    paddle_speed_text = menu_font.render(f'Paddle Speed: {paddleSpeed}', True, (255, 255, 255))
    paddle_speed_rect = paddle_speed_text.get_rect(center=(W // 2, H // 2 - 100))

    ball_speed_text = menu_font.render(f'Ball Speed: {ballSpeed}', True, (255, 255, 255))
    ball_speed_rect = ball_speed_text.get_rect(center=(W // 2, H // 2))

    # Additional settings can be added here

    screen.fill(bg)
    screen.blit(paddle_speed_text, paddle_speed_rect)
    screen.blit(ball_speed_text, ball_speed_rect)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return  # Return to the game
                elif event.key == pygame.K_UP:
                    increase_paddle_speed()
                elif event.key == pygame.K_DOWN:
                    decrease_paddle_speed()
                elif event.key == pygame.K_LEFT:
                    decrease_ball_speed()
                elif event.key == pygame.K_RIGHT:
                    increase_ball_speed()

def increase_paddle_speed():
    global paddleSpeed
    paddleSpeed += 1

def decrease_paddle_speed():
    global paddleSpeed
    paddleSpeed -= 1
    if paddleSpeed < 0:
        paddleSpeed = 0

def increase_ball_speed():
    global ballSpeed
    ballSpeed += 1

def decrease_ball_speed():
    global ballSpeed
    ballSpeed -= 1
    if ballSpeed < 1:
        ballSpeed = 1

menu_font = pygame.font.SysFont('comicsansms', 60)

def main_menu():
    menu_text = menu_font.render('Main Menu', True, (255, 255, 255))
    menu_text_rect = menu_text.get_rect(center=(W // 2, H // 2 - 100))

    start_text = menu_font.render('Press Space to Start', True, (255, 255, 255))
    start_text_rect = start_text.get_rect(center=(W // 2, H // 2))

    settings_text = menu_font.render('Press S for Settings', True, (255, 255, 255))
    settings_text_rect = settings_text.get_rect(center=(W // 2, H // 2 + 100))

    screen.fill(bg)
    screen.blit(menu_text, menu_text_rect)
    screen.blit(start_text, start_text_rect)
    screen.blit(settings_text, settings_text_rect)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return  # Start the game
                elif event.key == pygame.K_s:
                    settings_menu()  # Go to the settings menu

main_menu()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pause_menu()

    screen.fill(bg)

    [pygame.draw.rect(screen, color_list[color], block) for color, block in enumerate(block_list)]
    pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)
    pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius)

    ball.x += ballSpeed * dx
    ball.y += ballSpeed * dy

    if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
        dx = -dx
    if ball.centery < ballRadius + 50: 
        dy = -dy
    if ball.colliderect(paddle) and dy > 0:
        dx, dy = detect_collision(dx, dy, ball, paddle)

    hitIndex = ball.collidelist(block_list)
    if hitIndex != -1:
        hitRect = block_list.pop(hitIndex)
        hitColor = color_list.pop(hitIndex)
        dx, dy = detect_collision(dx, dy, ball, hitRect)
        game_score += 1
        collision_sound.play()

    screen.blit(game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255)), game_score_rect)

    if ball.bottom > H:
        screen.fill((0, 0, 0))
        screen.blit(losetext, losetextRect)
    elif not len(block_list):
        screen.fill((255, 255, 255))
        screen.blit(wintext, wintextRect)

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddleSpeed
    if key[pygame.K_RIGHT] and paddle.right < W:
        paddle.right += paddleSpeed

    pygame.display.flip()
    clock.tick(FPS)