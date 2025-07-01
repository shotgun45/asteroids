import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2 )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        split_angle = random.uniform(20,50)
        chip1_velocity = self.velocity.rotate(split_angle)
        chip2_velocity = self.velocity.rotate(-split_angle)
        chip_radius = self.radius - ASTEROID_MIN_RADIUS
        
        chip1 = Asteroid(self.position.x, self.position.y, chip_radius)
        chip1.velocity = chip1_velocity * 1.2
        chip2 = Asteroid(self.position.x, self.position.y, chip_radius)
        chip2.velocity = chip2_velocity * 1.2