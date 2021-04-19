from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from utils import Render


class Triangle(Render):
    def __init__(self) -> None:
        super().__init__()

    def draw(self):
        self.clear()
        glBegin(GL_TRIANGLES)
        glColor3f(1.0, 0.0, 0.0)
        glVertex2f(-0.5, -0.5)

        glColor3f(0.0, 1.0, 0.0)
        glVertex2f(0.5, -0.5)

        glColor3f(1.0, 0.0, 0.0)
        glVertex2f(0.0, 0.5)
        glEnd()
        self.flush()

    def display(self, *event):
        self.draw()

    def keyboard(self, *event):
        print(event)
