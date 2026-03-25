
import pygame
from config import COR_BRANCO, LARGURA_TELA

class GerenciadorPontuacao:

    def __init__(self, score_sound=None):
        self.p1 = 0
        self.p2 = 0
        self.fonte = pygame.font.SysFont(None, 40)
        self.score_sound = score_sound

    def atualizar(self, bola):
        if bola.rect.left <= 0:
            self.p2 += 1
            if self.score_sound:
                self.score_sound.play()
            bola.resetar()

        elif bola.rect.right >= LARGURA_TELA:
            self.p1 += 1
            if self.score_sound:
                self.score_sound.play()
            bola.resetar()

    def desenhar(self, tela):
        texto = self.fonte.render(f"{self.p1} - {self.p2}", True, COR_BRANCO)
        tela.blit(texto, (LARGURA_TELA // 2 - 30, 20))