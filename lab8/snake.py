import pygame 
import sys
import time 
import random 
import math 

pygame.init()

width , height = 500 , 500 
cell_size = 10 

screen = pygame.display.set_mode((width , height))
pygame.display.set_caption('snake 2d')

#colours 
black = (0 , 0 , 0)
white = (255 , 255 , 255)
green = (0 , 255 , 0)
red = (255 , 0 , 0)
blue = (0 , 0 , 255)
violet = (139 , 0 , 255)
yellow = (255 , 255 , 0)

def random_position():
    x , y  = random.randint(20 , width - 20) , random.randint(20 , height - 20)
    if (x % 10 == 0) and (y % 10 == 0):
        return x , y 
    if (x == snake_pos[0] and y == snake_pos[1]):
        return random_position()
    return random_position()
    

#positions 
snake_pos = [100 , 100]
snake_body = [ [100 , 100] , [80 , 100] , [60 , 100]]
direction = 'RIGHT'
change_to = direction

#Фичи 
score = 0
hit_sound = pygame.mixer.Sound(r"c:\Users\Professional\Downloads\Roblox Death Sound - OOF  Sound Effect HD - HomeMadeSoundEffects (mp3cut.net).mp3")
level = 1 

fruits_x , fruits_y = random_position()

#speed 
speed = 5
clock = pygame.time.Clock()



running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                change_to = 'UP'
            elif event.key == pygame.K_DOWN and direction != "UP":
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != "RIGHT":
                change_to = 'RIGHT'
    direction = change_to

    if direction == 'UP':
        snake_pos[1] -= cell_size
    elif direction == 'DOWN':
        snake_pos[1] += cell_size
    elif direction == 'LEFT':
        snake_pos[0] -= cell_size
    elif direction == 'RIGHT':
        snake_pos[0] += cell_size
    
    snake_body.insert(0 , list(snake_pos))
    snake_body.pop()

    screen.fill(black)

    #for  tp  
    #if snake_pos[0] < 0 :
    #    snake_pos[0] = width - cell_size
    #elif snake_pos[0] >= width:
    #    snake_pos[0] = 0
    #elif snake_pos[1] < 0:
    #    snake_pos[1] = height - cell_size         
    #elif snake_pos[1] >= height:
    #    snake_pos[1] = 0

     #for level 
    if score < 5:
        level = 1
        speed = 10
    elif score < 10:
        level = 2
        speed = 15
    elif score < 18:
        level = 3
        speed = 25
    elif score < 40:
        level = 4
        speed = 50
    

    #fruits collecting
    if math.hypot(snake_pos[0] - fruits_x, snake_pos[1] - fruits_y) < cell_size // 2:
        
        score += 1
        fruits_x , fruits_y = random_position()
    
    font = pygame.font.Font(None , 20)
    text1 = font.render(f"Ur score {score}" , True , green)
    text2 = font.render(f"level: {level}" , True , yellow)
    screen.blit(text2 , (400 , 30)) 
    screen.blit(text1, (400, 20))

   


    #for wall 
    pygame.draw.rect(screen, blue, pygame.Rect(0, 0, width, cell_size))  
    pygame.draw.rect(screen, blue, pygame.Rect(0, 0, cell_size, height))  
    pygame.draw.rect(screen, blue, pygame.Rect(width - cell_size, 0, cell_size, height))  
    pygame.draw.rect(screen, blue, pygame.Rect(0, height - cell_size, width, cell_size))  
    
        
    if (snake_pos[0] <= 0 or snake_pos[0] >= width - cell_size or
        snake_pos[1] <= 0 or snake_pos[1] >= height - cell_size):
        hit_sound.play()
        lines = [
            "GAME OVER!!:(" ,
            f"u ended up with {score} score"
        ]
        for i , line in enumerate(lines):
            
            font = pygame.font.Font(None , 50)
            text = font.render(line , True , red )
            screen.blit(text , (width // 7  , height // 3 + i * 50))

        pygame.display.flip()
        pygame.time.delay(2000)
        running = False
    
    pygame.draw.circle(screen , violet , (fruits_x , fruits_y) , cell_size // 2)
    #print(f" fruit x: {fruits_x} , y:  {fruits_y}")
    #print(f" snake x : {snake_pos[0]} , y : {snake_pos[1]}")
    
    for block in snake_body:
        pygame.draw.rect(screen , green , pygame.Rect(block[0] , block[1] , cell_size , cell_size ))
    pygame.display.flip()
    clock.tick(speed)

pygame.quit()
sys.exit()