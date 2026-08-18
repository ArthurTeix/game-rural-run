import pygame
from random import randint

pygame.init()

# configurações da tela
tamanho_tela = (462, 606)
largura_tela, altura_tela = tamanho_tela
tela = pygame.display.set_mode(tamanho_tela)

# carrega a imagem de fundo
fundo = pygame.image.load("assets/img/background.png")

# configurações do jogador
largura_jogador = 57
altura_jogador = 114
jogador = pygame.Rect(231, 470, largura_jogador, altura_jogador)

jogador_img = pygame.image.load("assets/img/Robozin.png").convert_alpha()

# redimensiona a imagem pro tamanho do retângulo do jogador
jogador_img = pygame.transform.scale(jogador_img, (largura_jogador, altura_jogador))

# configurações dos obstáculos
largura_obstaculo = 57
altura_obstaculo = 40
velocidade_obstaculo = 1

lista_obstaculos = []  # cada obstáculo é um pygame.Rect

# criar obstáculos periodicamente
criar_obstaculos = pygame.USEREVENT + 1
pygame.time.set_timer(criar_obstaculos, 1100)  # a cada 1seg

# cores
cores = {
    'preto': (0, 0, 0),
    'verde': (0, 255, 0),
    'vermelho': (255, 0, 0)
}

# título do jogo
pygame.display.set_caption("RURAL RUN")

def desenhar_inicio_jogo():
    tela.blit(fundo, (0, 0))

    # desenhando jogador na tela
    tela.blit(jogador_img, jogador)

    # desenhando os obstáculos na tela
    for obstaculo in lista_obstaculos:
        pygame.draw.rect(tela, cores['vermelho'], obstaculo)

def movimento_jogador(evento):
    if (evento.type == pygame.KEYDOWN): # se o evento for de pressionar tecla

        if (evento.key == pygame.K_RIGHT) and (jogador.x < 400):
            jogador.x += 1 

        if (evento.key == pygame.K_LEFT) and (jogador.x > 3):
            jogador.x -= 1

def criar_obstaculo():
    x = randint(30, 405) # obstaculos nascem aleatoriamente entre o px 30 e 405 de largura
    novo_obstaculo = pygame.Rect(x, -altura_obstaculo, largura_obstaculo, altura_obstaculo)
    lista_obstaculos.append(novo_obstaculo)

def mover_obstaculos():
    for obstaculo in lista_obstaculos:
        obstaculo.y += velocidade_obstaculo

    # remove obstáculos que já saíram da tela
    lista_obstaculos[:] = [obstaculo for obstaculo in lista_obstaculos if obstaculo.y < altura_tela]

def verificar_colisao_o():
    for obstaculo in lista_obstaculos:
        if jogador.colliderect(obstaculo):
            return True
    return False

fim_de_jogo = False
while not fim_de_jogo:
    desenhar_inicio_jogo()

    for evento in pygame.event.get():
        if (evento.type == pygame.QUIT):
            fim_de_jogo = True 

        if (evento.type == criar_obstaculos):
            quantidade_por_vez = 2
            for quant in range(quantidade_por_vez):
                criar_obstaculo()

    movimento_jogador(evento)

    mover_obstaculos()

    if verificar_colisao_o():
        fim_de_jogo = True

    pygame.time.wait(1) 
    pygame.display.flip()

pygame.quit()