import pygame 

pygame.init()
Width , Height = 500 , 500 
screen = pygame.display.set_mode((Width , Height))
pygame.display.set_caption('music player')



music = (r"C:\Users\Professional\Desktop\Python Labs\lab1\lab7\Toky ghoul.mp3")
pygame.mixer.init()
pygame.mixer.music.load(music)
pygame.mixer.music.play()

volume = 0.5
pygame.mixer.music.set_volume(volume)


def play_pause():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()

def stop():
    pygame.mixer.music.stop()

def restart():
    pygame.mixer.music.stop()
    pygame.mixer.music.play()

def change_volume(delta):
    global volume
    volume = max(0.0 , min(1.0 , volume+delta))
    pygame.mixer.music.set_volume(volume)


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                play_pause()
            elif event.key == pygame.K_s:
                stop() 
            elif event.key == pygame.K_r:
                restart()
            elif event.key == pygame.K_UP:
                change_volume(0.1)
            elif event.key == pygame.K_DOWN:
                change_volume(-0.1)
        
pygame.quit()