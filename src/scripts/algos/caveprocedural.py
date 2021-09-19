import math
from random import random
import itertools

from datahandler.layout import Layout
from datahandler.room import Room
from scripts.algos.floodfill import flood_fill
from scripts.algos.line import getLinePixels, drawLine


class CaveProcedural:
    def __init__(self, layout: Layout):
        self.width: int = layout.width
        self.height: int = layout.height

        self.layout = layout

        self.room_size_threshold = 10
        self.connection_radius = 2

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

    def detectRooms(self):
        visited = [[False for x in range(self.width)] for y in range(self.height)]

        for x in range(self.width):
            for y in range(self.height):
                if not visited[y][x] and not self.layout.grid[y][x]:
                    tiles = flood_fill(self.layout.grid, x, y, visited=visited)
                    if len(tiles) < self.room_size_threshold:
                        for tile in tiles:
                            self.layout.grid[tile[1]][tile[0]] = 1
                        continue

                    room = Room(tiles=tiles)
                    room.calculate_borders(layout=self.layout)
                    self.layout.rooms.append(room)
                else:
                    visited[y][x] = True

        self.layout.rooms.sort(key=lambda r:r.size, reverse=True)

    def _create_gallary(self, a, b):
        dx = abs(a[0] - b[0])
        dy = abs(a[1] - b[1])
        

    def connect_rooms(self) -> list:
        connectors = []
        for room_A in self.layout.rooms:
            nearest_room, cordA, cordB = room_A.nearestRoom(self.layout.rooms)
            Room.connect(room_A, nearest_room)
            self._create_gallary(cordA, cordB)
            connectors.append([cordA, cordB])
            pixels = getLinePixels(cordA, cordB)
            drawLine(self.layout.grid, pixels, radius=self.connection_radius)

        return connectors

if __name__ == '__main__':
    size = int(input())
    noise = CaveProcedural(Layout((size, size)))

    noise.smoothing(iterations=10)
    for a in noise.layout.grid:
        print(list(map(lambda x: "#" if x else " ",a)))

    noise.detectRooms()
