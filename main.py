import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import game_state

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

    font = pygame.font.SysFont(None, 36)

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

        # display the score
        score_text = font.render(f"Score: {game_state.score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        # display the timer
        timer_text = font.render(f"Time: {int(game_state.game_time)}s", True, (255, 255, 255))
        screen.blit(timer_text, (10, 40))

        # update the screen
        pygame.display.flip()

        # limit frame rate to 60 FPS
        dt = clock.tick(60) / 1000.0  # seconds
        game_state.game_time += dt

def title_screen(screen):
    import random
    from asteroid import Asteroid

    font_title = pygame.font.SysFont("arial", 48, bold=True)
    font_sub = pygame.font.SysFont("arial", 36)
    title = font_title.render("A REALLY SKETCHY VERSION OF ASTEROIDS", True, (255, 255, 255))
    prompt = font_sub.render("Press SPACE to begin or Q to quit", True, (200, 200, 200))

    # Create demo asteroids for the title screen
    demo_asteroids = []
    for _ in range(8):
        x = random.uniform(0, SCREEN_WIDTH)
        y = random.uniform(0, SCREEN_HEIGHT)
        radius = random.choice([20, 30, 40])
        asteroid = Asteroid(x, y, radius)
        angle = random.uniform(0, 360)
        speed = random.uniform(30, 80)
        asteroid.velocity = pygame.Vector2(speed, 0).rotate(angle)
        demo_asteroids.append(asteroid)

    clock = pygame.time.Clock()
    waiting = True
    while waiting:
        dt = clock.tick(60) / 1000.0  # seconds

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    exit()

        # Update demo asteroids
        for asteroid in demo_asteroids:
            asteroid.update(dt)

        # Draw background and asteroids
        screen.fill((0, 0, 0))
        for asteroid in demo_asteroids:
            asteroid.draw(screen)

        # Draw title and prompt
        screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, SCREEN_HEIGHT // 2 - 100))
        screen.blit(prompt, (SCREEN_WIDTH // 2 - prompt.get_width() // 2, SCREEN_HEIGHT // 2 + 20))
        pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    exit()

def main():
    pygame.init()
    is_running = True
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    title_screen(screen)

    while is_running:
        game_over = game_loop(screen, clock)
        if not game_over:
            is_running = False  # user closed the window
            break

        # show game over message
        font = pygame.font.SysFont("arial", 48, bold=True)
        message1 = font.render("Game Over!", True, (255, 0, 0))
        message2 = font.render("Press R to restart or Q to quit.", True, (255, 0, 0))
        score_text = font.render(f"Final Score: {game_state.score}", True, (255, 255, 255))
        timer_text = font.render(f"Time Survived: {int(game_state.game_time)}s", True, (255, 255, 255))
        screen.fill((0, 0, 0))

        # Stack all messages vertically, centered
        elements = [score_text, timer_text, message1, message2]
        total_height = sum(e.get_height() for e in elements) + 30  # 10px spacing between lines
        start_y = (SCREEN_HEIGHT - total_height) // 2

        y = start_y
        for i, e in enumerate(elements):
            screen.blit(e, (SCREEN_WIDTH // 2 - e.get_width() // 2, y))
            y += e.get_height() + 10  # 10px vertical spacing

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
