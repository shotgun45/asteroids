import pytest
import pygame
from player import Player
from constants import PLAYER_RADIUS

def test_player_creation():
    player = Player(50, 60)
    assert player.position.x == 50
    assert player.position.y == 60
    assert player.radius == PLAYER_RADIUS