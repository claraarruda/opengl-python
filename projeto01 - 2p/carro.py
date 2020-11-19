import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from math import *

pi = 3.14


def drawCircle():
    glBegin(GL_POLYGON)
    for i in range(360):
        angle = 2 * pi * i / 360
        x = cos(angle)
        y = sin(angle)
        glVertex2f(x, y)
    glEnd()

def drawCircleOutlined():
    glBegin(GL_POLYGON)
    for i in range(360):
        angle = 2 * pi * i / 360
        x = cos(angle)
        y = sin(angle)
        glVertex2f(x, y)
    glColor3f(0.0, 0.0, 0.0)
    glVertex2f(15, 10)
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(10, 15)
    glColor3f(0.0, 0.0, 0.0)
    glVertex2f(-15, -10)
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(-10, -15)
    
    glEnd()

def drawSquares():
    glBegin(GL_QUADS)
    glVertex2f(0, 0)
    glVertex2f(0, 50)
    glVertex2f(50, 50)
    glVertex2f(50, 0)
    glEnd()


def mainSquares():
    pygame.init()
    display = (600, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluOrtho2D(0, 300, 0, 300)
    
    xParabrisa = 75
    xBase = 75
    xTeto = 130
    xCirEsq = 100
    xCirDir = 150

    yParabrisa = 100
    yBase = 80
    yTeto = 110
    yCirEsq = 80
    yCirDir = 80

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    print('DOWN PRESSED')
                    yParabrisa = yParabrisa - 5
                    yBase = yBase - 5
                    yTeto = yTeto - 5
                    yCirEsq = yCirEsq - 5
                    yCirDir = yCirDir - 5
                elif event.key == pygame.K_LEFT:
                    print('LEFT PRESSED')
                    xParabrisa = xParabrisa - 5
                    xBase = xBase - 5
                    xTeto = xTeto - 5
                    xCirEsq = xCirEsq - 5
                    xCirDir = xCirDir - 5
                elif event.key == pygame.K_RIGHT:
                    print('RIGHT PRESSED')
                    xParabrisa = xParabrisa + 5
                    xBase = xBase + 5
                    xTeto = xTeto + 5
                    xCirEsq = xCirEsq + 5
                    xCirDir = xCirDir + 5
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    print('UP PRESSED')
                    yParabrisa = yParabrisa + 5
                    yBase = yBase + 5
                    yTeto = yTeto + 5
                    yCirEsq = yCirEsq + 5
                    yCirDir = yCirDir + 5

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glPushMatrix()
        glTranslatef(xTeto, yTeto, 0.0)
        glScalef(30, 30, 30)
        glColor3f(0.0, 0.0, 1.0)
        drawCircle()
        glFlush()
        glPopMatrix()

        glPushMatrix()
        glTranslated(xBase, yBase, 0)
        glScalef(2.0, 0.7, 0)
        glColor3f(0.0, 0.0, 1.0)
        drawSquares()
        glPopMatrix()

        glPushMatrix()
        glTranslated(xParabrisa, yParabrisa, 0)
        glScalef(0.3, 0.3, 0)
        glColor3f(0.0, 1.0, 1.0)
        drawSquares()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(xCirDir, yCirDir, 0.0)
        glScalef(10, 10, 10)
        glColor3f(0.5, 0.5, 0.5)
        drawCircle()
        glFlush()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(xCirEsq, yCirEsq, 0.0)
        glScalef(10, 10, 10)
        glColor3f(0.5, 0.5, 0.5)
        drawCircle()
        glFlush()
        glPopMatrix()

        # glPushMatrix()
        # glTranslatef(xCirEsq, yCirEsq, 0.0)
        # glScalef(0.5, 0.5, 0.5)
        # drawCircleOutlined()
        # glFlush()
        # glPopMatrix()

        # glPushMatrix()
        # glTranslatef(xCirDir, yCirDir, 0.0)
        # glScalef(0.5, 0.5, 0.5)
        # drawCircleOutlined()
        # glFlush()
        # glPopMatrix()

        pygame.display.flip()

mainSquares()
