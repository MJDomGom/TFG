import sys
import pickle
import os
import neat
from pong.game import Game as Gm
import pygame
pygame.init()

width, height = 800, 600
win = pygame.display.set_mode((width, height))
game = Gm(win, width, height)
negro = (0, 0, 0)



class PongGame:
    def __init__(self, window, width, height):
        self.game = Gm(window, width, height)
        self.raq_izq = self.game.left_paddle
        self.raq_der = self.game.right_paddle
        self.pelota = self.game.ball

    def jugar(self, mejorIndividuo, config):
        red = neat.nn.FeedForwardNetwork.create(mejorIndividuo, config)
        run = True
        fps = 60
        clock = pygame.time.Clock()
        while run:
            clock.tick(fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    menuInicial()
            teclasPulsadas = pygame.key.get_pressed()
            if teclasPulsadas[pygame.K_w]:
                self.game.move_paddle(left=True, up=True)
            if teclasPulsadas[pygame.K_s]:
                self.game.move_paddle(left=True, up=False)
            out = red.activate(
                (self.raq_der.y, self.pelota.y, abs(self.raq_der.x - self.pelota.x)))
            des = out.index(max(out))
            self.moverRaq(des, False)
            self.game.loop()
            self.game.draw(True, False)
            pygame.display.update()

    def fitness(self, individuo1, individuo2, info):
        individuo1.fitness += info.left_hits
        individuo2.fitness += info.right_hits

    def entrenar_ia(self, individuo1, individuo2, config):
        red1 = neat.nn.FeedForwardNetwork.create(individuo1, config)
        red2 = neat.nn.FeedForwardNetwork.create(individuo2, config)

        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    menuInicial()
                    
            out1 = red1.activate(
                (self.raq_izq.y, self.pelota.y, abs(self.raq_izq.x - self.pelota.x)))
            des1 = out1.index(max(out1))
            self.moverRaq(des1, True)
            out2 = red2.activate(
                (self.raq_der.y, self.pelota.y, abs(self.raq_der.x - self.pelota.x)))
            des2 = out2.index(max(out2))
            self.moverRaq(des2, False)
            #print(out1, out2)

            info = self.game.loop()
            self.game.draw(draw_score=False, draw_hits=True)
            pygame.display.update()

            # Si falla 1 vez, pasamos a la siguiente raqueta, porque continuara fallando
            if info.left_score >= 1 or info.right_score >= 1 or info.right_hits > 50 or info.left_hits > 50:
                self.fitness(individuo1, individuo2, info)
                break

    def moverRaq(self, des, left):
        if left:
            if des == 0:
                pass
            elif des == 1:
                self.game.move_paddle(left=True, up=True)
            else:
                self.game.move_paddle(left=True, up=False)
        else:
            if des == 0:
                pass
            elif des == 1:
                self.game.move_paddle(left=False, up=True)
            else:
                self.game.move_paddle(left=False, up=False)

def eval_individuos(individuos, config):
        width, height = 800, 600
        win = pygame.display.set_mode((width, height))

        for i, (individuo_id, individuo1) in enumerate(individuos):
            if i == len(individuos) - 1:
                break
            individuo1.fitness = 0
            for individuo_id2, individuo2 in individuos[i+1:]:
                individuo2.fitness = 0 if individuo2.fitness == None else individuo2.fitness
                game = PongGame(win, width, height)
                game.entrenar_ia(individuo1, individuo2, config)

def neat_pong(config):
        #poblacion = neat.Checkpointer.restore_checkpoint('neat-checkpoint-')
        poblacion = neat.Population(config)
        poblacion.add_reporter(neat.StdOutReporter(True))
        estadisticas = neat.StatisticsReporter()
        poblacion.add_reporter(estadisticas)
        # poblacion.add_reporter(neat.Checkpointer(5))

        mejorIndividuo = poblacion.run(eval_individuos, 30)
        with open("mejor.pickle", "wb") as f:
            pickle.dump(mejorIndividuo, f)

def cargarMejor(config):
        width, height = 800, 600
        win = pygame.display.set_mode((width, height))
        with open("mejor.pickle", "rb") as f:
            mejorIndividuo = pickle.load(f)

        juego = PongGame(win, width, height)
        juego.jugar(mejorIndividuo, config)

def menuInicial():
        dir = os.path.dirname(__file__)
        config_neat = os.path.join(dir, 'config.txt')
        config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                            neat.DefaultSpeciesSet, neat.DefaultStagnation, config_neat)
        menu = pygame.display.set_mode((width, height))
        run = True
        while run:
            menu.fill(negro)
            titulo = pygame.image.load(os.path.join("img/assets","titulo_pong.png"))
            btn_entrenar_img = pygame.image.load(os.path.join("img/assets","btn_entrenar.png"))
            btn_best_img = pygame.image.load(os.path.join("img/assets","btn_best.png"))
            btn_entrenar = pygame.Rect(200, 200, 287, 59)
            btn_best = pygame.Rect(200, 400, 287, 59)
            mousex, mousey = pygame.mouse.get_pos()
            if btn_entrenar.collidepoint((mousex, mousey)):
                if click:
                    neat_pong(config)
            elif btn_best.collidepoint((mousex, mousey)):
                if click:
                    cargarMejor(config)
            click = False
            pygame.draw.rect(menu, negro, btn_entrenar)
            pygame.draw.rect(menu, negro, btn_best)
            menu.blit(titulo, (150, 0))
            menu.blit(btn_entrenar_img, (200, 200))
            menu.blit(btn_best_img, (200, 400))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True


if __name__ == '__main__':
    menuInicial()
