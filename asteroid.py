import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, SCREEN_WIDTH, SCREEN_HEIGHT
import game_state

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
        # Determine color based on radius
        if self.radius > ASTEROID_MIN_RADIUS * 2:
            self.color = (0, 255, 0)  # Green for large
        elif self.radius > ASTEROID_MIN_RADIUS:
            self.color = (255, 255, 0)  # Yellow for medium
        else:
            self.color = (255, 0, 0)  # Red for small

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

        # Allow asteroids to wrap around the screen
        if self.position.x < -self.radius:
            self.position.x = SCREEN_WIDTH + self.radius
        elif self.position.x > SCREEN_WIDTH + self.radius:
            self.position.x = -self.radius

        if self.position.y < -self.radius:
            self.position.y = SCREEN_HEIGHT + self.radius
        elif self.position.y > SCREEN_HEIGHT + self.radius:
            self.position.y = -self.radius

        # calculate score based on radius
    def split(self):
        if self.radius > ASTEROID_MIN_RADIUS * 2:
            game_state.score += 10
        elif self.radius > ASTEROID_MIN_RADIUS:
            game_state.score += 20
        else:
            game_state.score += 50

        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        split_angle = random.uniform(20, 50)
        chip1_velocity = self.velocity.rotate(split_angle)
        chip2_velocity = self.velocity.rotate(-split_angle)
        chip_radius = self.radius - ASTEROID_MIN_RADIUS

        chip1 = Asteroid(self.position.x, self.position.y, chip_radius)
        chip1.velocity = chip1_velocity * 1.2

        chip2 = Asteroid(self.position.x, self.position.y, chip_radius)
        chip2.velocity = chip2_velocity * 1.2