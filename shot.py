import pygame
from asteroid import Asteroid
from constants import SHOT_RADIUS

class Shot(Asteroid):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.color = (255, 255, 255)  # White

    # Shots should not wrap around the screen, they should disappear when they go off-screen
    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius)