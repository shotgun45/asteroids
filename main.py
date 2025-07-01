# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    pygame.init()
    is_running = True
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
    # draw the background    
    screen.fill(000000)

    # update the screen
    pygame.display.flip()

    '''
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    '''

if __name__ == "__main__":
    main()