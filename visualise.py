import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import keyboard as kb
import numpy as np

# Rotations for possible button presses
rotations = [[-1, 0, 0], [1, 0, 0], [0, -1, 0], [0, 1, 0], [0, 0, 0]]

# Corners points of all tiles on surface 
verticies = [

    # Up                   ###################################################################
    #UBL - UBR
    [-1.5,  1.5, -1.5],
    [-0.5,  1.5, -1.5],
    [ 0.5,  1.5, -1.5],
    [ 1.5,  1.5, -1.5],
    #UMBL - UMBR
    [-1.5,  1.5, -0.5],
    [-0.5,  1.5, -0.5],
    [ 0.5,  1.5, -0.5],
    [ 1.5,  1.5, -0.5],
    #UMFL - UMFR
    [-1.5,  1.5,  0.5],
    [-0.5,  1.5,  0.5],
    [ 0.5,  1.5,  0.5],
    [ 1.5,  1.5,  0.5],
    #UFL - UFR
    [-1.5,  1.5,  1.5],
    [-0.5,  1.5,  1.5],
    [ 0.5,  1.5,  1.5],
    [ 1.5,  1.5,  1.5],
    # Up Mid               ###################################################################
    #MUBL - MUBR
    [-1.5,  0.5, -1.5],
    [-0.5,  0.5, -1.5],
    [ 0.5,  0.5, -1.5],
    [ 1.5,  0.5, -1.5],
    #MUMBL - MUMBR
    [-1.5,  0.5, -0.5],
    [ 1.5,  0.5, -0.5],
    #MUMFL - MUMFR
    [-1.5,  0.5,  0.5],
    [ 1.5,  0.5,  0.5],
    #MUFL - MUFR
    [-1.5,  0.5,  1.5],
    [-0.5,  0.5,  1.5],
    [ 0.5,  0.5,  1.5],
    [ 1.5,  0.5,  1.5],
    # Down Mid             ###################################################################    
    #MDBL - MDBR
    [-1.5, -0.5, -1.5],
    [-0.5, -0.5, -1.5],
    [ 0.5, -0.5, -1.5],
    [ 1.5, -0.5, -1.5],
    #MDMBL - MDMBR
    [-1.5, -0.5, -0.5],
    [ 1.5, -0.5, -0.5],
    #MDMFL - MDMFR
    [-1.5, -0.5,  0.5],
    [ 1.5, -0.5,  0.5],
    #MDFL - MDFR
    [-1.5, -0.5,  1.5],
    [-0.5, -0.5,  1.5],
    [ 0.5, -0.5,  1.5],
    [ 1.5, -0.5,  1.5],
    # Down                 ###################################################################
    #DBL - DBR
    [-1.5, -1.5, -1.5],
    [-0.5, -1.5, -1.5],
    [ 0.5, -1.5, -1.5],
    [ 1.5, -1.5, -1.5],
    #DMBL - DMBR
    [-1.5, -1.5, -0.5],
    [-0.5, -1.5, -0.5],
    [ 0.5, -1.5, -0.5],
    [ 1.5, -1.5, -0.5],
    #DMFL - DMFR
    [-1.5, -1.5,  0.5],
    [-0.5, -1.5,  0.5],
    [ 0.5, -1.5,  0.5],
    [ 1.5, -1.5,  0.5],
    #DFL - DFR
    [-1.5, -1.5,  1.5],
    [-0.5, -1.5,  1.5],
    [ 0.5, -1.5,  1.5],
    [ 1.5, -1.5,  1.5]
    ]

