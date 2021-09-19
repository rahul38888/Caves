import math

from datahandler.layout import Layout

import itertools


class Room:
    def __init__(self, tiles: set):
        self.tiles = tiles
        self.size = len(tiles)
        self.border = set()
        self.connected_rooms = []

    def calculate_borders(self, layout: Layout):
        for tile in self.tiles:
            x, y = tile
            for i, j in itertools.product(range(-1, 2), range(-1, 2)):
                if (i == 0 or j == 0) and not layout.grid[y+j][x + i]:
                    self.border.add((x + i, y + j))

    @staticmethod
    def connect(roomA, roomB):
        roomA.connected_rooms.append(roomB)
        roomB.connected_rooms.append(roomA)

    def nearestRoom(self, rooms: list):
        nearest_room = None
        min_dist = math.inf
        cordA, cordB = None, None
        for room in rooms:
            if self == room:
                continue
            temp_min_dist = math.inf
            temp_cordA, temp_cordB = None, None
            for cord_A in self.border:
                for cord_B in room.border:
                    distance = math.pow(cord_A[0] - cord_B[0], 2) + math.pow(cord_A[1] - cord_B[1], 2)
                    if temp_min_dist > distance:
                        temp_min_dist = distance
                        temp_cordA = cord_A
                        temp_cordB = cord_B

            if min_dist > temp_min_dist:
                nearest_room = room
                cordA = temp_cordA
                cordB = temp_cordB
                min_dist = temp_min_dist

        return nearest_room, cordA, cordB

    def __eq__(self, other):
        return self.tiles == other.tiles
