from src.lines import Lines


def lines():
    lines = Lines()
    lines.init()
    lines.specs()
    lines.draw()


if __name__ == '__main__':
    lines()
