import pygame
from random import randint

VelAvanza=7
#CLASSE PER LE MONETE      
class Monete:
    def __init__(self,screen, posxminima=1100, posxmassima=1300):
        self.monete_pos_x=1300
        self.monete_altezza=randint(300,650)
        self.monete_larghezza=randint(posxminima, posxmassima)
        self.monete_pos_x=1200
        self.screen=screen        
        self.moneta1=pygame.image.load('immaginiGioco/moneta1.png')
        self.moneta2=pygame.image.load('immaginiGioco/monete_2.png')
        self.moneta3=pygame.image.load('immaginiGioco/monete3.png')
        self.moneta4=pygame.image.load('immaginiGioco/monete4.png')
        self.moneta5=pygame.image.load('immaginiGioco/monete5.png')
        self.moneta6=pygame.image.load('immaginiGioco/monete6.png')
        self.moneta7=pygame.image.load('immaginiGioco/monete7.png')
        self.moneta8=pygame.image.load('immaginiGioco/monete8.png')
        self.moneteArray=[self.moneta1,self.moneta2,self.moneta3,self.moneta4,self.moneta5,self.moneta6,self.moneta6,self.moneta8]
        self.monete_index=0
        self.monete_surface=self.moneteArray[self.monete_index]
        self.rect=self.moneta1.get_rect(topleft=(self.monete_pos_x,self.monete_altezza))
    
    def collide(self, other_rect):
        return self.rect.colliderect(other_rect)
    
    def animazione_monete(self):
        self.monete_index+=0.1
        if self.monete_index>=len(self.moneteArray):
            self.monete_index=0
        self.monete_surface=self.moneteArray[int(self.monete_index)]

    def aggiungimonete(self,screen, keys):
        if keys[pygame.K_LEFT]:
            self.monete_pos_x+=VelAvanza
        if keys[pygame.K_RIGHT]:
            self.monete_pos_x-=VelAvanza
        self.rect.x = self.monete_pos_x
        screen.blit(self.monete_surface,self.rect)

class Monete2:
    def __init__(self,screen, posxminima=1100, posxmassima=1300):
        self.monete_pos_x=1300
        self.monete_altezza=randint(300,650)
        self.monete_larghezza=randint(posxminima, posxmassima)
        self.monete_pos_x=1200
        self.screen=screen        
        self.moneta1=pygame.image.load('immaginiGioco/moneta1.png')
        self.moneta2=pygame.image.load('immaginiGioco/monete_2.png')
        self.moneta3=pygame.image.load('immaginiGioco/monete3.png')
        self.moneta4=pygame.image.load('immaginiGioco/monete4.png')
        self.moneta5=pygame.image.load('immaginiGioco/monete5.png')
        self.moneta6=pygame.image.load('immaginiGioco/monete6.png')
        self.moneta7=pygame.image.load('immaginiGioco/monete7.png')
        self.moneta8=pygame.image.load('immaginiGioco/monete8.png')
        self.moneteArray=[self.moneta1,self.moneta2,self.moneta3,self.moneta4,self.moneta5,self.moneta6,self.moneta6,self.moneta8]
        self.monete_index=0
        self.monete_surface=self.moneteArray[self.monete_index]
        self.rect=self.moneta1.get_rect(topleft=(self.monete_pos_x,self.monete_altezza))
    
    def collide(self, other_rect):
        return self.rect.colliderect(other_rect)
    
    def animazione_monete(self):
        self.monete_index+=0.1
        if self.monete_index>=len(self.moneteArray):
            self.monete_index=0
        self.monete_surface=self.moneteArray[int(self.monete_index)]

    def aggiungimonete(self,screen):
        self.monete_pos_x-=4
        self.rect.x = self.monete_pos_x
        screen.blit(self.monete_surface,self.rect)