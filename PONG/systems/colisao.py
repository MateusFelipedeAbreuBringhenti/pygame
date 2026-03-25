class SistemaColisao:

    def __init__(self, bola, jogadores, paddle_sound=None):
        self.bola = bola
        self.jogadores = jogadores
        self.paddle_sound = paddle_sound

    def verificar(self):
        for jogador in self.jogadores:
            if self.bola.rect.colliderect(jogador.rect):
                self.bola.vel_x *= -1
                if self.paddle_sound:
                    self.paddle_sound.play()
                break