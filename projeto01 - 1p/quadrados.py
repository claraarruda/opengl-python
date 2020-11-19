import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def drawSquares():
    glBegin(GL_QUADS)
    glVertex2f(0, 0)
    glVertex2f(0, 50)
    glVertex2f(50, 50)
    glVertex2f(50, 0)
    glEnd()

def mainSquares():
    pygame.init()
    display = (300,300)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluOrtho2D(0, 300, 0, 300)
    yEsq, yDir = 150, 150

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    print('DOWN PRESSED')
                    yDir = yDir - 5
                    yEsq = yEsq + 5
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    print('UP PRESSED')
                    yDir = yDir + 5
                    yEsq = yEsq - 5

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        glPushMatrix()
        glTranslated(200, yDir, 0)
        glColor3f(0.0, 1.0, 0.0)
        drawSquares()
        glPopMatrix()

        glPushMatrix()
        glTranslated(50, yEsq, 0)
        glColor3f(0.0, 0.0, 1.0)
        drawSquares()
        glPopMatrix()


        pygame.display.set_caption('Quadrados')
        pygame.display.flip()
