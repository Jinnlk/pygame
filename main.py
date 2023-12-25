# importing game function
import game
import pygame

# game variables
width, height = 1280, 720
pygame.init()

# start the game!
game.main_menu(pygame, width, height)
game.start_game(pygame, width, height)
