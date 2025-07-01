import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player

def main():
    pygame.init()
    is_running = True
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # clock and delta time to control the frame rate
    clock = pygame.time.Clock()
    dt = 0

    # groups
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()

    # assign groups to Player containers
    Player.containers = updatables, drawables

    # create player (it will auto-add to the groups)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

        # draw the background
        screen.fill((0, 0, 0))

        # update logic
        updatables.update(dt)

        # draw everything
        for drawable in drawables:
            drawable.draw(screen)

        # update the screen
        pygame.display.flip()

        # limit frame rate to 60 FPS
        dt = clock.tick(60) / 1000.0

if __name__ == "__main__":
    main()
