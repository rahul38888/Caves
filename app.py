import pygame

from datahandler.layout import Layout
from scripts.caveprocedural import CaveProcedural
from render.engine import RenderEngine
from scripts.pathfindingapp import PathFindingApp
from scripts.pathfinder import PathFinder

sq_width = 10
size = (80, 40)
itertions = 50
fps_cap = 10
layout = Layout(size)
pf = PathFinder()

state = dict()

def update_source(pathfinderapp: PathFindingApp):
    pathfinderapp.layout.sources.clear()
    pathfinderapp.add_follower()

    state["source"] = pathfinderapp.layout.sources.pop()
    pathfinderapp.layout.add_follower(source=state["source"])

    state["path"] = pathfinderapp.get_path(source=state["source"])

def init():
    cave = CaveProcedural(layout=layout)
    cave.smoothing(iterations=itertions)

    pathfinderapp = PathFindingApp(layout=cave.layout, pathfinder=pf)
    pathfinderapp.new_target()

    update_source(pathfinderapp)

    def keymap(event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_t:
            pathfinderapp.new_target()
            state["path"] = pathfinderapp.get_path(source=state["source"])

        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            update_source(pathfinderapp)

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

    return re


if __name__ == '__main__':
    re = init()

    re.start()

