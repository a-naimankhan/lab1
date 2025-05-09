import pygame 
import sys
import random
import time
from pygame.locals import *

pygame.init() 

#images 
enemy_image = r"C:\Users\Professional\Desktop\Python Labs\lab1\lab9\race\Enemy.png"
player_image = r"C:\Users\Professional\Desktop\Python Labs\lab1\lab9\race\Player.png"
background = pygame.image.load(r"C:\Users\Professional\Desktop\Python Labs\lab1\lab9\race\AnimatedStreet.png")
crash_sound = r"C:\Users\Professional\Desktop\Python Labs\lab1\lab9\race\crash.wav"
coin_image = pygame.image.load(r"C:\Users\Professional\Desktop\Python Labs\lab1\lab9\race\coin.png")
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
        
        if  self.rect.left > 0:
            if pressed_keys[K_LEFT] or pressed_keys[K_a]:
                self.rect.move_ip(-2 , 0)
        if self.rect.right < width:
            if pressed_keys[K_RIGHT] or pressed_keys[K_d]:
                self.rect.move_ip(2 , 0)

    def draw(self , surface):
        surface.blit(self.image , self.rect)

class Coin(pygame.sprite.Sprite):
    def __init__(self, x , y , width , height):
        super().__init__()
        self.image = pygame.transform.scale(coin_image , (width , height))
        self.rect = self.image.get_rect()
        self.rect.center = (x , y)

    def move(self):
        self.rect.move_ip(0,speed)
        if self.rect.bottom > height:
            self.reset()

    

    def reset(self):
        self.rect.center = (random.randint(30, 370), random.randint(50, 400))
        
        #random size for moneta
        size_index = random.randint(1, 3)
        if size_index == 1:
            self.image = pygame.transform.scale(coin_image, (30, 30)) 
        elif size_index == 2:
            self.image = pygame.transform.scale(coin_image, (50, 50))  
        elif size_index == 3:
            self.image = pygame.transform.scale(coin_image, (75, 75))  
        
        
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(30, 370), random.randint(50, 400))



    def draw(self , surface):
        surface.blit(self.image , self.rect)


#objects 
#object1 = pygame.Rect((20 , 50 )  , (50 , 100))
#object2 = pygame.Rect((10 , 10) , (100 , 100))

#print(object1.colliderect(object2)) пересакаются ли 
#print(object1.collidepoint(50, 75))  если точка 50 , 75 находится внутри обжект 1 

P1 = Player()
E1 = Enemy()


enemies = pygame.sprite.Group()
enemies.add(E1)


diffrent_coins = {
    1 : pygame.sprite.Group() , 
    2 : pygame.sprite.Group() ,
    3 : pygame.sprite.Group()
    }
index  = random.randint(1 , 3) 

if index == 1:
    coin = Coin(random.randint(30 , 370) , random.randint(40 , 500) ,30  , 30)
if index == 2:
    coin = Coin(random.randint(30 , 370) , random.randint(40 , 500)  , 50 , 50)
if index == 3: 
    coin = Coin(random.randint(30 , 370) , random.randint(40 , 500) , 100 , 100)



diffrent_coins[index].add(coin)


all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

for coin_group in diffrent_coins.values():
    all_sprites.add(coin_group)


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

   # чекаем что бы монета не заспавнилась внутри вражеской машины 
    for enemy in enemies:
        if enemy.rect.collidepoint(coin.rect.center):  
            coin.reset() 

    for group in diffrent_coins.values():
        for coin in group:
            if pygame.sprite.collide_rect(P1, coin):  #checkayuo если монета попадется игроку 
                if coin.rect.width == 30:
                    coins_collected += 5  
                elif coin.rect.width == 50:
                    coins_collected += 3  
                elif coin.rect.width == 75:
                    coins_collected += 1  
            
            
                coin.reset()
    
        

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

    