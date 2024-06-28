import vpython as vp, keyboard as kb, time, itertools as iter, math, copy, numpy as np


#Graphical renderer of Rubiks cube
class Cube_Renderer():


    # Creates the cube and all the pieces, and all rotational objects and vectors    
    def __init__(self):

        # Sets size of background in display window, and hides all objects until cube is fully rendered
        background = vp.canvas(background=vp.vec(1,1,1), width=1000, height=800)
        background.visible = False

        # Colours for the 3 layers of each set of pyramids, 6 surface colours and the interior colour of each piece
        colour_options = [vp.color.blue, vp.color.green, vp.color.white, vp.color.yellow, vp.color.red, vp.color.orange, vp.color.black]
        #                 Right          Left            Top             Bottom           Front         Back             Interior

        # Groups the colours for use when creating the pyramids
        colours = []
        for i in range(6):
            colours.append(([colour_options[i]] + [colour_options[6]] * 2)[::int((i % 2 - 0.5) * 2)])

        # Axis of each pyramid making up each piece, used when rendering the pyramids
        self.__render_axes__ = [[-1, 0, 0], [1, 0, 0], [0, -1, 0], [0, 1, 0], [0, 0, -1], [0, 0, 1]]

        # Axes for turns, initially the same as render_axes, but will need to be changed to account for cube rotation
        self.__turn_axes__ = copy.deepcopy([[component * -1 for component in axis] for axis in self.__render_axes__])

        # Position of each pyramid, relative to the centre of a piece
        position_vectors = [[component * (-0.5) for component in axis] for axis in self.__render_axes__]

        # Current turn being made and number of rotations left, if no turn is being made the variable is [0, 0]
        self.selected_turn = [0, 0]        

        # Position of each piece, relative to the centre of the cube, centre of the cube is at the origin
        piece_vectors = []
        for y in range(-1, 2):
            y_vectors = []
            for z in range(-1, 2):
                x_vectors = []
                for x in range(-1, 2):
                    x_vectors.append([x, z, y])
                y_vectors.append(x_vectors)
            piece_vectors.append(y_vectors)

        # Each piece of the cube, from bottom back left, to top front right
        self.__pieces__ = []
        for y in range(3):
            z_set = []
            for z in range(3):
                x_set = []
                for x in range(3):
                    piece = []
                    # Sides of each piece
                    for s in range(6):

                        # Creates the pyramids that make up the piece
                        piece.append(vp.pyramid(color=colours[s][[y, x, z][math.floor(s/2)]], pos=vp.vec(*position_vectors[s]) + vp.vec(*piece_vectors[z][x][y]), axis=vp.vec(*self.__render_axes__[s]), size=vp.vec(0.5, 1, 1)))
                    # Binds each side of each piece together, so they rotate together during turns
                    x_set.append(vp.compound(piece))
                z_set.append(x_set)
            self.__pieces__.append(z_set)

        # Coordinates of the 9 pieces in each face
        self.faces = [[[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [0, 1, 2], [0, 2, 0], [0, 2, 1], [0, 2, 2]],          # Green
                      [[2, 0, 0], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]],          # Blue
                      [[0, 0, 0], [0, 1, 0], [0, 2, 0], [1, 0, 0], [1, 1, 0], [1, 2, 0], [2, 0, 0], [2, 1, 0], [2, 2, 0]],          # Yellow
                      [[0, 0, 2], [0, 1, 2], [0, 2, 2], [1, 0, 2], [1, 1, 2], [1, 2, 2], [2, 0, 2], [2, 1, 2], [2, 2, 2]],          # White
                      [[0, 0, 0], [0, 0, 1], [0, 0, 2], [1, 0, 0], [1, 0, 1], [1, 0, 2], [2, 0, 0], [2, 0, 1], [2, 0, 2]],          # Orange
                      [[0, 2, 0], [0, 2, 1], [0, 2, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]]          # Red


        # When a face is turned, the coordinate references in self.faces need to be updated, this shows the how they change
        self.__reference_changes__ = []
        reference_template = [0, 3, 6, 7, 8, 5, 2, 1]

        for i in range(6):
            self.__reference_changes__.append(reference_template[::int((i % 2 - 0.5) * -2)])

        # For some reason orange and red reverse the flipping pattern, this accounts for it
        self.__reference_changes__[-2], self.__reference_changes__[-1] = self.__reference_changes__[-1], self.__reference_changes__[-2]

        # Makes objects visible now cube is fully rendered
        background.visible = True


    # Renders the cube, checking for user rotation and cube moves every frame
    def render(self):

        # Individual frame, allowing rotation and turns
        while True:
            # Check which keys have been pressed, and complete appropriate rotation ()
            keys = []
            if kb.is_pressed("w"): keys.append(1)
            if kb.is_pressed("s"):
                if 1 in keys:
                    keys.remove(1)
                else:
                    keys.append(0)
            if kb.is_pressed("a"): keys.append(3)
            if kb.is_pressed("d"):
                if 3 in keys:
                    keys.remove(3)
                else:
                    keys.append(2)                
            if kb.is_pressed("q"): keys.append(4)
            if kb.is_pressed("e"):
                if 3 in keys:
                    keys.remove(4)
                else:
                    keys.append(5) 

            # If a turn is being made, turn the cube
            if self.selected_turn != [0, 0]:
                self.__turn__()

            # If values have been added to keys, rotate the cube
            if keys != []: self.__rotate__(keys)

            # Time between frames
            time.sleep(0.005)


    # Turn the face of the cube chosen by the user
    def __turn__(self):

        # Pull coordinates needed for the turn selected, and rotate each of the corresponding cubes in the selected direction
        for [y, z, x] in self.faces[self.selected_turn[0][0]]:
            self.__pieces__[y][z][x].rotate(angle=vp.radians(1 * self.selected_turn[0][1]), axis=vp.vec(*self.__turn_axes__[self.selected_turn[0][0]]), origin=vp.vec(0,0,0))

        # Reduces the number of frames of rotation remaining. When it reaches 0, the rotation is complete and the piece references in each face need to be updates
        self.selected_turn[1] -= 1
        if self.selected_turn[1] == 0:

            # Pulls reference changes, and reverses the list if the turn was anticlockwise
            reference_moves = self.__reference_changes__[self.selected_turn[0][0]][::self.selected_turn[0][1]]

            # Pairs of initial and target pieces, so the references for each piece rotate along with the faces
            pairs = []
            for i in range(8):
                pairs.append([self.faces[self.selected_turn[0][0]][reference_moves[i % 8]], self.faces[self.selected_turn[0][0]][reference_moves[(i + 2) % 8]]])

            # For each input piece reference, every occurence in the cube is swapped to the target reference
            for face, piece in iter.product(range(6), range(9)):
                for pair in pairs:
                    # Move onto next piece after an input reference is found
                    if self.faces[face][piece] == pair[0]:
                        self.faces[face][piece] = pair[1]
                        break

            # As the move is complete, the selected_turn varaible is now empty
            self.selected_turn = [0,0]


    # Rotate the cube based on user input
    def __rotate__(self, keys):

        # Rotates in each of the chosen directions individually
        for key in keys:
            for y, z, x in iter.product(range(3), range(3), range(3)):
                self.__pieces__[y][z][x].rotate(angle=vp.radians(-0.35), axis=vp.vec(*self.__render_axes__[key]), origin=vp.vec(0,0,0))


            test = [0,2,1] 

            # x, ycos - zsin, ysin + zcos
            if self.__render_axes__[key][0] == 0:
                print(0)
                self.__turn_axes__[0] = [self.__turn_axes__[0][test[0]],
                                         self.__turn_axes__[0][test[1]] * math.cos(vp.radians(0.35)) - self.__turn_axes__[0][test[2]] * math.sin(vp.radians(0.35)),
                                         self.__turn_axes__[0][test[1]] * math.sin(vp.radians(0.35)) + self.__turn_axes__[0][test[2]] * math.cos(vp.radians(0.35))]
                self.__turn_axes__[1] = [self.__turn_axes__[1][test[0]],
                                         self.__turn_axes__[1][test[1]] * math.cos(vp.radians(0.35)) - self.__turn_axes__[1][test[2]] * math.sin(vp.radians(0.35)),
                                         self.__turn_axes__[1][test[1]] * math.sin(vp.radians(0.35)) + self.__turn_axes__[1][test[2]] * math.cos(vp.radians(0.35))]
            # xcos + zsin, y, -xsin + zcos
            if self.__render_axes__[key][1] == 0:
                print(1)
                self.__turn_axes__[2] = [self.__turn_axes__[2][test[0]] * math.cos(vp.radians(0.35)) + self.__turn_axes__[2][test[2]] * math.sin(vp.radians(0.35)),
                                         self.__turn_axes__[2][test[1]],
                                    -1 * self.__turn_axes__[2][test[0]] * math.sin(vp.radians(0.35)) + self.__turn_axes__[2][test[2]] * math.cos(vp.radians(0.35))]
                self.__turn_axes__[3] = [self.__turn_axes__[3][test[0]] * math.cos(vp.radians(0.35)) + self.__turn_axes__[3][test[2]] * math.sin(vp.radians(0.35)),
                                         self.__turn_axes__[3][test[1]],
                                    -1 * self.__turn_axes__[3][test[0]] * math.sin(vp.radians(0.35)) + self.__turn_axes__[3][test[2]] * math.cos(vp.radians(0.35))]
            # xcos - ysin, xsin + ycos, z
            if self.__render_axes__[key][2] == 0:
                print(2)
                self.__turn_axes__[4] = [self.__turn_axes__[4][test[0]] * math.cos(vp.radians(0.35)) - self.__turn_axes__[4][test[1]] * math.sin(vp.radians(0.35)),
                                         self.__turn_axes__[4][test[0]] * math.sin(vp.radians(0.35)) + self.__turn_axes__[4][test[1]] * math.cos(vp.radians(0.35)),
                                         self.__turn_axes__[4][test[2]]]
                self.__turn_axes__[5] = [self.__turn_axes__[5][test[0]] * math.cos(vp.radians(0.35)) - self.__turn_axes__[5][test[1]] * math.sin(vp.radians(0.35)),
                                         self.__turn_axes__[5][test[0]] * math.sin(vp.radians(0.35)) + self.__turn_axes__[5][test[1]] * math.cos(vp.radians(0.35)),
                                         self.__turn_axes__[5][test[2]]]
            #print(self.__render_axes__[key])  
        print(self.__turn_axes__)