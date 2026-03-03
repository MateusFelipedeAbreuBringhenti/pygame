# 🎮 Colisão de Objetos com Condições de Contorno

Simulação desenvolvida em **Python 3.12 utilizando Pygame**, demonstrando colisão entre dois objetos (`Rect`) com tratamento de condições de contorno.

📚 Atividade acadêmica - Computação Gráfica e Tecnologias Imersivas (SINF7NA)
👨‍🏫 Professor: Dr. Rafael Barbosa  

---

## 📌 Objetivo

Implementar:

- Dois objetos (`Rect`) em movimento contínuo
- Colisão entre os objetos
- Colisão com as bordas da janela
- Alteração dinâmica de direção e cor
- Organização e versionamento do projeto com Git e GitHub

---

## 🧠 Conceitos Aplicados

- Game Loop (loop principal de jogos)
- Programação orientada a eventos
- Manipulação de vetores de velocidade
- Condições de contorno
- Detecção de colisão com `colliderect`
- Renderização de texto com Pygame
- Controle de FPS com `Clock`

---

## ⚙️ Tecnologias Utilizadas

- Python 3.12
- Pygame

---

## 📂 Estrutura do Projeto

```
pygame/
|
|-- venv311
|-- README.md
|-- teste-pygame.py
```

---

# 🏗 Estrutura do Código Explicada

## 1️⃣ Inicialização do Pygame

```python
pygame.init()

largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Janela')
```

### Aqui:

- Inicializamos o Pygame  
- Definimos tamanho da janela  
- Criamos a superfície principal de renderização  

---

## 2️⃣ Criação dos Textos como Objetos Rect

```python
texto = fonte.render('Mateus', True, BRANCO)
texto_rect = texto.get_rect()
```

### Cada texto possui:

- Uma superfície visual (`Surface`)  
- Um retângulo (`Rect`) que define posição e colisão  

### O `Rect` é responsável por:

- Detectar colisão  
- Definir limites  
- Atualizar posição  

---

## 3️⃣ Velocidade Aleatória Inicial

```python
velocidade_x1 = random.randint(-2,2)
velocidade_y1 = random.randint(-2,2)
```

### Cada objeto possui:

- Velocidade horizontal (x)  
- Velocidade vertical (y)  

### Evita-se velocidade `(0,0)` para impedir objetos parados:

```python
while velocidade_x1 == 0 and velocidade_y1 == 0:
    velocidade_x1 = random.randint(-2,2)
    velocidade_y1 = random.randint(-2,2)
```

---

## 4️⃣ Game Loop (Coração do Programa)

```python
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
```

### O loop executa continuamente:

- Captura eventos  
- Atualiza posições  
- Verifica colisões  
- Renderiza objetos  
- Atualiza tela  

---

## 5️⃣ Movimento dos Objetos

```python
texto_rect.x += velocidade_x1
texto_rect.y += velocidade_y1
```

### Movimento baseado em:

```
posição += velocidade
```

---

## 6️⃣ Colisão com as Bordas (Condições de Contorno)

### Exemplo:

```python
if texto_rect.right >= largura:
    texto_rect.right = largura
    velocidade_x1 = random.randint(-2,0)
```

### Quando o objeto atinge a borda:

- A posição é corrigida  
- A direção é alterada  
- A velocidade é recalculada  

Isso simula o efeito clássico do DVD.

---

## 7️⃣ Colisão Entre Objetos

```python
if texto_rect.colliderect(texto_2_rect):
    velocidade_x1 = random.randint(-2,2)
    velocidade_y1 = random.randint(-2,2)
    velocidade_x2 = random.randint(-2,2)
    velocidade_y2 = random.randint(-2,2)
```

### Quando ocorre colisão:

- Novas velocidades são atribuídas  
- Ambos os objetos mudam direção  

---

## 8️⃣ Alteração Dinâmica de Cor

```python
cor_atual = (
    random.randint(1,255),
    random.randint(1,255),
    random.randint(1,255)
)
```

### Após colisão:

- Uma nova cor RGB é gerada  
- Os textos são re-renderizados com essa cor  

---

## 9️⃣ Controle de FPS

```python
clock.tick(240)
```

### Limita o programa a 240 frames por segundo, garantindo:

- Estabilidade  
- Consistência na simulação  

---

## ▶️ Como Executar

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/MateusFelipedeAbreuBringhenti/pygame.git
cd pygame
```

### 2️⃣ Instalar o Pygame

Caso não tenha instalado:

```bash
pip install pygame
```

### 3️⃣ Executar o projeto

```bash
python teste-pygame.py
```

---

## 🎮 Funcionamento

- Dois textos se movimentam aleatoriamente pela tela
- Ao colidir com as bordas:
- A direção é ajustada
- Ao colidir entre si:
- Novas velocidades são atribuídas
- A cor dos textos é alterada dinamicamente

A simulação utiliza lógica semelhante ao efeito clássico de tela DVD.

---

## 👨‍💻 Autor

Mateus Felipe de Abreu Bringhenti  

---

## 📜 Licença

Projeto desenvolvido para fins acadêmicos e não, não copiem colegas 😭