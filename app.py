from scripts.pathfinder import PathFinder
from datahandler.layout import Layout

if __name__ == '__main__':
    a = 100
    l = Layout((a, a))
    pf = PathFinder(layout=l)

    target = (a-2, a - 1)
    source = (0, 0)
    pf.update_target(target=target)

    print(pf.get_path(source=source))
