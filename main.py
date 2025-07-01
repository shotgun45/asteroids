import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
    pygame.init()
    is_running = True
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    # groups
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # assign groups to containers
    Player.containers = updatables, drawables
    Asteroid.containers = asteroids, updatables, drawables
    AsteroidField.containers = updatables
    Shot.containers = shots, updatables, drawables

    # create player (automatically added to groups)
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    # create asteroid field
    asteroid_field = AsteroidField()

    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot()

        # draw the background
        screen.fill((0, 0, 0))

        # update logic
        updatables.update(dt)

        # draw everythingimport pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def game_loop(screen, clock):
    dt = 0

    # groups
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # assign groups to containers
    Player.containers = updatables, drawables
    Asteroid.containers = asteroids, updatables, drawables
    AsteroidField.containers = updatables
    Shot.containers = shots, updatables, drawables

    # create player (automatically added to groups)
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    # create asteroid field
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False  # signal to quit
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot()

        # draw the background
        screen.fill((0, 0, 0))

        # update logic
        updatables.update(dt)

        # draw everything
        for drawable in drawables:
            drawable.draw(screen)

        # check for collisions
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                return True  # signal game over to restart

        # check for collisions between asteroids and shots
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    asteroid.split()
                    shot.kill()

        # update the screen
        pygame.display.flip()

        # limit frame rate to 60 FPS
        dt = clock.tick(60) / 1000.0

def main():
    pygame.init()
    is_running = True
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    while is_running:
        game_over = game_loop(screen, clock)
        if not game_over:
            is_running = False  # user closed the window
            break

        # show game over message
        font = pygame.font.SysFont(None, 48)
        message = font.render("Game Over! Press R to restart or Q to quit.", True, (255, 0, 0))
        screen.fill((0, 0, 0))
        screen.blit(message, (SCREEN_WIDTH // 2 - message.get_width() // 2, SCREEN_HEIGHT // 2))
        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    is_running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        waiting = False  # restart game loop
                    elif event.key == pygame.K_q:
                        waiting = False
                        is_running = False  # exit game

if __name__ == "__main__":
    main()

    for drawable in drawables:
        drawable.draw(screen)

    # check for collisions
    for asteroid in asteroids:
        if asteroid.collides_with(player):
            print("Game over!")
            sys.exit()

    # check for collisions between asteroids and shots
    for asteroid in asteroids:
        for shot in shots:
            if asteroid.collides_with(shot):
                asteroid.split()
                shot.kill()
    
    # update the screen
    pygame.display.flip()

    # limit frame rate to 60 FPS
    dt = clock.tick(60) / 1000.0

if __name__ == "__main__":
    main()
