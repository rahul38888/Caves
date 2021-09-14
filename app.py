import pygame

from datahandler.layout import Layout
from scripts.caveprocedural import CaveProcedural
from render.engine import RenderEngine
from scripts.pathfindingapp import PathFindingApp
from scripts.pathfinder import PathFinder

sq_width = 10
size = (80, 40)
itertions = 10
fps_cap = 10
layout = Layout(size)
pf = PathFinder()

state = dict()

def init():
    cave = CaveProcedural(layout=layout)
    cave.smoothing(iterations=itertions)

    pathfinderapp = PathFindingApp(layout=cave.layout, pathfinder=pf)
    pathfinderapp.new_target()
    pathfinderapp.add_follower()

    source = pathfinderapp.layout.sources.pop()
    state["path"] = pathfinderapp.get_path(source=source)
    pathfinderapp.layout.add_follower(source=source)

    def keymap():
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_t:
                pathfinderapp.new_target()
                state["path"] = pathfinderapp.get_path(pathfinderapp.layout.sources)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                pass

    def update():
        pass

    def render(display):

        for y in range(cave.height):
            for x in range(cave.width):
                color_val = (not pathfinderapp.layout.grid[y][x]) * 255

                color = (color_val, color_val, color_val)
                if pathfinderapp.layout.is_target((x,y)):
                    color = (0, 255, 0)
                elif pathfinderapp.layout.is_source((x,y)):
                    color = (255, 0, 0)
                elif state["path"] and state["path"].__contains__((x,y)):
                    color = (0, 0, 255)

                rect = [x*sq_width, y*sq_width, sq_width, sq_width]
                pygame.draw.rect(display, color, rect)

        pygame.display.flip()

    re = RenderEngine([size[0]*sq_width, size[1]*sq_width], update, render, keymap, fps_cap)

    return re, cave, pathfinderapp


if __name__ == '__main__':
    re, cave, pathfinder = init()

    re.start()

