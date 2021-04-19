from random import randrange

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy

from utils import Render


class Grid(Render):
    def __init__(self) -> None:
        super().__init__()
        self.divider_x = 1
        self.divider_y = 1
        

    def draw(self):
        self.clear()
        glBegin(GL_LINES)
        glColor3f(255, 255, 255)

        values_x = []
        for i in numpy.arange(-1, 1.1, 1 / self.divider_x).tolist():
            values_x.append(i)

        values_y = []
        for i in numpy.arange(-1, 1.1, 1 / self.divider_y).tolist():
            values_y.append(i)


        for value in values_x:
            glVertex2f(-1, value)
            glVertex2f(1, value)


        for value in values_y:
            glVertex2f(value, -1)
            glVertex2f(value, 1)

        glColor3f(255, 0, 0)
        glVertex2f(1, 0)
        glVertex2f(-1, 0)

        glColor3f(0, 255, 0)
        glVertex2f(0, 1)
        glVertex2f(0, -1)

        glEnd()
        self.flush()

    def display(self, *event):
        self.draw()

    def keyboard(self, *event):
        key, *_ = event
        if key == b'x':
            self.divider_x = self.divider_x + 1
        if key == b'X':
            self.divider_x = self.divider_x - 1

        if key == b'y':
            self.divider_y = self.divider_y + 1
        if key == b'Y':
            self.divider_y = self.divider_y - 1

        glutPostRedisplay()
