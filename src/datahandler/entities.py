import enum

import pygame


class Player:
    def __init__(self, initial_pos: tuple, initial_coordinate: tuple):
        self.position = initial_pos
        self.coordinate = initial_coordinate
        self.directions: list = [Direction.NONE, Direction.NONE, Direction.NONE, Direction.NONE]
        self.speed = 1

    def search_coordinate(self, coordinate: tuple):
        pass


class Enemy:
    def __init__(self, initial_pos: tuple, speed: int):
        self.position = initial_pos


class Direction(enum.Enum):
    NONE = (0, 0)

    UP = (0, -1)
    # UP_LEFT = (-1, -1)
    LEFT = (-1, 0)
    # DOWN_LEFT = (-1, 1)
    DOWN = (0, 1)
    # DOWN_RIGHT = (1, 1)
    RIGHT = (1, 0)
    # UP_RIGHT = (1, -1)


PLAYER_KEY_MAP = {
    pygame.K_UP: Direction.UP,
    pygame.K_RIGHT: Direction.RIGHT,
    pygame.K_DOWN: Direction.DOWN,
    pygame.K_LEFT: Direction.LEFT
}
