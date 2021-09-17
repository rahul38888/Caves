import pygame

def draw():
    pygame.init()

    screen = pygame.display.set_mode((500,500))
    screen.fill([255,255,255])

    clock = pygame.time.Clock()

    while True:
        running = True

        while running:
            clock.tick(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            pygame.draw.polygon(screen, [255, 0, 0], [(0, 0), (250, 500), (250, 250)], width=0)

            pygame.display.flip()

if __name__ == '__main__':
    draw()
