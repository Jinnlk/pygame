import pygame

WIDTH, HEIGHT = 1280, 720
GAME_OVER = False

pygame.init()
screen = pygame.display.set_mode((1280, 720))


def check_time():
    return pygame.time.get_ticks()


while not GAME_OVER:

    screen.fill("purple")
    pygame.display.flip()

    if check_time() > 5000:
        GAME_OVER = True

pygame.quit()
