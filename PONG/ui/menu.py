import pygame
import sys
from config import *


class Menu:

    def __init__(self, tela):
        self.tela = tela
        self.clock = pygame.time.Clock()

        self.fonte_titulo = pygame.font.SysFont(None, 70)
        self.fonte_opcao = pygame.font.SysFont(None, 40)
        self.fonte_instrucao = pygame.font.SysFont(None, 25)

        self.opcoes = ["Fácil", "Difícil"]
        self.selecionado = 0
        self.dificuldade = "facil"

    def executar(self):
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_UP:
                        self.selecionado = (self.selecionado - 1) % len(self.opcoes)

                    if evento.key == pygame.K_DOWN:
                        self.selecionado = (self.selecionado + 1) % len(self.opcoes)

                    if evento.key == pygame.K_SPACE:
                        self.dificuldade = (
                            "facil" if self.selecionado == 0 else "dificil"
                        )
                        return self.dificuldade

            self.tela.fill(COR_PRETO)

            titulo = self.fonte_titulo.render("PONG", True, COR_BRANCO)
            self.tela.blit(titulo, (LARGURA_TELA // 2 - 100, 120))

            for i, opcao in enumerate(self.opcoes):
                texto = self.fonte_opcao.render(opcao, True, COR_BRANCO)

                x = LARGURA_TELA // 2 - 40
                y = 280 + i * 50

                self.tela.blit(texto, (x, y))

                if i == self.selecionado:
                    seta = self.fonte_opcao.render(">", True, COR_BRANCO)
                    self.tela.blit(seta, (x - 30, y))

            tempo = pygame.time.get_ticks()
            if tempo % 2000 < 1000:
                instrucao = self.fonte_instrucao.render(
                    "Pressione ESPAÇO para jogar", True, COR_BRANCO
                )
                self.tela.blit(instrucao, (LARGURA_TELA // 2 - 120, 450))

            pygame.display.flip()
            self.clock.tick(FPS)