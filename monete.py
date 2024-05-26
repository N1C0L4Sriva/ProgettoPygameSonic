import pygame
from pygame import Surface
from classebase import Oggettobase
from random import randint
# class Monete(Oggettobase):
#     def __init__(self, posizione: tuple = (randint(500,1200),), velocità: tuple = (0,0), accelerazione: tuple = (0,0), percorsoimmagine: str = None, immagine: Surface = None):
#         super().__init__(posizione, velocità, accelerazione, percorsoimmagine, moneta1=pygame.image.load('immaginiGioco/moneta1.png'))
#         self.presa=False

# class Sonic(Oggettobase):
#     def __init__(self, posizione: tuple = ..., velocità: tuple = ..., accelerazione: tuple = ..., grandezza: tuple = ..., percorsoimmagine: str = None, immagine: Surface = None, colore: tuple = ...):
#         super().__init__(posizione, velocità, accelerazione, grandezza, percorsoimmagine, immagine, colore)
        
class Monete:
    def __init__(self):
        self.screen=screen
        self.altezza=randint(300,800)
        self.pos_x=900
        self.moneta1=pygame.image.load('immaginiGioco/moneta1.png')

    def aggiungimonete(self):
        screen.blit(self.moneta1,(self.pos_x,self.altezza))
            
        


