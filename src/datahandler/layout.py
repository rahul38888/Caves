import itertools
import random

from scripts.pathfinder import PathFinder


class Layout:
    def __init__(self, dimensions: tuple, grid: list = None):
        # 0: empty, -1: obstacle, 1: target, 2: start
        self.width: int = dimensions[0]
        self.height: int = dimensions[1]

        self.target = None
        self.source = None
        self.pathfider = PathFinder(self)

        self.followers = []

        if grid:
            self.grid = grid
        else:
            self.grid = [[0 for i in range(dimensions[0])] for j in range(dimensions[1])]

    def getNeighbours(self, x, y) -> list:
        nei = list()
        for i, j in itertools.product(range(-1, 2), range(-1, 2)):
            if 0 <= x + i < self.width and 0 <= y + j < self.height and not i == j == 0:
                nei.append((x + i, y + j))

        return nei

    def _random_position(self):
        x, y = 0, 0
        while self.grid[y][x]:
            x, y = random.randint(0,self.width-1), random.randint(0,self.height-1)
            if (x,y) == self.target or (x,y) in self.source:
                x,y =0,0

        return x,y

    def update_target(self):
        self.target = self._random_position()
        self.pathfider.update_target(self.target)

    def add_follower(self):
        self.followers.append(self._random_position())