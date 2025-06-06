import pygame
import random
import sys
import os
import time

# Inicialização do Pygame
pygame.init()

# Caminho da pasta atual
base_path = os.path.dirname(os.path.abspath(__file__))
imagens_path = os.path.join(base_path, "imagens")

# Configurações da tela
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Bruxo Invaders - Lateral")

# Cores
branco = (255, 255, 255)
amarelo = (255, 255, 0)
vermelho = (255, 0, 0)
verde = (0, 255, 0)

# Fonte para pontuação
fonte = pygame.font.SysFont("Arial", 24)
pontuacao = 0

# Taxa de disparo dos vilões (um tiro a cada 2 segundos)
cadencia_tiro_vilao = 2

# Vida do jogador
vida = 100
dano_tiro_vilao = 10

# Carregar a imagem do fundo
try:
    fundo = pygame.image.load(os.path.join(imagens_path, "fundo.png.jpg"))
    fundo = pygame.transform.scale(fundo, (largura, altura))
except:
    print("Erro: Não foi possível carregar a imagem de fundo.")
    sys.exit()

# Carregar a imagem do bruxo (jogador)
try:
    bruxo_imagem = pygame.image.load(os.path.join(imagens_path, "bruxo.png.png")).convert_alpha()
    bruxo_imagem = pygame.transform.scale(bruxo_imagem, (60, 60))
except:
    print("Erro: Não foi possível carregar a imagem do bruxo.")
    sys.exit()

# Carregar a imagem do tiro do bruxo
try:
    tiro_imagem = pygame.image.load(os.path.join(imagens_path, "tiro.png.png")).convert_alpha()
    tiro_imagem = pygame.transform.scale(tiro_imagem, (30, 10))
except:
    print("Erro: Não foi possível carregar a imagem do tiro.")
    sys.exit()

# Carregar a imagem do vilão
try:
    vilao_imagem = pygame.image.load(os.path.join(imagens_path, "vilao.png.jpg")).convert_alpha()
    vilao_imagem = pygame.transform.scale(vilao_imagem, (50, 50))
except:
    print("Erro: Não foi possível carregar a imagem do vilão.")
    sys.exit()

# Configurações do Bruxo (Jogador)
bruxo_largura, bruxo_altura = 60, 60
bruxo_x = 20  # Posição fixa no canto esquerdo
bruxo_y = altura // 2
bruxo_velocidade = 5

# Feitiços do Bruxo e dos Vilões
feiticamentos = []
tiros_vilao = []
feitico_velocidade = 7
tiro_vilao_velocidade = 5

# Vilões
viloes = []
vilao_largura, vilao_altura = 50, 50
num_viloes = 5
vilao_velocidade = 3

# Função para criar vilões
def criar_vilao():
    x = largura  # Surgem na direita
    y = random.randint(0, altura - vilao_altura)
    return pygame.Rect(x, y, vilao_largura, vilao_altura)

# Função para desenhar a barra de vida
def desenhar_barra_vida(vida):
    largura_barra = 200
    altura_barra = 20
    preenchimento = int((vida / 100) * largura_barra)
    pygame.draw.rect(tela, vermelho, (10, 40, largura_barra, altura_barra))
    pygame.draw.rect(tela, verde, (10, 40, preenchimento, altura_barra))

# Função para desenhar na tela
def desenhar():
    tela.blit(fundo, (0, 0))  # Fundo

    # Desenhar o Bruxo (Jogador)
    tela.blit(bruxo_imagem, (bruxo_x, bruxo_y))

    # Desenhar os feitiços do bruxo
    for feitico in feiticamentos:
        tela.blit(tiro_imagem, (feitico.x, feitico.y))

    # Desenhar os tiros dos vilões
    for tiro in tiros_vilao:
        pygame.draw.rect(tela, amarelo, tiro)

    # Desenhar os vilões
    for vilao in viloes:
        tela.blit(vilao_imagem, (vilao.x, vilao.y))

    # Desenhar a barra de vida
    desenhar_barra_vida(vida)

    # Exibir a pontuação
    texto = fonte.render(f"Pontos: {pontuacao}", True, branco)
    tela.blit(texto, (10, 10))

    pygame.display.flip()

# Função principal do jogo
def jogo():
    global pontuacao, bruxo_y, vida
    clock = pygame.time.Clock()
    rodando = True
    ultimo_tiro_vilao = time.time()

    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Verifica se a tecla espaço foi pressionada
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    feitico = pygame.Rect(bruxo_x + bruxo_largura, bruxo_y + bruxo_altura // 2, 30, 10)
                    feiticamentos.append(feitico)

        # Movimento do Bruxo
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_UP] and bruxo_y > 0:
            bruxo_y -= bruxo_velocidade
        if teclas[pygame.K_DOWN] and bruxo_y < altura - bruxo_altura:
            bruxo_y += bruxo_velocidade

        # Criar novos vilões
        if len(viloes) < num_viloes:
            viloes.append(criar_vilao())

        # Movimento e colisão dos vilões
        for vilao in viloes[:]:
            vilao.x -= vilao_velocidade

            # Tiro do vilão
            if time.time() - ultimo_tiro_vilao > cadencia_tiro_vilao:
                tiro = pygame.Rect(vilao.x, vilao.y + vilao_altura // 2, 10, 5)
                tiros_vilao.append(tiro)
            ultimo_tiro_vilao = time.time()

            # Colisão com feitiços
            for feitico in feiticamentos[:]:
                if vilao.colliderect(feitico):
                    viloes.remove(vilao)
                    feiticamentos.remove(feitico)
                    pontuacao += 10

        # Verificar se o jogador foi atingido por um tiro
        for tiro in tiros_vilao[:]:
            tiro.x -= tiro_vilao_velocidade
            if tiro.colliderect(pygame.Rect(bruxo_x, bruxo_y, bruxo_largura, bruxo_altura)):
                vida -= dano_tiro_vilao
                tiros_vilao.remove(tiro)
                if vida <= 0:
                    print("Game Over! Vida esgotada.")
                    rodando = False

        desenhar()
        clock.tick(30)

jogo()
pygame.quit()
 