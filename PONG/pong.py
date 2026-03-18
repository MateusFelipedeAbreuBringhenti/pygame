import pygame
import sys
import random

pygame.init()

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

LARGURA = 800
ALTURA = 600

class Raquete:
    def __init__(self, x, y, largura=10, altura=60, velocidade=5):
        self.rect = pygame.Rect(x, y, largura, altura)
        self.velocidade = velocidade

    def move_up(self):
        if self.rect.top > 0:
            self.rect.y -= self.velocidade

    def move_down(self):
        if self.rect.bottom < ALTURA:
            self.rect.y += self.velocidade

    def draw(self, tela):
        pygame.draw.rect(tela, BRANCO, self.rect)

class Bola:
    def __init__(self, tamanho=15):
        self.rect = pygame.Rect(LARGURA // 2, ALTURA // 2, tamanho, tamanho)
        self.vel_x = 5
        self.vel_y = 5

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        if self.rect.top <= 0 or self.rect.bottom >= ALTURA:
            self.vel_y *= -1

    def reset(self):
        self.rect.center = (LARGURA // 2, ALTURA // 2)
        self.vel_x *= -1

    def draw(self, tela):
        pygame.draw.ellipse(tela, BRANCO, self.rect)

class Pontos:
    def __init__(self):
        self.p1 = 0
        self.p2 = 0
        self.font = pygame.font.SysFont(None, 40)

    def draw(self, tela):
        text = self.font.render(f"{self.p1} - {self.p2}", True, BRANCO)
        tela.blit(text, (LARGURA // 2 - 30, 20))

class Jogo:
    def __init__(self):
        self.tela = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption("Pong")

        self.clock = pygame.time.Clock()

        self.player1 = Raquete(15, ALTURA // 2 - 30)
        self.player2 = Raquete(LARGURA - 25, ALTURA // 2 - 30)
        self.ball = Bola()
        self.score = Pontos()

        self.dificuldade = "facil"

    def menu(self):
        fonte_titulo = pygame.font.SysFont(None, 70)
        fonte_opcao = pygame.font.SysFont(None, 40)
        fonte_instrucao = pygame.font.SysFont(None, 25)

        opcoes = ["Fácil", "Difícil"]
        selecionado = 0

        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_UP:
                        selecionado = (selecionado - 1) % len(opcoes)
                    if evento.key == pygame.K_DOWN:
                        selecionado = (selecionado + 1) % len(opcoes)
                    if evento.key == pygame.K_SPACE:
                        if selecionado == 0:
                            self.dificuldade = "facil"
                        else:
                            self.dificuldade = "dificil"
                        return

            self.tela.fill(PRETO)

            titulo = fonte_titulo.render("PONG", True, BRANCO)
            self.tela.blit(titulo, (LARGURA // 2 - 100, 120))

            for OpcaoDeJogo, opcao in enumerate(opcoes):
                cor = BRANCO
                texto = fonte_opcao.render(opcao, True, cor)

                x = LARGURA // 2 - 40
                y = 280 + OpcaoDeJogo * 50

                self.tela.blit(texto, (x, y))

                if OpcaoDeJogo == selecionado:
                    seta = fonte_opcao.render(">", True, BRANCO)
                    self.tela.blit(seta, (x - 30, y))

            tempo = pygame.time.get_ticks()
            if tempo % 2000 < 1000:
                instrucao = fonte_instrucao.render("Pressione ESPAÇO para jogar", True, BRANCO)
                self.tela.blit(instrucao, (LARGURA // 2 - 120, 450))

            pygame.display.flip()
            self.clock.tick(60)

    def handle_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.player1.move_up()
        if keys[pygame.K_DOWN]:
            self.player1.move_down()

    def ai(self):
        alvo = self.ball.rect.centery

        if self.dificuldade == "facil":
            velocidade = 3
            erro = 40
        else:
            velocidade = 7
            erro = 5

        alvo += random.randint(-erro, erro)

        if self.player2.rect.centery < alvo:
            self.player2.rect.y += velocidade
        elif self.player2.rect.centery > alvo:
            self.player2.rect.y -= velocidade

        if self.player2.rect.top < 0:
            self.player2.rect.top = 0
        if self.player2.rect.bottom > ALTURA:
            self.player2.rect.bottom = ALTURA

    def check_collision(self):
        for jogador in (self.player1, self.player2):
            if self.ball.rect.colliderect(jogador.rect):
                self.ball.vel_x *= -1
                break

    def check_score(self):
        if self.ball.rect.left <= 0 or self.ball.rect.right >= LARGURA:
            if self.ball.rect.left <= 0:
                self.score.p2 += 1
            else:
                self.score.p1 += 1
            self.ball.reset()

    def draw(self):
        self.tela.fill(PRETO)

        self.player1.draw(self.tela)
        self.player2.draw(self.tela)
        self.ball.draw(self.tela)
        self.score.draw(self.tela)

        pygame.display.flip()

    def run(self):
        self.menu()

        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.handle_input()
            self.ai()
            self.ball.update()
            self.check_collision()
            self.check_score()
            self.draw()

            self.clock.tick(60)

if __name__ == "__main__":
    jogo = Jogo()
    jogo.run()