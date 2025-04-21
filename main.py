# this allows us to use code from
# the open-source pygame library
# throughout this file
from constants import *

import pygame

print ("Starting Asteroids!")
print ("Screen width:", SCREEN_WIDTH)
print("Screen height:", SCREEN_HEIGHT)


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Set the game loop

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        pygame.display.flip()

if __name__ == "__main__":
    main()
