import pygame
from perlin_noise import PerlinNoise

def draw():
    pygame.init()

    noise = PerlinNoise()

    size = 500

    image = [[noise([i/size,j/size]) for i in range(size)] for j in range(size)]
    print(image)

    screen = pygame.display.set_mode((size,size))
    # screen.fill([255,255,255])

    clock = pygame.time.Clock()
    while running:
        running = True

        while running:
            clock.tick(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            for j in range(size):
                for i in range(size):
                    rect = [i,j,1,1]
                    pygame.draw.rect(screen,[255*image[j][i],255*image[j][i]],rect)

            pygame.display.flip()

        pygame.quit()


if __name__ == '__main__':
    draw()
