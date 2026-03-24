# Pong Refatorado (Python + Pygame)

Projeto desenvolvido com foco em **refatoração de código**, aplicando boas práticas de engenharia de software como separação de responsabilidades e princípios SOLID.

---

## Objetivo

Transformar um código monolítico em uma aplicação:

- Modular
- Legível
- Escalável
- Fácil de manter

---

## Conceitos Aplicados

- SRP (Responsabilidade Única)
- Separação de responsabilidades
- Baixo acoplamento
- Organização por camadas
- Clean Code

---

## Funcionalidades

- Menu inicial com seleção de dificuldade  
- IA com comportamento ajustável  
- Sistema de pontuação  
- Colisão entre objetos  
- Controle via teclado  

---

## Detalhes do projeto

### Inicialização do jogo

```python
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()
```

### Explicação

Essa parte é responsável por inicializar o ambiente do jogo.

- pygame.init() → inicia todos os módulos da biblioteca
- set_mode() → cria a janela do jogo
- set_caption() → define o nome da janela
- clock → controla o FPS (velocidade do jogo)

---

### Criação dos jogadores (raquetes)

```python
player = pygame.Rect(50, HEIGHT//2 - 50, 10, 100)
opponent = pygame.Rect(WIDTH - 60, HEIGHT//2 - 50, 10, 100)
```

### Explicação

As raquetes são representadas por retângulos (Rect).

- Primeiro valor → posição X
- Segundo → posição Y
- Terceiro → largura
- Quarto → altura

Usar Rect facilita:

- colisão
- movimentação
- renderização

---

### Movimento do jogador

```python
keys = pygame.key.get_pressed()
if keys[pygame.K_UP]:
    player.y -= speed
if keys[pygame.K_DOWN]:
    player.y += speed
```

### Explicação

Captura as teclas pressionadas continuamente.
- get_pressed() → retorna todas as teclas pressionadas
- Movimento é feito alterando a posição Y

Isso permite movimento fluido (sem precisar ficar clicando várias vezes).

---

### Movimento da bola

```python
ball.x += ball_speed_x
ball.y += ball_speed_y
```

### Explicação

A bola se move somando velocidade à posição.
Conceito importante:
- Movimento = posição + velocidade

---

### Colisão com raquete

```python
if ball.colliderect(player) or ball.colliderect(opponent):
    ball_speed_x *= -1
```

### Explicação

- colliderect() detecta colisão entre objetos
- Inverte direção horizontal da bola

Isso simula o “rebote” da bola nas raquetes

---

### Sistema de pontuação

```python
if ball.left <= 0:
    opponent_score += 1
    reset_ball()

if ball.right >= WIDTH:
    player_score += 1
    reset_ball()
```

### Explicação

- Se a bola sair da tela → alguém pontua
- A bola é reiniciada

Isso define a regra principal do jogo

---

### Loop principal (game loop)

```python
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(60)
```

### Explicação

Esse é o coração do jogo:

- Captura eventos (fechar, teclado)
- Atualiza tela
- Controla FPS

Todo jogo em Pygame depende desse loop contínuo

---

## Controles

- ↑ / ↓ → mover raquete  
- ESPAÇO → selecionar no menu  

---

## IA do Jogo

A IA é configurada dinamicamente com base na dificuldade:

| Dificuldade | Velocidade | Erro |
|------------|----------|------|
| Fácil      | Baixa    | Alto |
| Difícil    | Alta     | Baixo |

---

## Expansão

O projeto foi estruturado para facilitar a adição de novas funcionalidades, como:

- Sistema de pausa  
- Multiplayer  
- Power-ups  
- Sons  
- Tela de Game Over  

---

## Autor

Mateus Felipe de Abreu Bringhenti

## Licença

Projeto desenvolvido para fins acadêmicos e não, não copiem colegas 😭
