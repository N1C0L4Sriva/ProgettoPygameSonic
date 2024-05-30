import pygame,sys
from sys import exit
from random import randint
from mob_ import mob
from piattaforme_ import piattaforme
from monete_ import Monete
from alberi_ import alberi

pygame.init() 

screen=pygame.display.set_mode((1100,700))
pygame.display.set_caption('sonic')

def inizializza():
    global sky_surface, ground_surface, ground_rect, alberi_tutti, mob_tutti, monete_tutte, piattaforme_tutte, gameover1

    sky_surface=pygame.image.load('immaginiGioco/background2.png').convert()
    ground_surface=pygame.image.load('immaginiGioco/pavimento1.png').convert()
    ground_rect=ground_surface.get_rect(topleft=(-100,700))
    gameover1=pygame.image.load('immaginiGioco/gameover.jpg')

    piattaforme_tutte=[]
    piattaforme_tutte.append(piattaforme(screen))

    monete_tutte=[]
    monete_tutte.append(Monete(screen, posxminima=1100, posxmassima=1300))

    mob_tutti=[]
    mob_tutti.append(mob(screen))

    alberi_tutti=[]
    alberi_tutti.append(alberi())

def aggiorna():
    pygame.display.update()
    Clock.tick(60+pygame.time.get_ticks()//2000)

def gameover():
    screen.blit(gameover1,(0,0))
    ricomincia=False
    while not ricomincia:
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
                inizializza()
                ricomincia=True
            if event.type==pygame.QUIT:
                pygame.quit()
            aggiorna()
            
inizializza()

# Creazione della finestra
pygame.display.set_caption('Sonic Main Menu')

def ismonetavalida(moneta, piattaforme_tutte):
    for piattaforma in piattaforme_tutte:
        if moneta.collide(piattaforma.rect):
            return False
    return True

def generamoneta(piattaforme_tutte):
    moneta=Monete(screen, posxminima=1100, posxmassima=1300)
    while not ismonetavalida(moneta, piattaforme_tutte):
        moneta=Monete(screen, posxminima=1100, posxmassima=1300)
    return moneta

screen=pygame.display.set_mode((1100,800))

pygame.display.set_caption('sonic')

#SONIC     
def animation():
    global sonic_surface, sonic_index, sonic_index2
    sonic_index+=0.1
    if sonic_index>=len(sonic_walk):
        sonic_index=0
    sonic_surface=sonic_walk[int(sonic_index)] 

sonic_y=750
sonic_x=300
gravità=0 
VelAvanza=10

sonic=pygame.image.load('immaginiGioco/sonic.png').convert_alpha()
sonic_rect=sonic.get_rect(bottomleft=(sonic_x,sonic_y))
sonic2=pygame.image.load('immaginiGioco/sonic2.png').convert_alpha()
sonic_walk=[sonic,sonic2]
sonic_index=0
sonic_index2=0
sonic_surface=sonic_walk[sonic_index]

larghezza_sonic2=sonic_surface.get_width()
altezza_sonic2=sonic_surface.get_height()

Clock=pygame.time.Clock()
punteggio=0


def gioco():
    global gravità, keys
    while True:
        keys=pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
        
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,ground_rect)

        if alberi_tutti[-1].posx_albero<750:
            alberi_tutti.append(alberi())
    
        for alber in alberi_tutti:
            alber.draw_alberi(keys,screen)

        animation()
        screen.blit(sonic_surface,sonic_rect)

        #GRAVITà
        gravità+=1
        sonic_rect.y+=gravità

        #muovo sonic con la tastiera 
        if keys[pygame.K_RIGHT]:
            ground_rect.x-=4
            if ground_rect.x<=-50:
                ground_rect.x=0

        if keys[pygame.K_LEFT]:
            ground_rect.x+=4
            if ground_rect.x>=0:
                ground_rect.x=-50
        
        if keys[pygame.K_UP] and (sonic_rect.colliderect(ground_rect)):
            gravità=-20

        if sonic_rect.colliderect(ground_rect)and sonic_rect.bottom>=700:
            sonic_rect.bottom=ground_rect.top +1

        #MONETE
        if monete_tutte[-1].monete_pos_x<750:
            monete_tutte.append(Monete(screen, posxminima=1100, posxmassima=1300))
    
        for moneta in monete_tutte:
            moneta.animazione_monete()
            generamoneta(piattaforme_tutte)
            ismonetavalida(moneta, piattaforme_tutte)
            moneta.aggiungimonete(screen, keys)

        #PIATTAFORME
        if piattaforme_tutte[-1].rect.x<850:
            piattaforme_tutte.append(piattaforme(screen))

        for platform in piattaforme_tutte:
            platform.mov_piattaforme(keys,sonic_rect, gravità)
            platform.draw_piattaforme(screen)

        #MOSTRI
        if mob_tutti[-1].mob_rect.x<650:
            mob_tutti.append(mob(screen))

        for mostro in mob_tutti:
            mostro.movimento_mob(keys)
            if sonic_rect.colliderect(mostro.mob_rect):
                gameover()
            mostro.draw_mob(screen)

        aggiorna()

WHITE = (255, 255, 255)

# Creazione della finestra
pygame.display.set_caption('Sonic Main Menu')

def main_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button_rect.collidepoint(event.pos):
                    print("Start button clicked!")
                    # Qui potresti inserire la chiamata per avviare il gioco
                    gioco()

        background_menu=pygame.image.load('immaginiGioco/sonic_menu.png')
        background_menu_1=pygame.transform.scale(background_menu, (1100,800))
        screen.blit(background_menu_1,(0,0))

        # Disegna il testo "START"
        sonic_logo=pygame.image.load('immaginiGioco/sonicLogo.png')
        start_button=pygame.image.load('immaginiGioco/start_button.png')
        start_button1=pygame.transform.scale(start_button, (500,200))

        # Crea un rettangolo attorno al testo "START"
        sonic_logo_rect=sonic_logo.get_rect(bottomleft=(350,300))
        start_button_rect=start_button1.get_rect(topleft=(300,300))
        
        screen.blit(start_button1,start_button_rect)
        screen.blit(sonic_logo,sonic_logo_rect)

        pygame.display.flip()

if __name__ == "__main__":
    main_menu()