# importing libraries
import pygame

# game variables
WIDTH, HEIGHT = 1280, 720
GAME_OVER = False

# initializing game window
pygame.init()
screen = pygame.display.set_mode((1280, 720))
player_pos = pygame.Vector2(600, 400)
screen.fill([204, 169, 221])

# function to game duration
def check_time():
    return pygame.time.get_ticks()

# game state loop, runs until game is over
while not GAME_OVER:

    screen.fill([204, 169, 221])

    # movement tech, checks for key presses and moves avatar accordingly
    keys = pygame.key.get_pressed()
    if player_pos.y > 0 and keys[pygame.K_w]:
        player_pos.y -= 5
    if player_pos.y < HEIGHT and keys[pygame.K_s]:
        player_pos.y += 5
    if player_pos.x > 0 and keys[pygame.K_a]:
        player_pos.x -= 5
    if player_pos.x < WIDTH and keys[pygame.K_d]:
        player_pos.x += 5

    # renders display according to new avatar location
    pygame.event.pump()
    pygame.draw.circle(screen, "white", player_pos, 10)
    pygame.display.flip()

    # checks if game is over
    if check_time() > 10000:
        GAME_OVER = True

pygame.quit()
