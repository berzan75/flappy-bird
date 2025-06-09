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
white= (255,255,255)
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

 
class Button():
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
        s.blit(self.image,(self.rect.x, self.rect.y))
        return action

class Bird(pygame.sprite.Sprite ):
    def __init__(self, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images=[]
        self.index=0
        self.counter=0
        for i in range (1,3):
            img=pygame.image.load(f"bird{i}.png")
            self.images.append(img)
        self.image=self.images[self.index]
        self.rect= self.image.get_rect()
        self.rect.center=[x,y]
        self.vel=0
        self.clicked=False

    def update(self):
        if flying==True:
            self.vel+=0.5
            if self.vel > 8:
                self.vel=8
            if self.rect.bottom < 768:
                self.rect.y += int(self.vel)
        
        if game_over == False:
            if pygame.mouse.get_pressed()[0]==1 and self.clicked==False:
                self.clicked=True
                self.vel=-10
            if pygame.mouse.get_pressed()[0]==0:
                self.clicked=False
            flap_cooldown=5
            self_counter+=1

            if self.counter > flap_cooldown:
                self_counter=0
                self.index+=1
                if self.index > len (self.images):
                    self.index=0
                self.image=self.images[self.index]
            
            #rotate the bird
            self.image =pygame.transform.rotate(self.images[self.index],self.vel *2)
        else:
            self.image =pygame.transform.rotate(self.images[self.index],-90)

                

pipe_group = pygame.sprite.Group()
bird_group = pygame.sprite.Group()

flappy=Bird(100, int (HEIGHT /2))

bird_group.add(flappy)

button= Button(int (WIDTH /2), int (HEIGHT/ 2),restart)

while True:
    clock.tick(fps)

    pipe_group.draw(s)
    bird_group.draw(s)
    bird_group.update()

    s.blit(ground,(ground_scroll,768))
    if len(pipe_group)>0:
        if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left and bird_group.sprites()[0].rect.right < pipe_group.sprites(0).rect.right\
            and pass_pipe == False:
                pass_pipe = True
        if pass_pipe == True:
            if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:
                pass_pipe = False
                score +=1
    draw_text(str(score),font,white,500 ,10)
