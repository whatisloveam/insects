# Setup Python ----------------------------------------------- #
import pygame
import sys
import os
from helper.settings import *
from game import Game

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100,32) # windows position
pygame.init()
pygame.display.set_caption(WINDOW_NAME)
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),0,32)

mainClock = pygame.time.Clock()

# Creation -------------------------------------------------------- #
game = Game(SCREEN)

# Loop ------------------------------------------------------------ #
while True:
    # events ----------------------------------------------------- #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
    # Update ------------------------------------------------------ #
    game.update()
    pygame.display.update()
    mainClock.tick(FPS)