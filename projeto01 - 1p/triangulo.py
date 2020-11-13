from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time

def init():
    glClearColor(0, 0, 0, 1)
    glClearDepth(1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

rotacao_obj = 0.0
veloc_rotacao_obj = 5.0

def keyPressed(bkey, x, y):
    global rotacao_obj
    global veloc_rotacao_obj

    key = bkey.decode("utf-8")
    if key == 't' or key == 'T':
        for i in range(5):
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glMatrixMode(GL_MODELVIEW)
            glLoadIdentity()  # resetar o estado

            glTranslatef(0.20, 0.20, 0.0)
            glRotate(rotacao_obj, 0.0, 0.0, 1.0)
            glTranslatef(0.20, 0.20, 0.0)  # transformacao realizada primeiro
            rotacao_obj += veloc_rotacao_obj
            rotacao_obj %= 360


def display():
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(0.5, 0.0, 0.0)
    glVertex3f(0.0, 0.5, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glEnd()

    glFlush()
    time.sleep(1/60.0)  # fps

def mainTriangle():
    glutInit()
    glutCreateWindow('Triangulo')
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(640, 480)
    glutDisplayFunc(display)
    glutKeyboardFunc(keyPressed)
    glutIdleFunc(display)
    init()
    glutMainLoop()
