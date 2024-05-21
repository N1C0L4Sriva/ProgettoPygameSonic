from pygame.color import THECOLORS 
import pygame
pygame.init()
fps=30
clock=pygame.time.Clock()
grandezzafinestra=(720,480)
finestra=pygame.display.set_mode(grandezzafinestra)
pygame.display.set_caption("SONIC")
def ciclo():
    while True:
        finestra.fill(THECOLORS["black"]) # cancello schermo 
        events=pygame.event.get()
        for event in events:
            if event.type==pygame.QUIT:
                pygame.quit()
                exit()
            if event.type==pygame.KEYDOWN:
                 pass #da fare



               
                 # gestisco eventi(chiudi finestra, schiaccio pulsanti)
                # aggiorno logica del gioco 
                # disegno (render dei vari oggetti)
                 # pygame.display.update
                 # time clock


