import pygame
from obstaculo import Obstaculo
pygame.init()

class cactusPequeño(Obstaculo):
    def __init__(self, img, num_cactus,pantalla):
        super().__init__(img, num_cactus,pantalla)
        self.posicion.y = 325

class cactusGrande(Obstaculo):
    def __init__(self, img, num_cactus,pantalla):
        super().__init__(img, num_cactus,pantalla)
        self.posicion.y = 300
