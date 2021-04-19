from random import randrange

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from utils import Render


class Lines(Render):
    def __init__(self) -> None:
        super().__init__()

    def draw(self):
        self.clear()
        glBegin(GL_LINES)

        for i in range(1, 101):
            r = randrange(0, 254)
            g = randrange(0, 254)
            b = randrange(0, 254)
            glColor3f(r, g, b)
            if i % 2:
                glVertex2f(-1, i/100)
                glVertex2f(1, i/100)
            else:
                glVertex2f(-1, -i/100)
                glVertex2f(1, -i/100)

        glEnd()
        self.flush()

    def display(self, *event):
        self.draw()

    def keyboard(self, *event):
        print(event)
