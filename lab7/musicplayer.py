import pygame
import os

pygame.init()

width, height = 700, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Music player")

background_image = pygame.image.load("lab7/images/player.png").convert()
background_image = pygame.transform.scale(background_image, (width, height))

music_files = [os.path.join("lab7/music", filename) for filename in os.listdir("lab7/music") if filename.endswith(".mp3")]
current_track = 0

def play_music():
    
    pygame.mixer.music.load(music_files[current_track])
    pygame.mixer.music.play()

def stop_music():
    
    pygame.mixer.music.stop()

def next_track():
    
    global current_track
    current_track = (current_track + 1) % len(music_files)
    play_music()

def previous_track():
    
    global current_track
    current_track = (current_track - 1) % len(music_files)
    play_music()

running = True

while running:
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_SPACE:
                
                if pygame.mixer.music.get_busy():
                    stop_music()
                else:
                    play_music()
            elif event.key == pygame.K_RIGHT:
                next_track()
            elif event.key == pygame.K_LEFT:
                previous_track()

    screen.blit(background_image, (0, 0))
    
    pygame.display.update()

pygame.quit()