# All dividing lines on surface
edges = [
    # X axis               ###################################################################
    #U
    [0,   3],
    [4,   7],
    [8,  11],
    [12, 15],
    #MU
    [16, 19],
    [24, 27],
    #MD
    [28, 31],
    [36, 39],
    #D
    [40, 43],
    [44, 47],
    [48, 51],
    [52, 55],

    # Y axis               ###################################################################
    #B
    [0,  40],
    [1,  41],
    [2,  42],
    [3,  43],
    #MB
    [4,  44],
    [7,  47],
    #MF
    [8,  48],
    [11, 51],
    #F
    [12, 52],
    [13, 53],
    [14, 54],
    [15, 55],

    # Z axis               ###################################################################
    #U
    [0,  12],
    [1,  13],
    [2,  14],
    [3,  15],
    #MU
    [16, 24],
    [19, 27],
    #MD
    [28, 36],
    [31, 39],
    #D
    [40, 52],
    [41, 53],
    [42, 54],
    [43, 55]
    ]

# Corners of all tiles
surfaces = [
    # Up                   ###################################################################
    [[[0, 1, 5, 4 ], [1, 2, 6, 5 ], [2, 3, 7, 6 ]],
     [[4, 5, 9, 8 ], [5, 6, 10,9 ], [6, 7, 11,10]],
     [[8, 9, 13,12], [9, 10,14,13], [10,11,15,14]]],

    # Down                 ###################################################################
    [[[43,42,46,47], [42,41,45,46], [41,40,44,45]],
     [[47,46,50,51], [46,45,49,50], [45,44,48,49]],
     [[51,50,54,55], [50,49,53,54], [49,48,52,53]]],

    # Left                 ###################################################################
    [[[0, 4, 20,16], [4, 8, 22,20], [8, 12,24,22]],
     [[16,20,32,28], [20,22,34,32], [22,24,36,34]],
     [[28,32,44,40], [32,34,48,44], [34,36,52,48]]],

    # Right                ###################################################################
    [[[15,11,23,27], [11, 7,21,23], [7, 3, 19,21]],
     [[27,23,35,39], [23,21,33,35], [21,19,31,33]],
     [[39,35,51,55], [35,33,47,51], [33,31,43,47]]],

    # Front                ###################################################################
    [[[12,13,25,24], [13,14,26,25], [14,15,27,26]],
     [[24,25,37,36], [25,26,38,37], [26,27,39,38]],
     [[36,37,53,52], [37,38,54,53], [38,39,55,54]]],

    # Back                 ###################################################################
    [[[3, 2, 18,19], [2, 1, 17,18], [1, 0, 16,17]],
     [[19,18,30,31], [18,17,29,30], [17,16,28,29]],
     [[31,30,42,43], [30,29,41,42], [29,28,40,41]]]
]

# Draw the cube
def form_cube(cube):

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    glEnable(GL_DEPTH_TEST)

    # Draw the colours of the tiles
    glBegin(GL_QUADS)
    for i in range(6):
        for j in range(3):
            for k in range(3):
                for vertex in surfaces[i][j][k]:

                    glColor3fv(cube.get_colour(i, j, k))
                    glVertex3fv(verticies[vertex])
    glEnd()

    # Draw edges of tiles and the cube
    glLineWidth(10)
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glColor3fv([0,0,0])
            glVertex3fv(verticies[vertex])
    glEnd()

# Display the cube
def display_cube(cube):
    pygame.init()
    # Dimensions of display window
    display = (1820,980)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(90, (display[0]/display[1]), 0.1, 50.0)
    
    # Sets position of cube on screen, set to centre of x and y axis
    glTranslatef(0.0,0.0, -5)


    # Each frame of visualiser
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Checks if any arrow keys have been pressed
        keys = [-1]
        if kb.is_pressed("up arrow"):
            keys.append(0)
        if kb.is_pressed("down arrow"):
            keys.append(1)
        if kb.is_pressed("left arrow"):
            keys.append(2)
        if kb.is_pressed("right arrow"):
            keys.append(3)

        # If multiple keys are pressed at once, combines rotation directions
        rotation = np.sum([rotations[x] for x in keys], axis=0)
        current_angle = 1
        # Rotate cube based on user inputs
        glRotatef(current_angle, rotation[0], rotation[1], rotation[2])
        # Draw cube
        form_cube(cube)
        pygame.display.flip()
        # Frame rate
        pygame.time.wait(10)

# https://pythonprogramming.net/opengl-rotating-cube-example-pyopengl-tutorial/