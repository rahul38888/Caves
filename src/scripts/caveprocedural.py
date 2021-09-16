from random import random
import itertools

from datahandler.layout import Layout
from algos.floodfill import flood_fill
from datahandler.room import Room


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

    def calculateRooms(self):
        visited = [[False for x in range(self.width)] for y in range(self.height)]

        for x in range(self.width):
            for y in range(self.height):
                if not visited[y][x] and not self.layout[y][x]:
                    tiles = flood_fill(self.layout.grid, x, y, visited=visited)
                    room = Room(tiles=tiles)
                    room.calculate_borders(layout=self.layout)
                    self.layout.rooms.append(room)

        self.layout.rooms.sort(key=lambda r:r.size, reverse=True)


if __name__ == '__main__':
    size = int(input())
    noise = CaveProcedural(Layout((size, size)))

    while True:
        noise.smoothing()
        for l in noise.layout.grid:
            lc = ["#" if i else " " for i in l]
            print(lc)

        input()
