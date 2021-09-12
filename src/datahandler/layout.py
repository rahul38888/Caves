import itertools


class Layout:
    def __init__(self, dimensions: tuple):
        # 0: empty, -1: obstacle, 1: target, 2: start
        self.width: int = dimensions[0]
        self.height: int = dimensions[1]
        self.grid = [[0 for i in range(dimensions[0])] for j in range(dimensions[1])]

    def getNeighbours(self, x, y) -> list:
        nei = list()
        for i, j in itertools.product(range(-1, 2), range(-1, 2)):
            if 0 <= x + i < self.width and 0 <= y + j < self.height and not i == j == 0:
                nei.append((x + i, y + j))

        return nei