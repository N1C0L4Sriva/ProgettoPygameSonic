import pygame,sys
from sys import exit
from random import randint
from mob_ import mob, mob2
from piattaforme_ import piattaforme, piattaforme2
from monete_ import Monete, Monete2
from alberi_ import alberi, Alberi2
from punteggio_ import Punti


pygame.init() 

screen=pygame.display.set_mode((1100,700))
pygame.display.set_caption('sonic')

def inizializza():
    global sky_surface, ground_surface, ground_rect, alberi_tutti, mob_tutti, monete_tutte, piattaforme_tutte, gameover1, punti1, alberi_tutti_2,monete_tutte2,mob_tutti2, piattaforme_tutte2

    sky_surface=pygame.image.load('immaginiGioco/background2.png').convert()
    ground_surface=pygame.image.load('immaginiGioco/pavimento1.png').convert()
    ground_rect=ground_surface.get_rect(topleft=(-100,700))
    gameover1=pygame.image.load('immaginiGioco/gameover.jpg')

    piattaforme_tutte=[]
    piattaforme_tutte.append(piattaforme(screen))
    piattaforme_tutte2=[]
    piattaforme_tutte2.append(piattaforme2(screen))

    monete_tutte=[]
    monete_tutte.append(Monete(screen, posxminima=1100, posxmassima=1300))
    monete_tutte2=[]
    monete_tutte2.append(Monete2(screen,posxminima=1100, posxmassima=1300))

    mob_tutti=[]
    mob_tutti.append(mob(screen))
    mob_tutti2=[]
    mob_tutti2.append(mob2(screen))

    alberi_tutti=[]
    alberi_tutti.append(alberi())
    alberi_tutti_2=[]
    alberi_tutti_2.append(Alberi2())

    punti1=Punti(screen, (30,30), (30,30))

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
    global sonic_surface, sonic_index
    sonic_index+=0.1
    if sonic_index>=len(sonic_walk):
        sonic_index=0
    sonic_surface=sonic_walk[int(sonic_index)] 

sonic_y=750
sonic_x=300
gravità=0 
gravità2=0
VelAvanza=10

sonic=pygame.image.load('immaginiGioco/sonic.png').convert_alpha()
sonic_rect=sonic.get_rect(bottomleft=(sonic_x,sonic_y))
sonic2=pygame.image.load('immaginiGioco/sonic2.png').convert_alpha()
sonic_walk=[sonic,sonic2]
sonic_index=0
sonic_surface=sonic_walk[sonic_index]

larghezza_sonic2=sonic_surface.get_width()
altezza_sonic2=sonic_surface.get_height()

#ROSE
def animation_rose():
    global rose_surface, rose_index
    rose_index+=0.1
    if rose_index>=len(rose_walk):
        rose_index=0
    rose_surface=rose_walk[int(rose_index)]

rose1=pygame.image.load('immaginiGioco/rose1.png').convert_alpha()
rose_rect=rose1.get_rect(bottomleft=(250,750))
rose2=pygame.image.load('immaginiGioco/rose2.png').convert_alpha()
rose_walk=[rose1,rose2]
rose_index=0
rose_surface=rose_walk[rose_index]

Clock=pygame.time.Clock()
punteggio=0

