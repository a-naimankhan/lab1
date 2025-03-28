import pygame 
import time 
from datetime import datetime
import math

pygame.init()
WIDTH , HEIGHT = 400 , 400
CENTER =( WIDTH // 2 , HEIGHT // 2)
screen = pygame.display.set_mode((WIDTH , HEIGHT))
clock = pygame.time.Clock()

background = pygame.image.load(r"C:\Users\Professional\Desktop\Python Labs\lab1\lab7\clock.png")
background = pygame.transform.scale(background , (WIDTH , HEIGHT))

sec_hand = pygame.image.load(r"C:\Users\Professional\Desktop\Python Labs\lab1\lab7\sec_hand.png")
sec_hand = pygame.transform.scale(sec_hand , (sec_hand.get_width() // 1.2 , sec_hand.get_height() // 1.2))
sec_hand_length = 120 

min_hand = pygame.image.load(r"C:\Users\Professional\Desktop\Python Labs\lab1\lab7\min_hand.png")
min_hand = pygame.transform.scale(min_hand , (min_hand.get_width() // 1.2 , min_hand.get_height() // 1.2))
min_hand_length = 90 

def rotate_hand(image , angle , center , length ):
    rotated_image = pygame.transform.rotate(image, -angle) 
    offset_x = math.sin(math.radians(angle)) * length
    offset_y = math.cos(math.radians(angle)) * length

    rotated_rect = rotated_image.get_rect(center=(center[0] + offset_x, center[1] - offset_y))
    
    return rotated_image , rotated_rect

running = True

while running:
    screen.blit(background , (0 , 0))
    now = datetime.now()
    second = now.second
    minute = now.minute
    
    print(f"second: {second}")
    print(f"min: {minute}")
    sec_angle = second * 6
    min_angle = minute * 6 +(second/60) * 6
    print(f"sec angle = {sec_angle}")
    print(f"min angle = {min_angle}")
    
    rotated_sec_hand , rotated_sec_rect = rotate_hand(sec_hand , sec_angle , CENTER , sec_hand_length)
    rotated_min_hand , rotated_min_rect = rotate_hand(min_hand , min_angle , CENTER , min_hand_length)

    pygame.draw.circle(screen , (0 ,0 , 0) , CENTER , 5)
    screen.blit(rotated_sec_hand , rotated_sec_rect)
    screen.blit(rotated_min_hand , rotated_min_rect)

    pygame.display.flip()
    clock.tick(1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit
