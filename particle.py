import pygame
import random

class Particle:
    def __init__(self, position, color):
        self.position = pygame.Vector2(position)
        angle = random.uniform(0, 2 * 3.14159)
        speed = random.uniform(60, 180)
        self.velocity = pygame.Vector2(speed, 0).rotate_rad(angle)
        self.lifetime = random.uniform(0.3, 0.7)
        self.color = color
        self.radius = random.randint(2, 4)

    def update(self, dt):
        self.position += self.velocity * dt
        self.lifetime -= dt

    def draw(self, screen):
        if self.lifetime > 0:
            pygame.draw.circle(screen, self.color, self.position, self.radius)