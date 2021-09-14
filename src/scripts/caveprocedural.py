from random import random
import itertools

from datahandler.layout import Layout

class CaveProcedural:
    def __init__(self, layout: Layout):
        self.width: int = layout.width
        self.height: int = layout.height

        self.layout = layout

        # 1: wall, 0: open
        for x in range(self.width):
            for y in range(self.height):
                val = 0 if random() < 0.5 else 1 if (0< x <self.width-1 and 0<y<self.height-1) else 1
                self.layout.grid[y][x] = val

    def _neighouring_walls(self, x, y) -> float:
        n_count = 0
        w_count = 0
        neighbor_depth = 1
        for i, j in itertools.product(range(-neighbor_depth, neighbor_depth + 1), range(-neighbor_depth, neighbor_depth + 1)):
            if 0 <= x + i < self.width and 0 <= y + j < self.height:
                if not i == j == 0:
                    w_count += self.layout.grid[y + j][x + i]
                    n_count+=1
            else:
                w_count+=1

        return 1 if w_count > n_count/2  else 0 if w_count < n_count/2 else self.layout.grid[y][x]

    def _single_smoothing(self):
        new_grid = [[0 for x in range(self.width)] for y in range(self.height)]
        for y in range(self.height):
            for x in range(self.width):
                new_grid[y][x] = self._neighouring_walls(x, y)

        self.layout.grid = new_grid

    def smoothing(self, iterations: int = 1):
        for i in range(iterations):
            self._single_smoothing()


if __name__ == '__main__':
    buckets = 3
    noise = CaveProcedural((10, 10))

    for i in range(21):
        print(noise._roundoff(i/10))
