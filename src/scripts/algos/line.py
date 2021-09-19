import math


def getLinePixels(a: tuple, b: tuple) -> list:
    inverted = False
    dx = b[0] - a[0]
    dy = b[1] - a[1]
    step = int(math.copysign(1, dx))
    gradStep = int(math.copysign(1, dy))

    smaller = abs(dy)
    larger = abs(dx)

    if larger < smaller:
        inverted = True
        larger, smaller = smaller, larger
        step, gradStep = gradStep, step

    gradAccumulator = larger / 2
    pixels = []
    x, y = a
    for i in range(larger + 1):
        pixels.append((x, y))

        if inverted:
            y += step
        else:
            x += step

        gradAccumulator += smaller
        if gradAccumulator >= larger:
            if inverted:
                x += gradStep
            else:
                y += gradStep
            gradAccumulator -= larger

    return pixels


def drawLine(grid: list, line_pixels: list, radius: int):
    for pixel in line_pixels:
        for y in range(pixel[1] - math.ceil(radius), pixel[1] + math.ceil(radius) + 1):
            for x in range(pixel[0] - math.ceil(radius), pixel[0] + math.ceil(radius) + 1):
                if 0 <= x < len(grid[0]) and 0 <= y < len(grid):
                    if math.pow(pixel[0] - x, 2) + math.pow(pixel[1] - y, 2) < math.pow(radius, 2):
                        grid[y][x] = 0


if __name__ == '__main__':
    n = 10
    grid = [[1 for i in range(10)] for i in range(10)]
    import random

    a = (random.randint(0, n - 1), random.randint(0, n - 1))
    b = (random.randint(0, n - 1), random.randint(0, n - 1))
    pixels = getLinePixels(a, b)
    drawLine(grid, pixels, radius=2)
    print(a, b)

    for line in grid:
        string = ""
        for i in line:
            if not i:
                string += "#"
            else:
                string += '..'
        print(string)
