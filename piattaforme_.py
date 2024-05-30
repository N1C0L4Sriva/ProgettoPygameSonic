import pygame
from random import randint
#CLASSE PER LE PIATTAFORME
VelAvanza=10

class piattaforme:
    def __init__(self, screen):
        self.screen=screen
        self.piattaforma1_x=randint(1100,2000)
        self.piattaforma1_y=randint(500,600)
        self.piattaforma1=pygame.image.load('immaginiGioco/piattaforma.png').convert()
        self.rect=self.piattaforma1.get_rect(topleft=(self.piattaforma1_x,self.piattaforma1_y))

    def draw_piattaforme(self,screen):
        screen.blit(self.piattaforma1,self.rect)
  
    def mov_piattaforme(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x+=VelAvanza

        if keys[pygame.K_RIGHT]:
            self.rect.x-=VelAvanza
            
        # if keys[pygame.K_UP] and sonic_rect.bottom==self.rect.top:
        #     gravità=-20

        
           

        # if keys[pygame.K_UP] and sonic_rect.colliderect(self.rect):
        #     sonic_rect.bottom=self.rect.top +1
        #     gravità=-20
        
        # if sonic_rect.colliderect(self.rect):
        #     if gravità>0:
        #         sonic_rect.bottom=self.rect.top
        #     if gravità<=0:
        #         gravità=5
        #         sonic_rect.top=self.rect.bottom