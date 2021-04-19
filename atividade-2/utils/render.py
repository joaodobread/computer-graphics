import sys

from OpenGL.GL import *
from OpenGL.GLUT import (glutInit, glutInitContextProfile, glutInitDisplayMode,
                         glutCreateWindow, glutDisplayFunc, glutKeyboardFunc, glutMainLoop,
                         GLUT_COMPATIBILITY_PROFILE, GLUT_SINGLE, GLUT_RGB)
from OpenGL.GLU import *
from utils import Colors


class Render:
    def __init__(self) -> None:
        glClearColor(*Colors.WHITE_RGB)

    def clear(self) -> None:
        glClear(GL_COLOR_BUFFER_BIT)

    def flush(self) -> None:
        glFlush()

    def specs(self) -> None:
        print(f"Device: {glGetString(GL_VENDOR).decode()}")
        print(f"Renderer: {glGetString(GL_RENDERER).decode()}")
        print(f"OpenGL: {glGetString(GL_VERSION).decode()}")

    def display(self, *event):
        raise Exception("Must be implemented by user")

    def keyboard(self, *event):
        raise Exception("Must be implemented by user")

    def init(self):
        glutInit(sys.argv)
        glutInitContextProfile(GLUT_COMPATIBILITY_PROFILE)
        glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
        glutCreateWindow('Main Window')
        glutDisplayFunc(self.display)
        glutKeyboardFunc(self.keyboard)

        glutMainLoop()
