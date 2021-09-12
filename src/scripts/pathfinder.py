from math import inf
from queue import Queue

from datahandler.layout import Layout


class PathFinder:
    def __init__(self, layout: Layout):
        self.layout = layout

        self.target = None
        self.dist = None
        self.prev = None

        self.normal_weight: float = 1.0
        self.diagonal_weight: float = 1.414

    def _recursive_step(self, x_cord, y_cord, prev: list, dist: list):
        visited = set()

        queue = Queue()
        queue.put((x_cord, y_cord))
        queued = set()

        while not queue.empty():
            x, y = queue.get()

            if visited.__contains__((x, y)):
                continue

            visited.add((x, y))

            for n in self.layout.getNeighbours(x, y):
                n_dist = self.normal_weight if (sum(n) - x - y) in [-1, 1] else self.diagonal_weight
                if dist[n[1]][n[0]] > dist[y][x] + n_dist:
                    dist[n[1]][n[0]] = dist[y][x] + n_dist
                    prev[n[1]][n[0]] = (x, y)
                if not queued.__contains__(n):
                    queue.put(n)
                    queued.add(n)

    def _update_shortest_matrix(self):
        x, y = self.target
        prev = [[None for i in range(self.layout.width)] for j in range(self.layout.height)]
        dist = [[inf for i in range(self.layout.width)] for j in range(self.layout.height)]

        prev[y][x] = (x, y)
        dist[y][x] = 0
        self._recursive_step(x, y, prev, dist)
        self.dist = dist
        self.prev = prev

    def update_target(self, target: tuple):
        self.target = target
        self._update_shortest_matrix()

    def get_path(self, source: tuple) -> list:
        path = []
        cur = source
        while True:
            path.append(cur)
            if cur == self.target:
                break
            cur = self.prev[cur[1]][cur[0]]

        return path
