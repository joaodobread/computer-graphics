from src.grid import Grid


def grid():
    grid = Grid()
    grid.init()
    grid.specs()
    grid.draw()


if __name__ == '__main__':
    grid()
