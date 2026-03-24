import pygame
from config import *
from entities.raquete import Raquete
from entities.bola import Bola
from systems.input_handler import GerenciadorInput
from systems.ia_controller import IAController
from systems.colisao import SistemaColisao
from systems.pontuacao import GerenciadorPontuacao
from ui.menu import Menu

class Jogo:

    def __init__(self):
        pygame.init()

        self.tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
        pygame.display.set_caption("Pong v2")

        self.clock = pygame.time.Clock()

        self.jogador1 = Raquete(15, ALTURA_TELA // 2 - 30)
        self.jogador2 = Raquete(LARGURA_TELA - 25, ALTURA_TELA // 2 - 30)
        self.bola = Bola()

        self.input = GerenciadorInput(self.jogador1)
        self.colisao = SistemaColisao(self.bola, [self.jogador1, self.jogador2])
        self.pontuacao = GerenciadorPontuacao()

        self.menu = Menu(self.tela)

        self.ia = None

    def configurar_dificuldade(self, dificuldade):
        if dificuldade == "facil":
            self.ia = IAController(self.jogador2, self.bola, velocidade=4, erro=30)
        else:
            self.ia = IAController(self.jogador2, self.bola, velocidade=7, erro=5)

    def executar(self):
        dificuldade = self.menu.executar()
        self.configurar_dificuldade(dificuldade)

        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.input.atualizar()
            self.ia.atualizar()
            self.bola.atualizar()
            self.colisao.verificar()
            self.pontuacao.atualizar(self.bola)

            self.tela.fill(COR_PRETO)

            self.jogador1.desenhar(self.tela)
            self.jogador2.desenhar(self.tela)
            self.bola.desenhar(self.tela)
            self.pontuacao.desenhar(self.tela)

            pygame.display.flip()
            self.clock.tick(FPS)