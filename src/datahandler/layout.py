import itertools
import random


# Definition type to keep information of layout
#   tiles
#   Rooms

class Layout:
    def __init__(self, dimensions: tuple, grid: list = None):
        self.width: int = dimensions[0]
        self.height: int = dimensions[1]

        self.rooms = list()

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

    def _random_position(self, ignore: list):
        x, y = 0, 0
        found = False
        while not found:
            x, y = random.randint(0,self.width-1), random.randint(0,self.height-1)
            if (x,y) in ignore or self.grid[y][x]:
                continue

            found = True

        return x,y

    def move_target(self, position: tuple = None, igrore: list = []) -> bool:
        if position:
            if 0 <= position[0] < self.width and 0 <= position[1] < self.height:
                if not self.grid[position[1]][position[0]] and position not in igrore:
                    return position
        else:
            return self._random_position(ignore=igrore)

        return None

    def new_source(self, ignore: list = []):
        return self._random_position(ignore=ignore)

