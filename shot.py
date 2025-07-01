import pygame
from asteroid import Asteroid
from constants import SHOT_RADIUS

class Shot(Asteroid):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)