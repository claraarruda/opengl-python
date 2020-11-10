from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *
import sys

pi = 3.14

def drawCircle():
    glBegin(GL_POLYGON)
    for i in range(300):
        angle = 2 * pi * i / 300
        x = cos(angle)
        y = sin(angle)
        glVertex2f(x, y)
    glEnd()

def keyPressedCircle(bkey, x, y):
    # Convert bytes object to string
    key = bkey.decode("utf-8")
    if key == 'c' or key == 'C':
        print('redimensiona o circulo')
        for i in range(350):
            glPushMatrix()
            glScalef(0.5, 0.5, 0.5)
            glClearColor(0.0, 0.0, 0.0, 1.0)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            displayCircle()
            glPopMatrix()

            glPushMatrix()
            glScalef(0.7, 0.7, 0.7)
            glClearColor(0.0, 0.0, 0.0, 1.0)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            displayCircle()
            glPopMatrix()

def displayCircle():
    drawCircle()
    glFlush()

def mainCircle():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Circulo")
    glClearColor(1.0, 1.0, 0.0, 1.0)
    glutDisplayFunc(displayCircle)
    glutKeyboardFunc(keyPressedCircle)
    glutMainLoop()
