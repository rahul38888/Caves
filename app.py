import pygame

from scripts.noisegen import Noise

sq_width = 10

def init():
    size = (40, 80)
    noise = Noise(size, threshold=0.5)

    pygame.init()
    display = pygame.display.set_mode([size[0]*sq_width, size[1]*sq_width])
    pygame.display.set_caption("Noise")

    clock = pygame.time.Clock()

    return display, clock, noise


if __name__ == '__main__':
    display, clock, noise = init()

    fps_cap = 10

    running = True
    while running:
        clock.tick(fps_cap)
        display.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                noise.smoothing()

        for y in range(noise.height):
            for x in range(noise.width):
                color_val = noise.grid[y][x] * 255
                color = (color_val, color_val, color_val)
                rect = [x*sq_width, y*sq_width, sq_width, sq_width]
                pygame.draw.rect(display, color, rect)

        pygame.display.flip()

    pygame.quit()
