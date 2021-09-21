import random

import pygame

from datahandler.layout import Layout
from render.renderdatagenerator import render_data
from scripts.pathfindingapp import PathFindingApp
from scripts.algos.pathfinder import PathFinder
from scripts.algos.caveprocedural import CaveProcedural
from render.engine import RenderEngine


# Actual application to initialize pygame, RenderEngine, do canvas generation and pathfinding
class App:
    def __init__(self, size=(80,40), sq_width=15, iterations=5):
        self.sq_width = sq_width
        self.size = size
        self.screen_size = (self.size[0]*self.sq_width, self.size[1]*self.sq_width)
        self.iterations = iterations
        self.fps_cap = 5

        self.wall_color = [95, 67, 42]
        self.wall_border_color = [71, 54, 39]
        self.room_color = [211, 255, 204]

        self.font_type = 'Comic Sans MS'
        self.font_size = 30
        self.font_color = (255, 255, 255)

        self.cave = CaveProcedural(layout=Layout(self.size))
        self.cave.smoothing(iterations=self.iterations)
        self.cave.detectRooms()
        self.cave.connectRooms()

        self.pathfinderapp = PathFindingApp(layout=self.cave.layout, pathfinder=PathFinder())

        self.player = self.pathfinderapp.move_target()
        self.no_of_enemies = 5
        self.enemies = []
        for i in range(self.no_of_enemies):
            enemy = self.pathfinderapp.new_follower(ignore=[self.player]+self.enemies)
            if enemy:
                self.enemies.append(enemy)

        self.renderEngine = self.init()

    def keymapHandler(self):
        def keymap(event):
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.player = self.pathfinderapp.move_target()

            player_moved = False
            new_position = self.player
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                new_position = (new_position[0], new_position[1]-1)
                player_moved = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                new_position = (new_position[0]+1, new_position[1])
                player_moved = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                new_position = (new_position[0], new_position[1]+1)
                player_moved = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                new_position = (new_position[0]-1, new_position[1])
                player_moved = True

            if player_moved:
                pos = self.pathfinderapp.move_target(position=new_position)
                if pos:
                    self.player = pos

        return keymap

    def updateHandler(self):
        def update():
            for i in range(len(self.enemies)):
                next_step = self.pathfinderapp.get_next_step(self.enemies[i])
                if next_step is not self.player:
                    self.enemies[i] = next_step

        return update

    def _rendertext(self, display, text: str, position: tuple):
        font = pygame.font.SysFont(self.font_type, self.font_size)
        textsurface = font.render(text, False, self.font_color)
        display.blit(textsurface,position)

    def renderHandler(self):
        def render(display):
            triangles, tags = render_data(self.cave.layout.grid, self.sq_width)
            # display.fill(self.room_color)
            pygame.draw.rect(display, self.room_color, rect=[0,0,self.screen_size[0], self.screen_size[1]])
            pygame.draw.rect(display, tuple(map(lambda x: (x-20)%255,self.wall_color)),
                             [0, (self.size[1])*self.sq_width,self.screen_size[0], 200])

            if self.player:
                color = (0, 255, 0)
                x, y = self.player
                pygame.draw.circle(display, color, ((x+0.5) * self.sq_width, (y+0.5) * self.sq_width), self.sq_width/2, width=0)
            if self.enemies:
                color = (255, 0, 0)
                for enemy in self.enemies:
                    x, y = enemy
                    pygame.draw.circle(display, color, ((x+0.5) * self.sq_width, (y+0.5) * self.sq_width), self.sq_width/2, width=0)

            for i in range(len(triangles)):
                tri = triangles[i]
                tag = tags[i]
                pygame.draw.polygon(display, self.wall_color, list(tri), width=0)

            text = "World size: " + str(self.size)
            self._rendertext(display, text, (20,(self.size[1]+2)*self.sq_width))

            pygame.display.flip()

        return render

    def init(self):
        return RenderEngine(list((1200, 600)), self.updateHandler(),
                                         self.renderHandler(), self.keymapHandler(), self.fps_cap)

    def start(self):
        self.renderEngine.start()
