import pygame
from sys import exit
from random import randint

from monete import Monete



def animation():
    global sonic_surface, sonic_index, sonic_index2

    if not sonic_rect.colliderect(ground2_rect) and not sonic_rect.colliderect(ground_rect):  #and sonic_rect.bottom<650:
        sonic_index2+=0.1
        sonic_surface=sonic_jump
        if sonic_index2>=len(sonic_jump):
            sonic_index2=0
        sonic_surface=sonic_jump[int(sonic_index2)]
    else:
        sonic_index+=0.1
        if sonic_index>=len(sonic_walk):
            sonic_index=0
        sonic_surface=sonic_walk[int(sonic_index)]

sonic_y=750
sonic_x=300
gravità=0 

punteggio=0
monete=[]

def generamonete(posizionex, altezza):
    altezza=randint(300,800)
    moneta= Monete((posizionex,altezza), (0,0),(0,0),(10,10))
    screen.blit(moneta)
    return moneta


screen=pygame.display.set_mode((1200,800))


pygame.display.set_caption('sonic')



sky_surface=pygame.image.load('immaginiGioco/background2.png').convert()

ground_surface=pygame.image.load('immaginiGioco/pavimento1.png').convert()
ground_rect=ground_surface.get_rect(topleft=(0,700))

ground2_surface=pygame.image.load('immaginiGioco/piattaforma.png').convert()
ground2_x=600
ground2_rect=ground2_surface.get_rect(topleft=(ground2_x,550))


sonic=pygame.image.load('immaginiGioco/sonic.png').convert_alpha()
sonic_rect=sonic.get_rect(bottomleft=(sonic_x,sonic_y))
sonic2=pygame.image.load('immaginiGioco/sonic2.png').convert_alpha()
sonic_walk=[sonic,sonic2]
sonic_jump1=pygame.image.load('immaginiGioco/sonic_jump_1.png').convert_alpha()
sonic_jump2=pygame.image.load('immaginiGioco/sonic_jump_2.png').convert_alpha()
sonic_jump=[sonic_jump1,sonic_jump2]
sonic_index=0
sonic_index2=0
sonic_surface=sonic_walk[sonic_index]

Clock=pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type==pygame.KEYDOWN and sonic_rect.bottom>=650 or sonic_rect.colliderect(ground2_rect):
            if event.key==pygame.K_UP:
                gravità= -20

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,ground_rect)
    screen.blit(ground2_surface,ground2_rect)
    # generamonete()



    #muovo sonic con la tastiera
    
    keys=pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        # sonic_rect.right+=4
        ground2_rect.x-=4
    
    

    gravità+=1
    sonic_rect.y+=gravità
    if sonic_rect.colliderect(ground_rect)and sonic_rect.bottom>=700:

        sonic_rect.bottom=ground_rect.top +1

    if sonic_rect.colliderect(ground2_rect):
        sonic_rect.bottom=ground2_rect.top +1

    
    animation()
       
    screen.blit(sonic_surface,sonic_rect)
    # pygame.draw.rect(screen,(255,0,0), sonic_rect,1)
    # pygame.draw.rect(screen,(255,0,0), ground2_rect,1)
    # pygame.draw.rect(screen,(255,0,0), ground_rect, 1)
    # if keys[pygame.K_UP]:
        
    

    pygame.display.update()
    Clock.tick(60)


