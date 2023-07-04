import math
import sys
import pygame
import neat
import os
import random
import pickle
from cactus import cactusGrande, cactusPequeño
import dino
import time
pygame.init()

# ATRUBUTOS NECESARIOS PARA LA REALIZACION DEL VIDEOJUEGO
height = 720
width = 1280
win = pygame.display.set_mode((width, height))
#global puntuacion, velocidad_juego, pos_x_fondo, pos_y_fondo, obstaculos, dinosaurios, genomes, redes, poblacion
fondoImg = pygame.image.load(os.path.join("img/ground", "Track.png"))
cactusPequeño_img = [pygame.image.load(os.path.join("img/cactus", "SmallCactus1.png")), pygame.image.load(
    os.path.join("img/cactus", "SmallCactus2.png")), pygame.image.load(os.path.join("img/cactus", "SmallCactus3.png"))]
cactusGrande_img = [pygame.image.load(os.path.join("img/cactus", "LargeCactus1.png")), pygame.image.load(
    os.path.join("img/cactus", "LargeCactus2.png")), pygame.image.load(os.path.join("img/cactus", "LargeCactus3.png"))]
fuenteTexto = pygame.font.SysFont("Arial", 20)
fps = 60
blanco = (255, 255, 255)
cielo = (135, 206, 235)
negro = (0, 0, 0)
pos_x_fondo = 0
pos_y_fondo = 380
# CARGAR CONFIGURACION PARA EL ALGORITMO NEAT
dir = os.path.dirname("__file__")
config_neat = os.path.join(dir, "config.txt")
config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                     neat.DefaultSpeciesSet, neat.DefaultStagnation, config_neat)


def menuInicial():

    with open("mejor.pickle", "rb") as f:
        mejorIndividuo = pickle.load(f)

    menu = pygame.display.set_mode((width, height))
    run = True
    click = False
    while run:
        menu.fill(cielo)
        titulo = pygame.image.load(os.path.join(
            "img/btn", "titulo_dino.png")).convert_alpha()
        btn_entrenar_img = pygame.image.load(os.path.join(
            "img/btn", "train_btn.png")).convert_alpha()
        btn_jugar_img = pygame.image.load(os.path.join(
            "img/btn", "best_btn.png")).convert_alpha()
        btn_entrenar = pygame.Rect(450, 300, 240, 126)
        btn_jugar = pygame.Rect(450, 500, 240, 126)
        mousex, mousey = pygame.mouse.get_pos()
        if btn_entrenar.collidepoint((mousex, mousey)):
            if click:
                dinoNeat()
        elif btn_jugar.collidepoint((mousex, mousey)):
            if click:
                bestNeat(mejorIndividuo, config)
        click = False
        pygame.draw.rect(menu, blanco, btn_entrenar)
        pygame.draw.rect(menu, blanco, btn_jugar)
        menu.blit(titulo, (300, 100))
        menu.blit(btn_entrenar_img, (450, 300))
        menu.blit(btn_jugar_img, (450, 500))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True


def dinoJuego(individuos, config):
    global puntuacion, velocidad_juego, pos_x_fondo, pos_y_fondo, obstaculos, dinosaurios, genomes, redes, poblacion
    clock = pygame.time.Clock()
    run = True
    puntuacion = 0
    velocidad_juego = 20
    obstaculos = []
    dinosaurios = []
    genomes = []
    redes = []

    for individuo_id, individuo in individuos:
        individuo.fitness = 0
        dinosaurios.append(dino.Dino())
        genomes.append(individuo)
        red = neat.nn.FeedForwardNetwork.create(individuo, config)
        redes.append(red)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                menuInicial()
                # sys.exit()

        win.fill(cielo)
        # Por cada dino, se tiene que dibujar en la pantalla
        for dinosaurio in dinosaurios:
            dinosaurio.update()
            dinosaurio.dibujar(win)

        # Si no existen mas dinosaurios, se para el juego
        if len(dinosaurios) == 0:
            break

        # Generar obstaculos de manera aleatoria y dibujarlos
        if len(obstaculos) == 0:
            aleatorio = random.randint(0, 1)
            if aleatorio == 0:
                obstaculos.append(cactusPequeño(
                    cactusPequeño_img, random.randint(0, 2), win))
            elif aleatorio == 1:
                obstaculos.append(cactusGrande(
                    cactusGrande_img, random.randint(0, 2), win))
                    
        # Por cada frame que este el dinosaurio en pantalla, su fitness aumenta en 1  
        for i, dinosaurio in enumerate(dinosaurios):
            genomes[i].fitness += 1

        for obs in obstaculos:
            obs.dibujar(win)
            obs.update(velocidad_juego, obstaculos)
            for i, dinosaurio in enumerate(dinosaurios):
                # Colision
                if dinosaurio.posicion.colliderect(obs.posicion):
                    genomes[i].fitness -= 100
                    dinosaurios.pop(i)
                    genomes.pop(i)
                    redes.pop(i)

        # Movimientos del dinosaurio
        for i, dinosaurio in enumerate(dinosaurios):
            out = redes[i].activate((dinosaurio.posicion.y, distancia(
                (dinosaurio.posicion.x, dinosaurio.posicion.y), obs.posicion.midtop)))
            if out[0] > 0.5 and dinosaurio.posicion.y == dinosaurio.pos_y:
                dinosaurio.saltar = True
                dinosaurio.correr = False

        clock.tick(fps)
        puntuar()
        fondoDino()
        vivos_texto = fuenteTexto.render(
            "Individuos vivos: " + str(len(dinosaurios)), True, negro)
        velocidad_texto = fuenteTexto.render(
            "Velocidad: " + str(velocidad_juego), True, negro)
        win.blit(vivos_texto, (75, 500))
        win.blit(velocidad_texto, (75, 560))
        pygame.display.set_caption("DinoJuego")
        pygame.display.update()


