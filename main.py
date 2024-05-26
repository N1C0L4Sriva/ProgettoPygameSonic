import pygame
from sys import exit
from random import randint
# from monete import Monete

sonic_y=750
sonic_x=300
gravità=0 
VelAvanza=4
class piattaforme:
    def __init__(self):
        self.screen=screen
        self.piattaforma1_x=600
        self.piattaforma1_y=550
        self.piattaforma1=pygame.image.load('immaginiGioco/piattaforma.png').convert()

    def draw_piattaforme(self):
        if keys[pygame.K_LEFT]:
            self.piattaforma1_x+=VelAvanza
        if keys[pygame.K_RIGHT]:
            self.piattaforma1_x-=VelAvanza
        self.piattaforma1_rect=self.piattaforma1.get_rect(topleft=(self.piattaforma1_x,self.piattaforma1_y))
        screen.blit(self.piattaforma1,self.piattaforma1_rect)
   
class Monete:
    def __init__(self):
        self.monete_pos_x=1100
        self.monete_altezza=randint(300,650)
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

    def animazione_monete(self):
        self.monete_index+=0.1
        if self.monete_index>=len(self.moneteArray):
            self.monete_index=0
        self.monete_surface=self.moneteArray[int(self.monete_index)]

    def aggiungimonete(self):
        if keys[pygame.K_LEFT]:
            self.monete_pos_x+=VelAvanza
        if keys[pygame.K_RIGHT]:
            self.monete_pos_x-=VelAvanza
        screen.blit(self.monete_surface,(self.monete_pos_x,self.monete_altezza))
        
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

# def generamonete(posizionex, altezza): 
    # moneta= Monete((posizionex,altezza), (0,0),(0,0),(10,10))
    # screen.blit(moneta,monete_rect)
    # return moneta

screen=pygame.display.set_mode((1100,800))

pygame.display.set_caption('sonic')

sky_surface=pygame.image.load('immaginiGioco/background2.png').convert()

ground_surface=pygame.image.load('immaginiGioco/pavimento1.png').convert()
ground_rect=ground_surface.get_rect(topleft=(-100,700))

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

piattaforme_tutte=[]
piattaforme_tutte.append(piattaforme())

monete_tutte=[]
monete_tutte.append(Monete())
# monete=Monete(display)
# moneta1=pygame.image.load('immaginiGioco/moneta1.png')


Clock=pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type==pygame.KEYDOWN and sonic_rect.bottom>=650 or sonic_rect.colliderect(ground2_rect) :
            if event.key==pygame.K_UP:
                gravità= -20

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,ground_rect)
 
    #muovo sonic con la tastiera 
    keys=pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        # sonic_rect.right+=4
        ground_rect.x-=4
        if ground_rect.x<=-50:
            ground_rect.x=0

    if keys[pygame.K_LEFT]:
        ground_rect.x+=4
        if ground_rect.x>0:
            ground_rect.x=-50

    for platform in piattaforme_tutte:
        platform.draw_piattaforme()

    if monete_tutte[-1].monete_pos_x<750:
        monete_tutte.append(Monete())

    for moneta in monete_tutte:
        moneta.animazione_monete()
        moneta.aggiungimonete()

    gravità+=1
    sonic_rect.y+=gravità
    if sonic_rect.colliderect(ground_rect)and sonic_rect.bottom>=700:
        sonic_rect.bottom=ground_rect.top +1

    if sonic_rect.colliderect(ground2_rect):
        sonic_rect.bottom=ground2_rect.top +1

    if sonic_rect.colliderect(ground2_rect) and sonic_rect.top==ground2_rect.bottom:
        sonic_rect.top=ground2_rect.bottom
        sonic_rect.y+=gravità

    animation()
    screen.blit(sonic_surface,sonic_rect)

    # pygame.draw.rect(screen,(255,0,0), sonic_rect,1)
    # pygame.draw.rect(screen,(255,0,0), ground2_rect,1)
    # pygame.draw.rect(screen,(255,0,0), ground_rect, 1)
    # if keys[pygame.K_UP]:

    pygame.display.update()
    Clock.tick(60)


