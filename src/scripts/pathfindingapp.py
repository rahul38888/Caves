

from datahandler.layout import Layout
from scripts.algos.pathfinder import PathFinder


# Pathfinder application uril to handle layout and pathfinder util
class PathFindingApp:
    def __init__(self, layout: Layout, pathfinder: PathFinder):
        self.layout = layout
        self.pathfinder = pathfinder

    def recalculate(self):
        if self.layout.target is None:
            return
        self.pathfinder.recalculate(self.layout.target[0], self.layout.target[1], self.layout)

    def new_target(self, target: tuple = None):
        self.layout.new_target(target=target)
        self.recalculate()

    def add_follower(self, source: tuple = None):
        self.layout.add_source(source)

    def get_path(self, source: tuple) -> list:
        path = []
        cur = source
        while True:
            path.append(cur)
            if cur == self.layout.target:
                break
            if not cur:
                return []

            cur = self.pathfinder.prev[cur[1]][cur[0]]

        return path


if __name__ == '__main__':
    a = 10
    l = Layout((a, a))
    pf = PathFinder()

    p_app = PathFindingApp(layout=l, pathfinder=pf)

    target = (a-2, a - 1)
    source = (0, 0)
    p_app.new_target(target=target)

    print(p_app.get_path(source=source))