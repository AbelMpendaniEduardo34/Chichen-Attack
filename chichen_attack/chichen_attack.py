import pygame
import random
import os

# Inicializar o Pygame
pygame.init()

# Definir a tela
LARGURA_TELA = 800
ALTURA_TELA = 600
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Chicken Attack: Galaxy Shooter")

# Definir cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)

# Definir o relógio
clock = pygame.time.Clock()

# Carregar imagens (coloque as imagens na pasta 'imagens')
dir_imagens = "imagens"
nave_img = pygame.image.load(os.path.join(dir_imagens, "1.png"))
nave_img = pygame.transform.scale(nave_img, (50, 50))
galinha_img = pygame.image.load(os.path.join(dir_imagens, "1B.png"))
galinha_img = pygame.transform.scale(galinha_img, (50, 50))
laser_img = pygame.image.load(os.path.join(dir_imagens, "beams.png"))
laser_img = pygame.transform.scale(laser_img, (10, 30))

# Variáveis do jogador  
nave_x = LARGURA_TELA // 2 - 25
nave_y = ALTURA_TELA - 60
nave_velocidade = 7

# Variáveis do laser
lasers = []
laser_velocidade = 10

# Variáveis dos inimigos
inimigos = []
inimigo_velocidade = 3

# Função para desenhar o jogador
def desenhar_nave(x, y):
    tela.blit(nave_img, (x, y))

# Função para desenhar o laser
def desenhar_lasers(lasers):
    for laser in lasers:
        tela.blit(laser_img, (laser.x, laser.y))

# Função para desenhar inimigos
def desenhar_inimigos(inimigos):
    for inimigo in inimigos:
        tela.blit(galinha_img, (inimigo.x, inimigo.y))

# Função para verificar colisão
def verificar_colisao(obj1, obj2):
    return obj1.colliderect(obj2)

# Função principal do jogo
def loop_jogo():
    rodando = True
    pontuacao = 0
    nave_x = LARGURA_TELA // 2 - 25
    nave_y = ALTURA_TELA - 60
    lasers = []
    inimigos = []

    while rodando:
        tela.fill(PRETO)  # Preencher a tela com preto

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        # Movimento do jogador
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and nave_x - nave_velocidade > 0:
            nave_x -= nave_velocidade
        if teclas[pygame.K_RIGHT] and nave_x + nave_velocidade < LARGURA_TELA - 50:
            nave_x += nave_velocidade
        if teclas[pygame.K_SPACE]:
            # Disparar laser
            if len(lasers) < 5:  # Limitar a quantidade de lasers na tela
                laser_rect = pygame.Rect(nave_x + 20, nave_y, 10, 30)
                lasers.append(laser_rect)

        # Movimento do laser
        for laser in lasers[:]:
            laser.y -= laser_velocidade
            if laser.y < 0:
                lasers.remove(laser)

        # Adicionar inimigos
        if random.randint(0, 50) == 0:  # Adiciona inimigos de tempos em tempos
            inimigo_x = random.randint(0, LARGURA_TELA - 50)
            inimigo_rect = pygame.Rect(inimigo_x, 0, 50, 50)
            inimigos.append(inimigo_rect)

        # Movimento dos inimigos
        for inimigo in inimigos[:]:
            inimigo.y += inimigo_velocidade
            if inimigo.y > ALTURA_TELA:
                inimigos.remove(inimigo)
          # Verificar colisões entre laser e inimigo
        for inimigo in inimigos[:]:
            for laser in lasers[:]:
                if verificar_colisao(inimigo, laser):
                    inimigos.remove(inimigo)
                    lasers.remove(laser)
                    pontuacao += 1

        # Verificar colisão entre inimigo e jogador
        for inimigo in inimigos:
            if verificar_colisao(inimigo, pygame.Rect(nave_x, nave_y, 50, 50)):
                rodando = False

        # Desenhar tudo na tela
        desenhar_nave(nave_x, nave_y)
        desenhar_lasers(lasers)
        desenhar_inimigos(inimigos)

        # Exibir pontuação
        fonte = pygame.font.SysFont(None, 36)
        texto_pontuacao = fonte.render(f'Pontuação: {pontuacao}', True, BRANCO)
        tela.blit(texto_pontuacao, (10, 10))

        # Atualizar a tela
        pygame.display.flip()
        clock.tick(60)  # FPS do jogo

    pygame.quit()

# Iniciar o jogo
loop_jogo()
