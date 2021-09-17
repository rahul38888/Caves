import pygame
import random

from datahandler.screencomponents import coordinate_map


def coordinate_data(grid: list, sq_width: float) -> list:
    grid_w = len(grid[0])
    grid_h = len(grid)
    triangles = []
    for y in range(grid_h + 1):
        for x in range(grid_w + 1):
            activation = (1, 1, 1, 1)
            if 0 < y < grid_h and 0 < x < grid_w:
                activation = (grid[y - 1][x - 1], grid[y - 1][x], grid[y][x], grid[y][x - 1])

            triangles += _get_triangles((x, y), activation, sq_width=sq_width)

    return triangles


def _get_triangles(index: tuple, cord_activations: tuple, sq_width: float) -> list:
    triangles = []
    for tri in coordinate_map.get(cord_activations):
        triangles.append(tuple(map(lambda c: (sq_width * index[0] + c[0] * sq_width,
                                              sq_width * index[1] + c[1] * sq_width), tri)))

    return triangles


if __name__ == '__main__':
    pygame.init()
    pygame.font.init()
    screen_size = 600
    display = pygame.display.set_mode((screen_size, screen_size))
    pygame.display.set_caption("Caves")

    clock = pygame.time.Clock()

    grid_size = 50
    sq_w = screen_size / grid_size
    grid = [[random.randint(0, 1) for i in range(grid_size)] for j in range(grid_size)]
    # triangles = coordinate_data(grid, sq_width=sq_w)
    triangles = _get_triangles((1, 1), (0, 0, 0, 0), sq_width=screen_size/3)

    activations = list(coordinate_map.keys())
    index = 0

    running = True
    while running:
        clock.tick(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                index = (index + 1) % len(activations)
                # triangles = coordinate_data(grid, sq_width=sq_w)
                triangles = _get_triangles((1, 1), activations[index], sq_width=screen_size/3)

            display.fill((255, 255, 255))
            rect = [screen_size/3, screen_size/3, int(screen_size/3), int(screen_size/3)]
            pygame.draw.rect(display, [0, 255, 0], rect, width=2)

            myfont = pygame.font.SysFont('Comic Sans MS', 30)
            textsurface = myfont.render(str(activations[index]), False, (0, 0, 0))
            display.blit(textsurface,(0,0))
            for tri in triangles:
                pygame.draw.polygon(display, [255, 0, 0], list(tri), width=2)

        pygame.display.update()

    pygame.quit()
