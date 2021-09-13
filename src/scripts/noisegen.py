from random import random
import itertools


class Noise:
    def __init__(self, dimensions: tuple, threshold: float = 0.5):
        self.width: int = dimensions[0]
        self.height: int = dimensions[1]

        self.threshold = threshold

        self.grid = [[0 if random() < self.threshold else 1 if (0< x <self.width-1 and 0<y<self.height-1) else 0
                      for x in range(self.width)] for y in range(self.height)]

    def _neighbours_mean_value(self, x, y) -> float:
        sum = 0
        count = 0
        for i, j in itertools.product(range(-1, 2), range(-1, 2)):
            if 0 <= x + i < self.width and 0 <= y + j < self.height and not i == j == 0:
                sum += self.grid[y+j][x+i]
                count += 1

        return 0 if sum/count < self.threshold else 1

    def _single_smoothing(self):
        new_grid = [[0 for x in range(self.width)] for y in range(self.height)]
        for y in range(self.height):
            for x in range(self.width):
                new_grid[y][x] = self._neighbours_mean_value(x, y)

        self.grid = new_grid

    def smoothing(self, iterations: int = 1):
        for i in range(iterations):
            self._single_smoothing()


if __name__ == '__main__':
    buckets = 3
    noise = Noise((10, 10))

    for i in range(21):
        print(noise._roundoff(i/10))
