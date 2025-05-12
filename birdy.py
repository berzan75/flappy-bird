import pygame
from pygame.locals import*
import random

pygame.init()
clock=pygame.time.Clock()
fps=60

WIDTH=864
HEIGHT=936

s=pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("flappy bird")

#defining font
font=pygame.font.Sysfont("Times New Roman ",60)
ground_scroll=0
scroll_speed=4
flying=False
game_over=False
pipegap=150
pipe_frequency=1500
score=0
pass_pipe= False

#load images
bg=pygame.image.load("bg.png")
ground=pygame.image.load("ground.png")
restart=pygame.image.load("restart.png")

def draw_text(text,color,font,x,y):
    image=font.render(text,True,color)
    s.blit(image,(x,y))

def reset_game():
    pass

class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("pipe.png")
        self.rect= self.image.get_rect()
        #position variable determines if the pipe is coming from the bottom or top
        #position 1 is from the top, -1 is from the bottom
        if pos ==1:
            self.image=pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft=[x,y-int(pipegap /2)]
        elif pos ==-1:
            self.rect.bottomright=[x,y +int(pipegap /2)]

    def update(self):
        self.rect.x -= scroll_speed
        if self.rect.right <0:
            self.kill()

 
class button():
    def __init__(self,x,y,image):
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
    def draw(self):
        action=False

        pos=pygame.mouse.get_pos()        
        
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1:
                action=True
        screen.blit(self.image,(self.rect.x, self.rect.y))
        return action
    