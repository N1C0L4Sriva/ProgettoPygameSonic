import pygame,sys
pygame.font.init()
from sys import exit
from random import randint

screen=pygame.display.set_mode((1100,800))

pygame.display.set_caption('sonic')

sonic_y=750
sonic_x=300
gravità=0 
VelAvanza=10

class mob:
    global keys ,gravità
    def __init__(self):
        self.screen=screen
        self.mob_x=randint(1300,1500)
        self.mob_y=620
        self.mob1_01=pygame.image.load('immaginiGioco/mob1_01.png').convert_alpha()
        self.mob1_02=pygame.image.load('immaginiGioco/mob1_02.png').convert_alpha()
        self.mob1_00=[self.mob1_01,self.mob1_02]
        self.parametro=0
        self.parametro2=0
        self.mob1=self.mob1_00[self.parametro]
        self.vel_y=5
        self.mob_rect=self.mob1.get_rect(topleft=(self.mob_x,self.mob_y))

    def movimento_mob(self):
        self.parametro2+=0.02
        if int(self.parametro2)==0:
            self.mob_rect.y-=self.vel_y
        else:
            self.mob_rect.y+=self.vel_y
        if int(self.parametro2)>1:
            self.parametro2=0

        if keys[pygame.K_LEFT]:
            self.mob_rect.x+=VelAvanza
        if keys[pygame.K_RIGHT]:
            self.mob_rect.x-=VelAvanza
    
    def draw_mob(self):
        screen.blit(self.mob1,self.mob_rect)

class piattaforme:
    def __init__(self):
        self.screen=screen
        self.piattaforma1_x=randint(1100,1400)
        self.piattaforma1_y=randint(400,600)
        self.piattaforma1=pygame.image.load('immaginiGioco/piattaforma.png').convert()
        self.piattaforma1_rect=self.piattaforma1.get_rect(topleft=(self.piattaforma1_x,self.piattaforma1_y))       

    def draw_piattaforme(self):
        self.piattaforma1_rect=self.piattaforma1.get_rect(topleft=(self.piattaforma1_x,self.piattaforma1_y))
        screen.blit(self.piattaforma1,self.piattaforma1_rect)
  
    def mov_piattaforme(self):
        global gravità
        if keys[pygame.K_LEFT]:
            self.piattaforma1_x+=VelAvanza

        if keys[pygame.K_RIGHT]:
            self.piattaforma1_x-=VelAvanza

        if keys[pygame.K_UP] and (sonic_rect.colliderect(ground_rect)):
            gravità=-20
        
        if keys[pygame.K_UP] and sonic_rect.colliderect(self.piattaforma1_rect):
            gravità=-20

        if sonic_rect.colliderect(self.piattaforma1_rect):
            if gravità>0:
                sonic_rect.bottom=self.piattaforma1_rect.top
            if gravità<=0:
                gravità=10
                sonic_rect.top=self.piattaforma1_rect.bottom
           
        
            
      
class Monete:
    def __init__(self):
        self.monete_pos_x=1300
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
    sonic_index+=0.1
    if sonic_index>=len(sonic_walk):
        sonic_index=0
    sonic_surface=sonic_walk[int(sonic_index)] 

screen=pygame.display.set_mode((1100,800))

pygame.display.set_caption('sonic')

sky_surface=pygame.image.load('immaginiGioco/background2.png').convert()

ground_surface=pygame.image.load('immaginiGioco/pavimento1.png').convert()
ground_rect=ground_surface.get_rect(topleft=(-100,700))

sonic=pygame.image.load('immaginiGioco/sonic.png').convert_alpha()
sonic_rect=sonic.get_rect(bottomleft=(sonic_x,sonic_y))
sonic2=pygame.image.load('immaginiGioco/sonic2.png').convert_alpha()
sonic_walk=[sonic,sonic2]
sonic_index=0
sonic_index2=0
sonic_surface=sonic_walk[sonic_index]

larghezza_sonic2=sonic_surface.get_width()
altezza_sonic2=sonic_surface.get_height()

piattaforme_tutte=[]
piattaforme_tutte.append(piattaforme())

monete_tutte=[]
monete_tutte.append(Monete())

mob_tutti=[]
mob_tutti.append(mob())


Clock=pygame.time.Clock()

def gioco():
    global gravità, piattaforma1_rect, keys
    while True:
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

        animation()
        screen.blit(sonic_surface,sonic_rect)

        gravità+=1
        sonic_rect.y+=gravità

        #muovo sonic con la tastiera 
        keys=pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            ground_rect.x-=4
            if ground_rect.x<=-50:
                ground_rect.x=0

        if keys[pygame.K_LEFT]:
            ground_rect.x+=4
            if ground_rect.x>0:
                ground_rect.x=-50

        if piattaforme_tutte[-1].piattaforma1_x<850:
            piattaforme_tutte.append(piattaforme())

        if sonic_rect.colliderect(ground_rect)and sonic_rect.bottom>=700:
            sonic_rect.bottom=ground_rect.top +1
    
        for platform in piattaforme_tutte:
            platform.mov_piattaforme()
            platform.draw_piattaforme()
    
        if monete_tutte[-1].monete_pos_x<750:
            monete_tutte.append(Monete())
    
        for moneta in monete_tutte:
            moneta.animazione_monete()
            moneta.aggiungimonete()
    
        if mob_tutti[-1].mob_rect.x<650:
            mob_tutti.append(mob())

        for mostro in mob_tutti:
            mostro.movimento_mob()
            mostro.draw_mob()

        pygame.display.update()
        Clock.tick(60+pygame.time.get_ticks()//2000)

BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# Creazione della finestra
pygame.display.set_caption('Sonic Main Menu')

# Font per il testo
font = pygame.font.SysFont("sonic font", 80)

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)

def main_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if sonic_logo_rect.collidepoint(event.pos):
                    print("Start button clicked!")
                    # Qui potresti inserire la chiamata per avviare il gioco
                    gioco()

        screen.fill(BLUE)

        # Disegna il testo "START"
        sonic_logo=pygame.image.load('immaginiGioco/sonicLogo.png')
        draw_text('START ', font, WHITE, screen, 1100 // 2, 800 // 2)

        # Crea un rettangolo attorno al testo "START"
        sonic_logo=pygame.image.load('immaginiGioco/sonicLogo.png')
        sonic_logo_rect=sonic_logo.get_rect(bottomleft=(350,300))
        start_button = pygame.Rect((11000 // 2 - 100, 800 // 2 - 50), (200, 100))
        pygame.draw.rect(screen, WHITE, start_button, 2)
        screen.blit(sonic_logo,sonic_logo_rect)

        pygame.display.flip()

if __name__ == "__main__":
    main_menu()