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