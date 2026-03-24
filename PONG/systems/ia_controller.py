import random

class IAController:

    def __init__(self, raquete, bola, velocidade, erro):
        self.raquete = raquete
        self.bola = bola
        self.velocidade = velocidade
        self.erro = erro

    def atualizar(self):
        alvo = self.bola.rect.centery + random.randint(-self.erro, self.erro)

        if self.raquete.rect.centery < alvo:
            self.raquete.rect.y += self.velocidade
        elif self.raquete.rect.centery > alvo:
            self.raquete.rect.y -= self.velocidade
