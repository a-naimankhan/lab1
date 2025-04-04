import pygame 
import sys
import math

pygame.init()

width , height = 800 , 600
screen = pygame.display.set_mode((width , height))
pygame.display.set_caption('simple PAINT')

black = (0 , 0 , 0)
white = (255 , 255 ,255)
green = (0 , 255 , 0)
red = (255,  0 , 0)
blue = (0 , 0 , 255)
gray = (200 , 200 , 200)

class Button:
    def __init__(self , x , y , width , height , text , color , action):
        self.rect = pygame.Rect(x,y , width , height)
        self.text = text
        self.color = color 
        self.action = action

    def draw(self , screen):
        pygame.draw.rect(screen , self.color , self.rect)
        font = pygame.font.Font(None , 30)
        text_surface = font.render(self.text , True , white)
        screen.blit(text_surface , (self.rect.x + 12 , self.rect.y + 12))

    def check_action(self , event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.action()

mode = 'brush'
drawing = False
brush_color = black
drawing_circle = False
circle_start = None 
curent_radius = 0

def set_black():
    global brush_color 
    brush_color = black

def set_white():
    global brush_color 
    brush_color = white

def set_green():
    global brush_color 
    brush_color = green
 
def set_red():
    global brush_color 
    brush_color = red

def set_blue():
    global brush_color 
    brush_color = blue

def clear_screen():
    screen.fill(white)

def set_circle_mode():
    global mode 
    mode = 'circle'

def set_rect_mode():
    global mode
    mode = 'rect'

    
def eraser():
    global brush_color 
    brush_color = white 

def exit_app():
    pygame.quit()
    sys.exit()

    

buttons = [
    Button(10 , 10 , 60 , 30 , 'Black' , black , set_black),
    
    Button(80 , 10 , 60 , 30 , 'Green' , green , set_green),
    
    Button(159 , 10 , 60 , 30 , 'Red' , red , set_red),
    
    Button(220 , 10 , 60 , 30 , 'Blue' , blue , set_blue),

    Button(290 , 10 , 60 , 30 , 'Eraser' , gray , eraser),

    Button(370 , 10 , 60 , 30 , 'Clear' , gray , clear_screen) , 
    
    Button(460 , 10 , 60 , 30 , 'Exit' , gray , exit_app) ,
    
    Button(550 , 10 , 60 , 30 , 'Circle' , gray , set_circle_mode) ,

    Button(620 , 10 , 60 , 30 , 'Rectangle' , gray , set_rect_mode)
    

]

clear_screen()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mode in ['circle' , 'rect']:
                circle_start = event.pos
            drawing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if mode == 'circle' and circle_start:
                end = event.pos
                radius = int(math.hypot(end[0] - circle_start[0] , end[1] - circle_start[1]))
                pygame.draw.circle(screen , brush_color , circle_start , radius , 2)
                circle_start = None
            elif mode == 'rect' and circle_start:
                end = event.pos
                x= min(circle_start[0] , end[0])
                y = min(circle_start[1] , end[1])
                w = abs(end[0] - circle_start[0])
                h = abs(end[1] - circle_start[1])
                pygame.draw.rect(screen , brush_color , (x , y , w , h) ,2)
                circle_start = None
            if event.button == 1:
                drawing  = False
                if drawing_circle:
                    drawing_circle = False

        elif event.type == pygame.MOUSEMOTION and drawing and mode == 'brush':
            mouse_x , mouse_y = event.pos
            pygame.draw.circle(screen , brush_color , (mouse_x , mouse_y) , 5)
        
        for button in buttons:
            button.check_action(event)

    if drawing and mode == 'brush':
        mouse_x , mouse_y = pygame.mouse.get_pos()
        if mouse_y > 50:
            pygame.draw.circle(screen , brush_color , (mouse_x , mouse_y) , 5)
    
    if drawing_circle and circle_start:
        mouse_x , mouse_y = pygame.mouse.get_pos()
        curent_radius = int(math.hypot(mouse_x - circle_start[0] , mouse_y - circle_start[1]))
        pygame.draw.circle(screen , brush_color , circle_start , curent_radius , 2)

    pygame.draw.rect(screen , gray , (0 , 0 , width , 50))
    for button in buttons:
        button.draw(screen)

    pygame.display.flip()
        