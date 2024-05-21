from pygame import Surface
from classebase import Oggettobase
class Monete(Oggettobase):
    def __init__(self, posizione: tuple = ..., velocità: tuple = ..., accelerazione: tuple = ..., grandezza: tuple = ..., percorsoimmagine: str = None, immagine: Surface = None, colore: tuple = ...):
        super().__init__(posizione, velocità, accelerazione, grandezza, percorsoimmagine, immagine, colore)
        self.presa=False

class Sonic(Oggettobase):
    def __init__(self, posizione: tuple = ..., velocità: tuple = ..., accelerazione: tuple = ..., grandezza: tuple = ..., percorsoimmagine: str = None, immagine: Surface = None, colore: tuple = ...):
        super().__init__(posizione, velocità, accelerazione, grandezza, percorsoimmagine, immagine, colore)
        
