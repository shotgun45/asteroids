import pytest
import pygame
from asteroid import Asteroid
from constants import ASTEROID_MIN_RADIUS

import sys
print(sys.path)

def test_asteroid_creation():
    asteroid = Asteroid(100, 100, 30)
    assert asteroid.position.x == 100
    assert asteroid.position.y == 100
    assert asteroid.radius == 30

def test_asteroid_color_large():
    asteroid = Asteroid(0, 0, ASTEROID_MIN_RADIUS * 3)
    assert asteroid.color == (0, 255, 0)

def test_asteroid_color_medium():
    asteroid = Asteroid(0, 0, ASTEROID_MIN_RADIUS * 1.5)
    assert asteroid.color == (255, 255, 0)

def test_asteroid_color_small():
    asteroid = Asteroid(0, 0, ASTEROID_MIN_RADIUS)
    assert asteroid.color == (255, 0, 0)