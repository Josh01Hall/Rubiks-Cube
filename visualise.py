import pygame, keyboard as kb, numpy as np, threading, itertools
from pygame import locals
from OpenGL import GL, GLU
import cube, move_window


class Visualiser():


    # Create all the objects needed
    def __init__(self):

        # Creates cube object
        self.myCube = cube.Cube()
        
        # Creates move_window object, then starts it in new thread so visualiser and move selector can run at the same time
        self.__mover_window__ = ""
        mover_thread = threading.Thread(target=self.__move_window__)
        mover_thread.start()

        # Indicator for if a move has been made by the user 
        self.__move_made__ = False

        # Rotations for possible button presses
        self.__rotations__ = [[-1, 0, 0], [1, 0, 0], [0, -1, 0], [0, 1, 0], [0, 0, 1], [0, 0, -1], [0, 0, 0]]

        # All points on cube surface 
        self.__verticies__ = []     
        skip = [-0.5, 0.5]
        vertex_values = [-1.5, -0.5, 0.5, 1.5]
        for y, z, x in itertools.product(vertex_values[::-1], vertex_values, vertex_values):
            if x not in skip or y not in skip or z not in skip:
                self.__verticies__.append([x, y, z])

        # All dividing lines on surface
        self.__edges__ = [
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
        self.__surfaces__ = [
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
    def __form_cube__(self):

        GL. glClear(GL.GL_COLOR_BUFFER_BIT|GL.GL_DEPTH_BUFFER_BIT)

        GL. glEnable(GL.GL_DEPTH_TEST)

        # Draw the colours of the tiles
        GL. glBegin(GL.GL_QUADS)
        for i in range(6):
            for j in range(3):
                for k in range(3):
                    for vertex in self.__surfaces__[i][j][k]:

                        GL.glColor3fv(self.myCube.get_colour(i, j, k))
                        GL.glVertex3fv(self.__verticies__[vertex])
        GL.glEnd()

        # Draw edges of tiles and the cube
        GL.glLineWidth(10)
        GL.glBegin(GL.GL_LINES)
        GL.glColor3fv([0,0,0])
        for edge in self.__edges__:
            for vertex in edge:                
                GL.glVertex3fv(self.__verticies__[vertex])
        GL.glEnd()


    # Display the cube
    def display_cube(self):
        pygame.init()
        # Dimensions of display window
        pygame.display.set_mode((1720, 880), locals.DOUBLEBUF|locals.OPENGL)
        GLU.gluPerspective(90, (1720/880), 0.1, 50.0)

        # Sets position of cube on screen, set to centre of x and y axis
        GL.glTranslatef(0, 0, -5)

        # Each frame of visualiser
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            if self.__move_made__ != False:
                self.myCube.rotate_face(self.__move_made__[0], self.__move_made__[1])
                self.__move_made__ = False

            # Checks if any arrow keys have been pressed
            keys = [-1]
            if kb.is_pressed("w"):
                keys.append(0)
            if kb.is_pressed("s"):
                keys.append(1)
            if kb.is_pressed("a"):
                keys.append(2)
            if kb.is_pressed("d"):
                keys.append(3)
            if kb.is_pressed("q"):
                keys.append(4)
            if kb.is_pressed("e"):
                keys.append(5)

            # If multiple keys are pressed at once, combines rotation directions
            rotation = np.sum([self.__rotations__[x] for x in keys], axis=0)

            # Rotate cube based on user inputs
            GL.glRotatef(1, rotation[0], rotation[1], rotation[2])

            # Draw cube
            self.__form_cube__()
            pygame.display.flip()

            # Frame rate
            pygame.time.wait(10)


    # Initiates wove_GUI object within its own thread
    def __move_window__(self):
       self.__mover_window__ = move_window.Move_GUI(self)


# https://pythonprogramming.net/opengl-rotating-cube-example-pyopengl-tutorial/