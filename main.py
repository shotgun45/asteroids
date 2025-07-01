import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player

def main():
    pygame.init()
    is_running = True
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # clock and delta time to control the frame rate
    clock = pygame.time.Clock()
    dt = 0

    # groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # classes in the groups
    Player.containers = updatable, drawable

    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

        # draw the background
        screen.fill((0, 0, 0))

        # update the player
        player.update(dt)

        # draw the player
        player.draw(screen)

        # update the screen
        pygame.display.flip()

        # limit frame rate to 60 FPS
        dt = clock.tick(60) / 1000.0  # convert milliseconds to seconds

if __name__ == "__main__":
    main()
