import pygame

pygame.init()

# configurações da tela
tamanho_tela = (462, 606)
tela = pygame.display.set_mode(tamanho_tela)

# carrega a imagem de fundo
fundo = pygame.image.load("assets/img/BackgroundSECO.png")

# configurações do jogador
largura_jogador = 57
altura_jogador = 114
jogador = pygame.Rect(231, 470, largura_jogador, altura_jogador)

jogador_img = pygame.image.load("assets/img/Robozin.png").convert_alpha()

# redimensiona a imagem pro tamanho do retângulo do jogador
jogador_img = pygame.transform.scale(jogador_img, (largura_jogador, altura_jogador))

# cores
cores = {
    'verde': (0, 255, 0),
    'preto': (0, 0, 0)

}

# título do jogo
pygame.display.set_caption("RURAL RUN")

def desenhar_inicio_jogo():
    tela.blit(fundo, (0, 0))

    # desenhando jogador na tela
    tela.blit(jogador_img, jogador)

def movimento_jogador(evento):
    if (evento.type == pygame.KEYDOWN): # se o evento for de pressionar tecla

        if (evento.key == pygame.K_RIGHT) and (jogador.x < 400):
            jogador.x += 1 

        if (evento.key == pygame.K_LEFT) and (jogador.x > 3):
            jogador.x -= 1

fim_de_jogo = False
while not fim_de_jogo:
    desenhar_inicio_jogo()

    for evento in pygame.event.get():
        if (evento.type == pygame.QUIT):
            fim_de_jogo = True 

    movimento_jogador(evento)

    pygame.time.wait(1) 
    pygame.display.flip()

pygame.quit()