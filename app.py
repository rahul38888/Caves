import pygame

from datahandler.layout import Layout
from scripts.caveprocedural import CaveProcedural
from render.engine import RenderEngine

sq_width = 10
size = (80, 40)
itertions = 10
fps_cap = 10
layout = Layout(size)


def init():
    noise = CaveProcedural(layout=layout)
    noise.smoothing(iterations=itertions)

    def keymap():
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                noise = CaveProcedural(layout)
                noise.smoothing(iterations=itertions)

    def update():
        pass

    def render():
        for y in range(noise.height):
            for x in range(noise.width):
                color_val = (not noise.layout.grid[y][x]) * 255
                color = (color_val, color_val, color_val)
                rect = [x*sq_width, y*sq_width, sq_width, sq_width]
                pygame.draw.rect(display, color, rect)

    re = RenderEngine([size[0]*sq_width, size[1]*sq_width], update, render, keymap, fps_cap)

    return re, noise


if __name__ == '__main__':
    re, noise = init()

    re.start()

