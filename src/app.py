import random

import pygame

from datahandler.layout import Layout
from render.renderdatagenerator import coordinate_data
from scripts.pathfindingapp import PathFindingApp
from scripts.algos.pathfinder import PathFinder
from scripts.algos.caveprocedural import CaveProcedural
from render.engine import RenderEngine


class App:
    def __init__(self, size=(80,40), sq_width=15, iterations=5):
        self.sq_width = sq_width
        self.size = size
        self.screen_size = (self.size[0]*self.sq_width, self.size[1]*self.sq_width)
        self.iterations = iterations
        self.fps_cap = 10

        self.state = dict()

        self.cave = CaveProcedural(layout=Layout(self.size))
        self.cave.smoothing(iterations=self.iterations)
        self.cave.detectRooms()

        self.cave.connectRooms()

        self.pathfinderapp = PathFindingApp(layout=self.cave.layout, pathfinder=PathFinder())
        self.pathfinderapp.new_target()

        self.renderEngine = self.init()

    def update_source(self):
        self.pathfinderapp.layout.sources.clear()
        self.pathfinderapp.add_follower()

        self.state["source"] = self.pathfinderapp.layout.sources.pop()
        self.pathfinderapp.layout.add_source(source=self.state["source"])

        self.state["path"] = self.pathfinderapp.get_path(source=self.state["source"])

    def keymapHandler(self):
        def keymap(event):
            if event.type == pygame.KEYDOWN and event.key == pygame.K_t:
                self.pathfinderapp.new_target()
                self.state["path"] = self.pathfinderapp.get_path(source=self.state["source"])

            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                self.update_source()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.cave = CaveProcedural(layout=Layout(self.size))
                self.cave.smoothing(iterations=self.iterations)
                self.cave.detectRooms()

                self.cave.connectRooms()
                self.renderEngine = self.init()

        return keymap

    def updateHandler(self):
        def update():
            pass

        return update

    def renderHandler(self):
        def render(display):
            triangles = coordinate_data(self.cave.layout.grid, self.sq_width)
            display.fill((255, 255, 255))

            if len(self.state["path"]):
                color = (0, 0, 255)
                points = list(map(lambda c: ((c[0] + 0.5) * self.sq_width, (c[1] + 0.5) * self.sq_width),self.state["path"]))
                pygame.draw.lines(display, color, False, points, width=2)
            if self.pathfinderapp.layout.target:
                color = (0, 255, 0)
                x, y = self.pathfinderapp.layout.target
                pygame.draw.circle(display, color, ((x+0.5) * self.sq_width, (y+0.5) * self.sq_width), self.sq_width/2, width=0)
            if self.state["source"]:
                color = (255, 0, 0)
                x, y = self.state["source"]
                pygame.draw.circle(display, color, ((x+0.5) * self.sq_width, (y+0.5) * self.sq_width), self.sq_width/2, width=0)

            # for room in self.cave.layout.rooms:
            #     for tile in room.tiles:
            #         x, y = tile
            #         rect = [x*self.sq_width, y*self.sq_width, self.sq_width, self.sq_width]
            #         pygame.draw.rect(display, room.color, rect=rect)

            for tri in triangles:
                pygame.draw.polygon(display, [0, 0, 0], list(tri), width=0)
                # pygame.draw.lines(display, [0, 0, 0], True, list(tri), blend=1)

            # for connector in self.connectors:
            #     connector = [((c[0]+0.5) * self.sq_width, (c[1]+0.5) * self.sq_width) for c in connector]
            #     pygame.draw.lines(display, (255, 0, 0), False, connector)

            pygame.display.flip()

        return render

    def init(self):
        self.update_source()

        self.renderEngine = RenderEngine(list((1200, 600)), self.updateHandler(),
                                         self.renderHandler(), self.keymapHandler(), self.fps_cap)

        return self.renderEngine

    def start(self):
        self.renderEngine.start()
