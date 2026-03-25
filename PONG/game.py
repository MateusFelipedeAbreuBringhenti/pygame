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
        pygame.mixer.init()

        self.tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
        pygame.display.set_caption("Pong v2")

        self.clock = pygame.time.Clock()

        self.paddle_sound = pygame.mixer.Sound("sounds/fahhh_KcgAXfs.wav")
        self.wall_sound = pygame.mixer.Sound("sounds/anime-ahh.wav")
        self.score_sound = pygame.mixer.Sound("sounds/dexter-meme.wav")

        pygame.mixer.music.load("sounds/indian-song.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

        self.jogador1 = Raquete(15, ALTURA_TELA // 2 - 30)
        self.jogador2 = Raquete(LARGURA_TELA - 25, ALTURA_TELA // 2 - 30)

        self.bolas = [Bola(wall_sound=self.wall_sound, verdadeira=True)]
        self.ultimo_spawn = pygame.time.get_ticks()

        self.input = GerenciadorInput(self.jogador1)
        self.pontuacao = GerenciadorPontuacao(score_sound=self.score_sound)

        self.colisao = SistemaColisao(
            None,
            [self.jogador1, self.jogador2],
            paddle_sound=self.paddle_sound
        )

        self.menu = Menu(self.tela)
        self.ia = None

    def configurar_dificuldade(self, dificuldade):
        bola_principal = self.bolas[0]

        if dificuldade == "facil":
            self.ia = IAController(self.jogador2, bola_principal, velocidade=4, erro=30)
        else:
            self.ia = IAController(self.jogador2, bola_principal, velocidade=7, erro=5)

    def executar(self):
        dificuldade = self.menu.executar()
        self.configurar_dificuldade(dificuldade)

        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            tempo_atual = pygame.time.get_ticks()

            self.input.atualizar()
            self.ia.atualizar()

            for bola in self.bolas:
                bola.atualizar()

            for bola in self.bolas:
                self.colisao.bola = bola
                self.colisao.verificar()
                self.colisao.limitar_velocidade()

            for bola in self.bolas:
                if bola.verdadeira:
                    self.pontuacao.atualizar(bola)

            if tempo_atual - self.ultimo_spawn >= 5000 and self.colisao.colidiu:

                novas_bolas = []

                for bola in self.bolas:
                    for _ in range(4):
                        nova = Bola(wall_sound=self.wall_sound, verdadeira=False)
                        nova.rect.center = bola.rect.center
                        novas_bolas.append(nova)

                self.bolas.extend(novas_bolas)
                self.colisao.colidiu = False
                self.ultimo_spawn = tempo_atual

            if len(self.bolas) > 20:
                self.bolas = self.bolas[:20]
            self.tela.fill(COR_PRETO)

            self.jogador1.desenhar(self.tela)
            self.jogador2.desenhar(self.tela)

            for bola in self.bolas:
                bola.desenhar(self.tela)

            self.pontuacao.desenhar(self.tela)

            pygame.display.flip()
            self.clock.tick(FPS)