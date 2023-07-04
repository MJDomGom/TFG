import pygame
import os
pygame.init()


class Dino:
    pos_x = 80
    pos_y = 310
    vel = 8
    correrImg = [pygame.image.load(os.path.join("img/dino", "DinoRun1.png")), pygame.image.load(os.path.join("img/dino", "DinoRun2.png"))]
    saltarImg = pygame.image.load(os.path.join("img/dino", "DinoJump.png"))
    height = 720
    width = 1280
    win = pygame.display.set_mode((width, height))

    def __init__(self):
        self.image = self.correrImg[0]
        self.correr = True
        self.saltar = False
        self.vel_salto = self.vel
        self.posicion = pygame.Rect(
            self.pos_x, self.pos_y, self.image.get_width(), self.image.get_height())
        self.index = 0

    def update(self):
        if self.correr:
            self.dinoCorrer()
        if self.saltar:
            self.dinoSaltar()
        if self.index >= 10:
            self.index = 0

    def dinoSaltar(self):
        self.image = self.saltarImg
        if self.saltar:
            self.posicion.y -= self.vel_salto * 5 
            self.vel_salto -= 0.8
        if self.vel_salto <= -self.vel:
            self.saltar = False
            self.correr = True
            self.vel_salto = self.vel

    def dinoCorrer(self):
        self.image = self.correrImg[self.index // 5]
        self.posicion.x = self.pos_x
        self.posicion.y = self.pos_y
        self.index += 1

    def dibujar(self, pantalla):
        pantalla.blit(self.image, (self.posicion.x,self.posicion.y))