import pygame

from datahandler.layout import Layout
from scripts.pathfindingapp import PathFindingApp
from scripts.algos.pathfinder import PathFinder
from scripts.algos.caveprocedural import CaveProcedural
from render.engine import RenderEngine


class App:
    def __init__(self):
        self.sq_width = 10
        self.size = (80, 40)
        self.itertions = 50
        self.fps_cap = 10

        self.state = dict()

        self.cave = CaveProcedural(layout=Layout(self.size))
        self.cave.smoothing(iterations=self.itertions)
        self.cave.detectRooms()

        self.pathfinderapp = PathFindingApp(layout=self.cave.layout, pathfinder=PathFinder())
        self.pathfinderapp.new_target()

        self.renderEngine = self.init()

    def update_source(self):
        self.pathfinderapp.layout.sources.clear()
        self.pathfinderapp.add_follower()

        self.state["source"] = self.pathfinderapp.layout.sources.pop()
        self.pathfinderapp.layout.add_follower(source=self.state["source"])

        self.state["path"] = self.pathfinderapp.get_path(source=self.state["source"])

    def keymapHandler(self):
        def keymap(event):
            if event.type == pygame.KEYDOWN and event.key == pygame.K_t:
                self.pathfinderapp.new_target()
                self.state["path"] = self.pathfinderapp.get_path(source=self.state["source"])

            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                self.update_source()

        return keymap

    def updateHandler(self):
        def update():
            pass

        return update

    def renderHandler(self):
        def render(display):
            for y in range(self.cave.height):
                for x in range(self.cave.width):
                    color_val = (not self.pathfinderapp.layout.grid[y][x]) * 255

                    color = (color_val, color_val, color_val)
                    if self.pathfinderapp.layout.is_target((x, y)):
                        color = (0, 255, 0)
                    elif self.pathfinderapp.layout.is_source((x, y)):
                        color = (255, 0, 0)
                    elif self.state["path"] and self.state["path"].__contains__((x, y)):
                        color = (0, 0, 255)

                    rect = [x * self.sq_width, y * self.sq_width, self.sq_width, self.sq_width]
                    pygame.draw.rect(display, color, rect)

            pygame.display.flip()

        return render

    def init(self):
        self.update_source()

        self.renderEngine = RenderEngine([self.size[0] * self.sq_width, self.size[1] * self.sq_width],
                                         self.updateHandler(), self.renderHandler(), self.keymapHandler(), self.fps_cap)

        return self.renderEngine

    def start(self):
        self.renderEngine.start()
