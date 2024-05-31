import pygame
from random import randint

VelAvanza=10
#CLASSE ALBERI
class alberi:
    def __init__(self):
        self.albero=pygame.image.load('immaginiGioco/tree.png').convert()
        self.alberi1=pygame.transform.scale(self.albero,(70,400))
        self.posx_albero=randint(1100,1300)
    
    def draw_alberi(self, keys, screen):
        if keys[pygame.K_LEFT]:
            self.posx_albero+=VelAvanza
        if keys[pygame.K_RIGHT]:
            self.posx_albero-=VelAvanza
        screen.blit(self.alberi1,(self.posx_albero,305))


class Alberi2:
    def __init__(self):
        self.albero=pygame.image.load('immaginiGioco/tree.png').convert()
        self.alberi1=pygame.transform.scale(self.albero,(70,400))
        self.posx_albero=randint(1100,1300)
    
    def draw_alberi(self, screen):  
        self.posx_albero-=3
        screen.blit(self.alberi1,(self.posx_albero,305))
        
        