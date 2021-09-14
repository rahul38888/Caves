import pygame


class RenderEngine:
    def __init__(self, dimensions: list, update, render, keymap, frame_rate: int = 10):

        self.dimensions = dimensions

        pygame.init()
        self.display = pygame.display.set_mode(dimensions)
        pygame.display.set_caption("Caves")

        self.keymap = keymap
        self.render = render
        self.update = update
        self.frame_rate = frame_rate

        self.clock = pygame.time.Clock()

    def start(self):
        running = True

        while running:
            self.clock.tick(self.frame_rate)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            if self.keymap:
                self.keymap()
            if self.update:
                self.update()
            if self.render:
                self.render(self.display)

        pygame.quit()
