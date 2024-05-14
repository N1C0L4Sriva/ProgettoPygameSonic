import pygame
from sys import exit

def animation():
    global sonic_surface, sonic_index, sonic_index2

    if sonic_rect.bottom<650:
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

sonic_y=650
sonic_x=400
gravità=0 


screen=pygame.display.set_mode((1200,800))

pygame.display.set_caption('sonic')

sky_surface=pygame.image.load('immaginiGioco/background.png').convert()
sky_x=-20

ground_surface=pygame.image.load('immaginiGioco/Ground.png').convert()

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
        
        if event.type==pygame.KEYDOWN and sonic_rect.bottom>=650:
            if event.key==pygame.K_UP:
                gravità= -20

    screen.blit(sky_surface,(sky_x,0))
    screen.blit(ground_surface,(0,650))
    animation()
    screen.blit(sonic_surface,sonic_rect)

    #muovo sonic con la tastiera
    
    keys=pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        sonic_rect.right+=4
        sky_x-=0.2
    
    if keys[pygame.K_LEFT]:
        sonic_surface=pygame.transform.flip(sonic_surface,True, False)
        sonic_rect.left-=4
        sky_x+=0.2
    
    gravità+=1
    sonic_rect.y+=gravità
    if sonic_rect.bottom>=650:
        sonic_rect.bottom=650

       
    
    
    # if keys[pygame.K_UP]:
        
    

    pygame.display.update()
    Clock.tick(60)
