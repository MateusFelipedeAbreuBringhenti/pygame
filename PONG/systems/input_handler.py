import pygame

class GerenciadorInput:

    def __init__(self, jogador):
        self.jogador = jogador

    def atualizar(self):
        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_UP]:
            self.jogador.mover_cima()

        if teclas[pygame.K_DOWN]:
            self.jogador.mover_baixo()