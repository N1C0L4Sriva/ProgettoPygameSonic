import pygame

colore=("yellow")


class Punti:
    def __init__(self, screen, pos, dimensione) -> None:
        self.screen=screen
        self.pos=pos
        self.dimensione=dimensione
        self.punti=0
        self.rect=pygame.Rect(pos[0], pos[1], dimensione[0], dimensione[1])
    
    def draw(self):
        font=pygame.font.Font(None, 80)
        text=font.render(str(self.punti), 1, colore)
        self.screen.blit(text, (30,30))
