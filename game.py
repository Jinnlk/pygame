# importing libraries
import pygame


# main menu function
def main_menu(pygame, width, height):

    screen = pygame.display.set_mode((width, height))
    font = pygame.font.SysFont("Comic Sans MS", 30)

    while True:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            break

        screen.fill([204, 169, 221])
        title = font.render('press "s" to start!', False, (0, 0, 0))
        screen.blit(title, (width / 2 - 30, height / 2 - 30))
        pygame.event.pump()
        pygame.display.flip()


# start game function
def start_game(pygame, width, height):

    GAME_OVER = False

    screen = pygame.display.set_mode((width, height))
    player_pos = pygame.Vector2(width / 2, height / 2)
    screen.fill([204, 169, 221])

    # game state loop, runs until game is over
    while not GAME_OVER:

        screen.fill([204, 169, 221])

        # movement tech, checks for key presses and moves avatar accordingly
        keys = pygame.key.get_pressed()
        if player_pos.y > 0 and keys[pygame.K_w]:
            player_pos.y -= 5
        if player_pos.y < height and keys[pygame.K_s]:
            player_pos.y += 5
        if player_pos.x > 0 and keys[pygame.K_a]:
            player_pos.x -= 5
        if player_pos.x < width and keys[pygame.K_d]:
            player_pos.x += 5

        # renders display according to new avatar location
        pygame.event.pump()
        pygame.draw.circle(screen, "white", player_pos, 10)
        pygame.display.flip()

        # checks if game is over
        if check_time() > 10000:
            GAME_OVER = True

    pygame.quit()


# function to game duration
def check_time():
    return pygame.time.get_ticks()
