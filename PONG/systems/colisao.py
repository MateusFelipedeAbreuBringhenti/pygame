import random

class SistemaColisao:

    def __init__(self, bola, jogadores, paddle_sound=None):
        self.bola = bola
        self.jogadores = jogadores
        self.paddle_sound = paddle_sound

    def verificar(self):
        for jogador in self.jogadores:
            if self.bola.rect.colliderect(jogador.rect):
                self.bola.vel_x *= -1
                self.bola.vel_y = random.choice([-1, 1]) * random.uniform(2, 6)
                if self.bola.vel_x > 0:
                    self.bola.rect.left = jogador.rect.right
                else:
                    self.bola.rect.right = jogador.rect.left
                if self.paddle_sound:
                    self.paddle_sound.play()

                break

    def limitar_velocidade(self):
        max_vel = 10

        if self.bola.vel_x > max_vel:
            self.bola.vel_x = max_vel
        if self.bola.vel_x < -max_vel:
            self.bola.vel_x = -max_vel

        if self.bola.vel_y > max_vel:
            self.bola.vel_y = max_vel
        if self.bola.vel_y < -max_vel:
            self.bola.vel_y = -max_vel