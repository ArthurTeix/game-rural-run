import pygame

pygame.init()

# configurações da tela
tamanho_tela = (462, 606)
tela = pygame.display.set_mode(tamanho_tela)

# carrega a imagem de fundo
fundo = pygame.image.load("assets/img/BackgroundSECO.png")

# configurações do jogador
# largura_jogador = 38
# altura_jogador = 76
largura_jogador = 76
altura_jogador = 152
jogador = pygame.Rect(231, 450, largura_jogador, altura_jogador)

# cores
cores = {
    'azul': (0, 255, 0),
    'preto': (0, 0, 0)

}

# título do jogo
pygame.display.set_caption("RURAL RUN")

def desenhar_inicio_jogo():
    tela.blit(fundo, (0, 0))

    pygame.draw.rect(tela, cores['azul'], jogador)

fim_de_jogo = False
while not fim_de_jogo:
    for evento in pygame.event.get():
        if (evento.type == pygame.QUIT):
            fim_de_jogo = True 

    desenhar_inicio_jogo()

    pygame.time.wait(1) 
    pygame.display.flip()

pygame.quit()