def gioco_multiplayer():
    global gravità, keys, gravità2
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

        if alberi_tutti_2[-1].posx_albero<750:
            alberi_tutti_2.append(Alberi2())
    
        for alber in alberi_tutti_2:
            alber.draw_alberi(screen)

        #GRAVITà
        gravità+=1
        sonic_rect.y+=gravità
        gravità2+=1
        rose_rect.y+=gravità2

        #muovo sonic e rose con la tastiera 
        ground_rect.x-=3
        sonic_rect.x-=3
        rose_rect.x-=3
        if ground_rect.x<=-50:
            ground_rect.x=0

        if keys[pygame.K_RIGHT]:
            sonic_rect.x+=6
    
        if keys[pygame.K_d]:
            rose_rect.x+=6

        if keys[pygame.K_LEFT]:
            sonic_rect.x-=4
            
        if keys[pygame.K_a]:
            rose_rect.x-=4
        
        if keys[pygame.K_UP] and (sonic_rect.colliderect(ground_rect)):
            gravità=-20
        
        if keys[pygame.K_w] and (rose_rect.colliderect(ground_rect)):
            gravità2=-20

        if sonic_rect.colliderect(ground_rect)and sonic_rect.bottom>=700:
            sonic_rect.bottom=ground_rect.top +1

        if rose_rect.colliderect(ground_rect)and rose_rect.bottom>=700:
            rose_rect.bottom=ground_rect.top +1

        #MONETE
        if monete_tutte2[-1].monete_pos_x<750:
            monete_tutte2.append(Monete2(screen, posxminima=1100, posxmassima=1300))
    
        for moneta in monete_tutte2:
            moneta.animazione_monete()
            generamoneta(piattaforme_tutte)
            ismonetavalida(moneta, piattaforme_tutte)
            moneta.aggiungimonete(screen)
        
            if sonic_rect.colliderect(moneta.rect):
                punti1.punti+=1
                monete_tutte2.remove(moneta)
            punti1.draw()
            if rose_rect.colliderect(moneta.rect):
                punti1.punti+=1
                monete_tutte2.remove(moneta)
            punti1.draw()

        #PIATTAFORME
        if piattaforme_tutte2[-1].rect.x<850:
            piattaforme_tutte2.append(piattaforme2(screen))

        for platform in piattaforme_tutte2:
            platform.mov_piattaforme()
            if platform.rect.colliderect(sonic_rect):
                if sonic_rect.bottom<platform.rect.centery:
                    gravità=0
                    sonic_rect.bottom=platform.rect.top 
                    if keys[pygame.K_UP] :
                        gravità=-20
            if platform.rect.colliderect(rose_rect):
                if rose_rect.bottom<platform.rect.centery:
                    gravità2=0
                    rose_rect.bottom=platform.rect.top 
                    if keys[pygame.K_w] :
                        gravità2=-20

            platform.draw_piattaforme(screen)
            # platform.sonic_sopra_piattaforma(keys,sonic_rect,gravità)


        #MOSTRI
        if mob_tutti2[-1].mob_rect.x<650:
            mob_tutti2.append(mob2(screen))

        for mostro in mob_tutti2:
            mostro.movimento_mob()
            mostro.animazione_mob()
            if sonic_rect.colliderect(mostro.mob_rect):
                gameover()
            if rose_rect.colliderect(mostro.mob_rect):
                gameover()
            mostro.draw_mob(screen)
        
        #personaggi
        animation()
        screen.blit(sonic_surface,sonic_rect)
        animation_rose()
        screen.blit(rose_surface,rose_rect)

        aggiorna()

#gioco singlePlayer
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
        
            if sonic_rect.colliderect(moneta.rect):
                punti1.punti+=1
                monete_tutte.remove(moneta)
            punti1.draw()

        #PIATTAFORME
        if piattaforme_tutte[-1].rect.x<850:
            piattaforme_tutte.append(piattaforme(screen))

        for platform in piattaforme_tutte:
            platform.mov_piattaforme(keys)
            if platform.rect.colliderect(sonic_rect):
                if sonic_rect.bottom<platform.rect.centery:
                    gravità=0
                    sonic_rect.bottom=platform.rect.top 
                    if keys[pygame.K_UP] :
                        gravità=-20

            platform.draw_piattaforme(screen)
            # platform.sonic_sopra_piattaforma(keys,sonic_rect,gravità)

        #MOSTRI
        if mob_tutti[-1].mob_rect.x<650:
            mob_tutti.append(mob(screen))

        for mostro in mob_tutti:
            mostro.movimento_mob(keys)
            mostro.animazione_mob()
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
                if start_button2_rect.collidepoint(event.pos):
                    gioco_multiplayer()

        background_menu=pygame.image.load('immaginiGioco/sonic_menu.png')
        background_menu_1=pygame.transform.scale(background_menu, (1100,800))
        screen.blit(background_menu_1,(0,0))

        # Disegna il testo "START"
        sonic_logo=pygame.image.load('immaginiGioco/sonicLogo.png')
        start_button=pygame.image.load('immaginiGioco/start_button.png')
        start_button1=pygame.transform.scale(start_button, (500,200))
        start_button2_0=pygame.image.load('immaginiGioco/multi.png')
        start_button2=pygame.transform.scale(start_button2_0, (300,300))

        # Crea un rettangolo attorno al testo "START"
        sonic_logo_rect=sonic_logo.get_rect(bottomleft=(350,300))
        start_button_rect=start_button1.get_rect(topleft=(300,300))
        start_button2_rect=start_button2.get_rect(topleft=(350,500))
        
        screen.blit(start_button1,start_button_rect)
        screen.blit(start_button2,start_button2_rect)
        screen.blit(sonic_logo,sonic_logo_rect)

        pygame.display.flip()

if __name__ == "__main__":
    main_menu()