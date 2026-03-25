import pygame
import random
from config import LARGURA_TELA, ALTURA_TELA

class Bola:
    def __init__(self, tamanho=15, wall_sound=None, verdadeira=True):
        self.rect = pygame.Rect(LARGURA_TELA // 2, ALTURA_TELA // 2, tamanho, tamanho)
        self.vel_x = random.choice([-5, 5])
        self.vel_y = random.uniform(-4, 4)
        self.wall_sound = wall_sound

        self.verdadeira = verdadeira
        self.cor = (
            random.randint(50, 255),
            random.randint(50, 255),
            random.randint(50, 255)
        )

    def atualizar(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        if self.rect.top <= 0 or self.rect.bottom >= ALTURA_TELA:
            self.vel_y *= -1
            self.vel_x += random.choice([-1, 1]) * random.uniform(0.5, 2)
            if self.wall_sound:
                self.wall_sound.play()

    def resetar(self):
        self.rect.center = (LARGURA_TELA // 2, ALTURA_TELA // 2)
        self.vel_x = random.choice([-5, 5])
        self.vel_y = random.uniform(-4, 4)

    def desenhar(self, tela):
        pygame.draw.ellipse(tela, self.cor, self.rect)