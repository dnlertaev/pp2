import pygame
import sys
import datetime

from datetime import datetime

weight, height = 600,600

screen = pygame.display.set_mode((weight, height))

pygame.display.set_caption("Mickey's clock")

mickeysclock = pygame.image.load("lab7/images/main-clock.png").convert_alpha()
mickeysclock = pygame.transform.scale(mickeysclock, (weight, height))
righthand = pygame.image.load("lab7/images/right-hand.png").convert_alpha()
lefthand = pygame.image.load("lab7/images/left-hand.png").convert_alpha()

clock_rect = mickeysclock.get_rect()
min_rect = righthand.get_rect()
sec_rect = lefthand.get_rect()

righthand_mask = pygame.mask.from_surface(righthand)
lefthand_mask = pygame.mask.from_surface(lefthand)

def our_clock():
    
    screen.fill((255, 255, 255))

    clock_x = (weight - clock_rect.width) // 2
    clock_y = (height - clock_rect.height) // 2

    screen.blit(mickeysclock, (clock_x, clock_y))

    time = datetime.now()

    sec_angle = (time.second / 60) * 360
    min_angle = ((time.minute + (time.second / 60)) / 60) * 360

    sec_angle = 90 - sec_angle
    min_angle = 90 - min_angle

    min_x = clock_x + clock_rect.width // 2 - min_rect.width // 2
    min_y = clock_y + clock_rect.height // 2 - min_rect.height // 2
    sec_x = clock_x + clock_rect.width // 2 - sec_rect.width // 2
    sec_y = clock_y + clock_rect.height // 2 - sec_rect.height // 2

    rotated_min = pygame.transform.rotate(righthand, min_angle)
    min_offset = (min_x + min_rect.width / 2 - rotated_min.get_rect().width / 2,
                  min_y + min_rect.height / 2 - rotated_min.get_rect().height / 2)
    screen.blit(rotated_min, min_offset)

    rotated_sec = pygame.transform.rotate(lefthand, sec_angle)
    sec_offset = (sec_x + sec_rect.width / 2 - rotated_sec.get_rect().width / 2,
                  sec_y + sec_rect.height / 2 - rotated_sec.get_rect().height / 2)
    screen.blit(rotated_sec, sec_offset)

    pygame.display.flip()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    our_clock()

pygame.quit()
sys.exit()