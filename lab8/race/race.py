import pygame 
import sys
import random
import time
from pygame.locals import *

pygame.init() 

#images 
enemy_image = r"C:\Users\Professional\Desktop\Python Labs\lab1\lab8\race\Enemy.png"
player_image = r"C:\Users\Professional\Desktop\Python Labs\lab1\lab8\race\Player.png"
background = pygame.image.load(r"C:\Users\Professional\Desktop\Python Labs\lab1\lab8\race\AnimatedStreet.png")
crash_sound = r"C:\Users\Professional\Desktop\Python Labs\lab1\lab8\race\crash.wav"
coin_image = pygame.image.load(r"C:\Users\Professional\Desktop\Python Labs\lab1\lab8\race\coin.png")
crash = pygame.mixer.Sound(crash_sound)

#color 
black =(0 , 0 , 0)
white = (255 , 255 ,255)
Gray = (128 , 128 , 128)
Red = (255 , 0 , 0)

#fps 
FPS = pygame.time.Clock()


#экран
width , height = 400 , 600
speed = 2
score = 0
coins_collected = 0

#fonts 
font = pygame.font.SysFont("Verdana" , 60)
font_small = pygame.font.SysFont("Verdana" , 20)
game_over = font.render("GAME OVER " , True , black)

#screen parametrs
display = pygame.display.set_mode((width , height))
display.fill(white)
pygame.display.set_caption("Race")


    

def appear_coins():
    coin_x , coin_y = (random.randint(30 , 370) , 250)
    if coin_x % 10 != 0:
        appear_coins()
    
        

class Enemy(pygame.sprite.Sprite):
    def __init__(self, ):
        super().__init__()
        self.image = pygame.image.load(enemy_image)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40 , width - 40) , 0)

    def move(self):
        global score 
        self.rect.move_ip(0,speed)
        if (self.rect.bottom > height):
            self.rect.top = 0
            self.rect.center = (random.randint(30 , 370) , 0)
            score += 1

    def draw(self , surface):
        surface.blit(self.image , self.rect)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(player_image)
        self.rect = self.image.get_rect()
        self.rect.center = (160 , 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)
       #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0,5)

        if  self.rect.left > 0:
            if pressed_keys[K_LEFT] or pressed_keys[K_a]:
                self.rect.move_ip(-5 , 0)
        if self.rect.right < width:
            if pressed_keys[K_RIGHT] or pressed_keys[K_d]:
                self.rect.move_ip(5 , 0)

    def draw(self , surface):
        surface.blit(self.image , self.rect)

class Coin(pygame.sprite.Sprite):
    def __init__(self,):
        super().__init__()
        self.image = pygame.transform.scale(coin_image , (30 , 30))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(30 , 370) , random.randint(50 ,400))

    def move(self):
        self.rect.move_ip(0,speed)
        if self.rect.bottom > height:
            self.reset()

    def reset(self):
    while True:
        new_x = random.randint(30, 370)
        new_y = random.randint(50, 400)
        self.rect.center = (new_x, new_y)

        # Проверка на пересечение с игроком
        if not self.rect.colliderect(P1.rect):
            break


    

    def draw(self , surface):
        surface.blit(self.image , self.rect)


#objects 
#object1 = pygame.Rect((20 , 50 )  , (50 , 100))
#object2 = pygame.Rect((10 , 10) , (100 , 100))

#print(object1.colliderect(object2)) пересакаются ли 
#print(object1.collidepoint(50, 75))  если точка 50 , 75 находится внутри обжект 1 

P1 = Player()
E1 = Enemy()
C1 = Coin()

enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(C1) 

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)


INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED ,  1000)


while True:

    for event in pygame.event.get():
        if event.type == INC_SPEED:
            speed += 0.125

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    display.blit(background  , (0 , 0))
    scores = font_small.render(f"score : {score}" , True , black)
    display.blit(scores , (10 , 10))
    coins_text = font_small.render(f"coins : {coins_collected} " , True , black)
    display.blit(coins_text , (10 , 30) )


    for entity in all_sprites:
        display.blit(entity.image , entity.rect)
        entity.move()

    if pygame.sprite.spritecollideany(P1 , coins):
        coins_collected += 1
        C1.reset()

    
        

    if pygame.sprite.spritecollideany(P1 , enemies):
        pygame.mixer.Sound(crash).play()
        time.sleep(0.5)

        display.fill(Red)
        display.blit(game_over , (30 , 250))

        pygame.display.update()

        for entity  in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    FPS.tick()

    