import pygame
from random import randint
#CLASSE PER I MOSTRI
VelAvanza=7
gravità=0 

class mob:
    global keys ,gravità
    def __init__(self, screen):
        self.screen=screen
        self.mob_x=randint(1300,3000)
        self.mob_y=620
        self.mob1_01=pygame.image.load('immaginiGioco/mob1_01.png').convert_alpha()
        self.mob1_02=pygame.image.load('immaginiGioco/mob1_02.png').convert_alpha()
        self.mob1_00=[self.mob1_01,self.mob1_02]
        self.parametro=0
        self.parametro2=0
        self.mob1=self.mob1_00[self.parametro]
        self.vel_x=5
        self.mob_rect=self.mob1.get_rect(topleft=(self.mob_x,self.mob_y))

    def movimento_mob(self, keys):
        self.parametro2+=0.02
        if int(self.parametro2)==0:
            self.mob_rect.x-=self.vel_x
        else:
            self.mob_rect.x+=self.vel_x
        if int(self.parametro2)>1:
            self.parametro2=0

        if keys[pygame.K_LEFT]:
            self.mob_rect.x+=VelAvanza
        if keys[pygame.K_RIGHT]:
            self.mob_rect.x-=VelAvanza
    
    def animazione_mob(self):
        self.parametro+=0.1
        if self.parametro>=len(self.mob1_00):
            self.parametro=0
        self.mob1=self.mob1_00[int(self.parametro)]

    def draw_mob(self,screen):
        global mob_rect
        screen.blit(self.mob1,self.mob_rect)


class mob2:
    global keys ,gravità
    def __init__(self, screen):
        self.screen=screen
        self.mob_x=randint(1300,3000)
        self.mob_y=620
        self.mob1_01=pygame.image.load('immaginiGioco/mob1_01.png').convert_alpha()
        self.mob1_02=pygame.image.load('immaginiGioco/mob1_02.png').convert_alpha()
        self.mob1_00=[self.mob1_01,self.mob1_02]
        self.parametro=0
        self.parametro2=0
        self.mob1=self.mob1_00[self.parametro]
        self.vel_x=5
        self.mob_rect=self.mob1.get_rect(topleft=(self.mob_x,self.mob_y))

    def movimento_mob(self):
        self.parametro2+=0.02
        if int(self.parametro2)==0:
            self.mob_rect.x-=self.vel_x
        else:
            self.mob_rect.x+=self.vel_x
        if int(self.parametro2)>1:
            self.parametro2=0

        self.mob_rect.x-=3
    
    def animazione_mob(self):
        self.parametro+=0.1
        if self.parametro>=len(self.mob1_00):
            self.parametro=0
        self.mob1=self.mob1_00[int(self.parametro)]

    def draw_mob(self,screen):
        global mob_rect
        screen.blit(self.mob1,self.mob_rect)