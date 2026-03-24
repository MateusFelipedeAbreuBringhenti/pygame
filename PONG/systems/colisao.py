class SistemaColisao:

    def __init__(self, bola, jogadores):
        self.bola = bola
        self.jogadores = jogadores

    def verificar(self):
        for jogador in self.jogadores:
            if self.bola.rect.colliderect(jogador.rect):
                self.bola.vel_x *= -1
                break