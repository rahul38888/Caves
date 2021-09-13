from ursina import *            # import everything we need with one line.

app = Ursina()
ground = Entity(
    model = 'plane',
    color = color.magenta,
    z = 0,
    y = -1,
    origin = (0, 0),
    scale = (5, 4, 10),
    collider = 'box'
)


if __name__ == '__main__':
    app.run()