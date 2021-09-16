from datahandler.layout import Layout

import itertools


class Room:
    def __init__(self, tiles: set):
        self.tiles = tiles
        self.size = len(tiles)
        self.border = set()

    def calculate_borders(self, layout: Layout):
        for tile in self.tiles:
            x, y = tile
            for i, j in itertools.product(range(-1, 2), range(-1, 2)):
                if (i == 0 or j == 0) and not layout[y+j][x + i]:
                    self.border.add((x + i, y + j))