def puntuar():
    global puntuacion, velocidad_juego
    puntuacion += 1
    if puntuacion % 100 == 0:
        velocidad_juego += 1
    texto = fuenteTexto.render("Puntos: "+str(puntuacion), True, negro)
    win.blit(texto, (1100, 0))


def fondoDino():
    global pos_x_fondo, pos_y_fondo, velocidad_juego
    width_fondo = fondoImg.get_width()
    win.blit(fondoImg, (pos_x_fondo, pos_y_fondo))
    win.blit(fondoImg, (width_fondo + pos_x_fondo, pos_y_fondo))
    if pos_x_fondo <= -width_fondo:
        pos_x_fondo = 0
    pos_x_fondo -= velocidad_juego


def distancia(a, b):
    x = a[0] - b[0]
    y = a[1] - b[1]
    return math.sqrt(x**2+y**2)


def dinoNeat():
    poblacion = neat.Population(config)
    poblacion.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    poblacion.add_reporter(stats)
    mejorIndividuo = poblacion.run(dinoJuego, 30)
    with open("mejor.pickle", "wb") as f:
        pickle.dump(mejorIndividuo, f)


def bestNeat(mejorIndividuo, config):
    global puntuacion, velocidad_juego, pos_x_fondo, pos_y_fondo, obstaculos, dinosaurios, genomes, redes, poblacion
    clock = pygame.time.Clock()
    run = True
    puntuacion = 0
    velocidad_juego = 20
    obstaculos = []
    dinosaurios = []
    genomes = []
    redes = []

    mejorIndividuo.fitness = 0
    dinosaurios.append(dino.Dino())
    genomes.append(mejorIndividuo)
    red = neat.nn.FeedForwardNetwork.create(mejorIndividuo, config)
    redes.append(red)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                menuInicial()

        win.fill(cielo)
        # Por cada dino, se tiene que dibujar en la pantalla
        for dinosaurio in dinosaurios:
            dinosaurio.update()
            dinosaurio.dibujar(win)

        # Si no existen mas dinosaurios, se para el juego
        if len(dinosaurios) == 0:
            break

        # Generar obstaculos de manera aleatoria y dibujarlos
        if len(obstaculos) == 0:
            aleatorio = random.randint(0, 1)
            if aleatorio == 0:
                obstaculos.append(cactusPequeño(
                    cactusPequeño_img, random.randint(0, 2), win))
            elif aleatorio == 1:
                obstaculos.append(cactusGrande(
                    cactusGrande_img, random.randint(0, 2), win))

        for obs in obstaculos:
            obs.dibujar(win)
            obs.update(velocidad_juego, obstaculos)
            for i, dinosaurio in enumerate(dinosaurios):
                # Por cada frame que el individuo sobrevive, se le suma 1 a su fitness
                #genomes[i].fitness += 1
                # Colision
                if dinosaurio.posicion.colliderect(obs.posicion):
                    # Si colisiona, se le resta 10 al fitness
                    #genomes[i].fitness -= 10
                    dinosaurios.pop(i)
                    genomes.pop(i)
                    redes.pop(i)

        # Movimientos del dinosaurio
        for i, dinosaurio in enumerate(dinosaurios):
            out = redes[i].activate((dinosaurio.posicion.y, distancia(
                (dinosaurio.posicion.x, dinosaurio.posicion.y), obs.posicion.midtop)))
            if out[0] > 0.5 and dinosaurio.posicion.y == dinosaurio.pos_y:
                dinosaurio.saltar = True
                dinosaurio.correr = False

        clock.tick(fps)
        puntuar()
        fondoDino()
        pygame.display.set_caption("DinoJuego")
        pygame.display.update()


if __name__ == '__main__':
    # dinoNeat()
    menuInicial()
