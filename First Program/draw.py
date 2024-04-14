import sys
import random
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Constants
GRID_SIZE = 10
GRID_WIDTH = 50
GRID_HEIGHT = 50
WINDOW_WIDTH = GRID_SIZE * GRID_WIDTH
WINDOW_HEIGHT = GRID_SIZE * GRID_HEIGHT
SNAKE_INITIAL_LENGTH = 3
UPDATE_INTERVAL = 200  # milliseconds
# mood_selection = int(input("Enter 0 for easy and 1 for hard mood: "))
# if mood_selection not in [0,1]:
#     sys.exit('NO GAME FOR YOU!!!')




# Directions
DIR_UP = 1
DIR_DOWN = -1
DIR_LEFT = 2
DIR_RIGHT = -2

# Colors
COLOR_SNAKE = (0, 1, 0)
COLOR_FOOD = (1, 0, 0)

# Variables
snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
direction = DIR_DOWN
food = None
score = 0


def draw_points(x, y):
    glPointSize(1) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x,y) #jekhane show korbe pixel
    glEnd()

# MidPoint Line Drawing Algorithm
# ********************************************************************************************
def midpoint_Line_Drawing(zone,x1,y1,x2,y2):
    dx = x2-x1
    dy = y2-y1
    d = 2*dy-dx
    d_diff = 2*(dy-dx)

    x = x1
    y= y1

    while x<=x2:
        a,b = originalZone(zone,x,y)
        draw_points(a,b)
        
        if d <= 0:
            d+= d+2*dy
            x+=1
        else:
            x+=1
            y+=1
            d = d+ d_diff

def findZone(x1,y1,x2,y2):
    dx= x2-x1
    dy= y2-y1

    if abs(dx) > abs(dy):
        if dx>0 and dy>0:
            return 0
        elif dx<0 and dy>0:
            return 3
        elif dx<0 and dy<0:
            return 4
        else:
            return 7
        
    else:
        if dx>0 and dy>0:
            return 1
        elif dx<0 and dy > 0:
            return 2
        elif dx<0 and dy<0:
            return 5
        else:
            return 6
        
def zeroZone(zone,x,y):
    if zone == 0:
        return x,y
    elif zone == 1:
        return y, x
    elif zone == 2:
        return y,-x
    elif zone == 3:
        return -x,y
    elif zone == 4:
        return -x,-y
    elif zone == 5:
        return -y,-x
    elif zone == 6:
        return -y,x
    elif zone == 7:
        return x,-y
    
def originalZone(zone,x,y):
    if zone == 0:
        return x,y
    elif zone == 1:
        return y, x
    elif zone == 2:
        return -y,x
    elif zone == 3:
        return -x,y
    elif zone == 4:
        return -x,-y
    elif zone == 5:
        return -y,-x
    elif zone == 6:
        return y,-x
    elif zone == 7:
        return x,-y
    
def draw_line(x1,y1,x2,y2):
    zone = findZone(x1,y1,x2,y2)
    x1, y1 = zeroZone(zone,x1,y1)
    x2,y2 = zeroZone(zone,x2,y2)
    midpoint_Line_Drawing(zone,x1,y1,x2,y2)
# ***************************************************************************************


def draw_rect(x, y, grid, color):
    glColor3f(*color)
    
    # Draw bottom line
    draw_line(x, y, x + grid, y)
    
    # Draw left line
    draw_line(x, y + grid, x, y)
    
    # Draw top line
    draw_line(x, y + grid, x + grid, y + grid)  # Adjusted endpoints
    
    # Draw right line
    draw_line(x + grid +1, y+1, x + grid, y + grid)  # Adjusted endpoints






def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    draw_rect(250,250,10,(1,0,0))
    # draw_line(100, 100, 200, 200)  # Draw a line from (100, 100) to (200, 200)
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
glutCreateWindow(b"Snake Game")
glClearColor(0, 0, 0, 1)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluOrtho2D(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT)
glutDisplayFunc(display)
glutMainLoop()

