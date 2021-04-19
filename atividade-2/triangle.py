from src.triangle import Triangle


def triangle():
    render = Triangle()
    render.init()
    render.specs()
    render.draw()


if __name__ == '__main__':
    triangle()
