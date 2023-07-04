import pygame
import os
import random
import sys
pygame.init()

class Obstaculo:
    cactusPequeño_img = [pygame.image.load(os.path.join("img/cactus", "SmallCactus1.png")),pygame.image.load(os.path.join("img/cactus", "SmallCactus2.png")),pygame.image.load(os.path.join("img/cactus", "SmallCactus3.png"))]
    cactusGrande_img = [pygame.image.load(os.path.join("img/cactus", "LargeCactus1.png")),pygame.image.load(os.path.join("img/cactus", "LargeCactus2.png")),pygame.image.load(os.path.join("img/cactus", "LargeCactus3.png"))]

    def __init__(self,img,num_cactus,pantalla):
        self.image = img
        self.tipo = num_cactus
        self.posicion = self.image[self.tipo].get_rect()
        self.posicion.x = 1280

    def update(self,velocidad,obstaculos):
        self.posicion.x -= velocidad
        if self.posicion.x < -self.posicion.width:
            obstaculos.pop()
    
    def dibujar(self, pantalla):
        pantalla.blit(self.image[self.tipo],self.posicion)