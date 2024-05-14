from typing import Any
from pygame.sprite import Sprite, Group
from pygame.surface import Surface
from pygame.transform import scale
from pygame.image import load
from pygame.mask import from_surface
class Oggettobase(Sprite):
    def __init__(self, 
                 posizione:tuple[2] = (0,0),
                 velocità:tuple[2]= (0,0),
                 accelerazione:tuple = (0,0),
                 grandezza:tuple[2]=(10,10),
                 percorsoimmagine:str= None,
                 immagine:Surface = None,
                 colore:tuple[3] = (0,0,0)):
        super().__init__()
        self.posizione=posizione
        self.velocità=velocità
        self.grandezza=grandezza
        self.accelerazione=accelerazione
        if percorsoimmagine is None:

            if immagine is not None:
                self.image=immagine
                
            else:
                self.image=Surface(grandezza)
                self.image.fill(colore)
        else:
                self.image = load(percorsoimmagine)
        
        self.image=scale(self.image, self.grandezza)     
        self.rect=self.image.get_rect()      
        self.mask=from_surface(self.image)
        self.rect.x, self.rect.y=self.posizione
    def movimento(self, coordinate:tuple[2]=None):
        if coordinate is None:
              self.rect.x, self.rect.y=self.posizione
        else:
             self.rect.x=coordinate[0]
             self.rect.y=coordinate[1]
    def update(self, *args: Any, **kwargs: Any) -> None:
         self.velocità = (self.velocità[0]+self.accelerazione[0], self.velocità[1]+self.accelerazione[1])

         self.posizione=(self.posizione[0]+self.velocità[0]+self.accelerazione[0]/2, self.posizione[1]+self.velocità[1]+self.accelerazione[1]/2)
        

         self.movimento()
    def __repr__(self) -> str:
        stringa="posizione:({}), velocità:({}), accelerazione:({}), grandezza({})".format(self.posizione, self.velocità, self.accelerazione, self.grandezza)
        return stringa
    
