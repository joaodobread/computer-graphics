from random import randrange

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from utils import Render


class Polygon(Render):
    def __init__(self) -> None:
        super().__init__()

    def draw(self):
        self.clear()
        glBegin(GL_POLYGON)
        glVertex3f(-0.5, 0.42, 0.0)
        glVertex3f(-1.0, 0.0, 0.0)
        glVertex3f(-0.5, 1.0, 0.0)
        glVertex3f(0.5, 1.0, 0.0)
        glVertex3f(1.0, 0.0, 0.0)
        glVertex3f(0.5, 1.0, 0.0)
        glVertex3f(0.3, -0.3, 0.0)
        glEnd()
        self.flush()

    def display(self, *event):
        self.draw()

    def keyboard(self, *event):
        print(event)
