import itertools
import random


class Layout:
    def __init__(self, dimensions: tuple, grid: list = None):
        # 0: empty, -1: obstacle, 1: target, 2: start
        self.width: int = dimensions[0]
        self.height: int = dimensions[1]

        self.rooms = list()

        self.target = None
        self.sources = set()

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
            if (x,y) == self.target or (x,y) in self.sources:
                x,y =0,0

        return x,y

    def is_target(self, cell: tuple):
        return cell == self.target

    def is_source(self, cell: tuple):
        return self.sources.__contains__(cell)

    def new_target(self, target: tuple = None):
        self.target = target if target else self._random_position()

    def add_source(self, source: tuple = None):
        self.sources.add(source if source else self._random_position())