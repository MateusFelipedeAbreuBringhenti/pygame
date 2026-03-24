import pygame
from config import ALTURA_TELA, COR_BRANCO

class Raquete:

    def __init__(self, x, y, largura=10, altura=60, velocidade=5):
        self.rect = pygame.Rect(x, y, largura, altura)
        self.velocidade = velocidade

    def mover_cima(self):
        if self.rect.top > 0:
            self.rect.y -= self.velocidade

    def mover_baixo(self):
        if self.rect.bottom < ALTURA_TELA:
            self.rect.y += self.velocidade

    def desenhar(self, tela):
        pygame.draw.rect(tela, COR_BRANCO, self.rect)
