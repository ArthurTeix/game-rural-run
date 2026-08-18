import pygame

pygame.init()

# configurações da tela
tamanho_tela = (462, 606)
tela = pygame.display.set_mode(tamanho_tela)

# cores
cores = {
    'preto': (0, 0, 0)
}

# título do jogo
pygame.display.set_caption("RURAL RUN")

def desenhar_inicio_jogo():
    tela.fill(cores['preto'])

fim_de_jogo = False
while not fim_de_jogo:
    for evento in pygame.event.get():
        if (evento.type == pygame.QUIT):
            fim_de_jogo = True 

    pygame.time.wait(1) 
    pygame.display.flip()

pygame.quit()