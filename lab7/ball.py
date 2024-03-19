import pygame
import sys

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Football")

background_image = pygame.image.load("lab7/images/football-field.jpg").convert()
background_image = pygame.transform.scale(background_image, (width, height))

ball_image = pygame.image.load("lab7/images/ball.png").convert_alpha()
ball_image = pygame.transform.scale(ball_image, (100, 100))

ball_rect = ball_image.get_rect(center=(width // 2, height // 2))
velocity = 20

running = True

while running:
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_UP:
                if ball_rect.top - velocity >= 0:
                    ball_rect.y -= velocity
            elif event.key == pygame.K_DOWN:                
                if ball_rect.bottom + velocity <= height:
                    ball_rect.y += velocity
                    
            elif event.key == pygame.K_LEFT:                
                if ball_rect.left - velocity >= 0:
                    ball_rect.x -= velocity
                    
            elif event.key == pygame.K_RIGHT:                
                if ball_rect.right + velocity <= width:
                    ball_rect.x += velocity

    screen.blit(background_image, (0, 0))

    screen.blit(ball_image, ball_rect)

    pygame.display.flip()

pygame.quit()
sys.exit()