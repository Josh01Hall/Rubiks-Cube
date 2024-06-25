import vpython as vp, keyboard as kb, time, copy, itertools as iter, math


#Graphical renderer of Rubiks cube
class Cube_Renderer():


    # Creates the cube and all the pieces, and all rotational objects and vectors    
    def __init__(self):

        # Sets size of background in display window
        background = vp.canvas(background=vp.vec(1,1,1), width=1000, height=800)

        # Colours for the 3 layers of each set of pyramids, 6 surface colours and the interior colour of each piece
        colour_options = [vp.color.blue, vp.color.green, vp.color.white, vp.color.yellow, vp.color.red, vp.color.orange, vp.color.black]
        #                 Right          Left            Top             Bottom           Front         Back             Interior
        colours = []

        # Groups the colours for use when creating the pyramids
        for i in range(6):
            colours.append(([colour_options[i]] + [colour_options[6]] * 2)[::int((i % 2 - 0.5) * 2)])

        # Axis of each pyramid making up each piece
        axis = [[-1, 0, 0], [1, 0, 0], [0, -1, 0], [0, 1, 0], [0, 0, -1], [0, 0, 1]]

        # Position of each pyramid, relative to the centre of a piece
        position_vectors = [[i * (-0.5) for i in row] for row in axis]

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

        # Each piece of the cube
        pieces = 3 * [3 * [3 * [3 * []]]]
        self.__faces__ = []
        self.__cube__ = []

        # Each piece of the cube, from bottom back left, to top front right
        for y, z, x, in iter.product(range(3), range(3), range(3)):

            # Sides of each piece
            piece = []
            for s in range(6):

                # Creates the pyramids that make up the piece
                piece.append(vp.pyramid(color=colours[s][[y, x, z][math.floor(s/2)]], pos=vp.vec(*position_vectors[s]) + vp.vec(*piece_vectors[z][x][y]), axis=vp.vec(*axis[s]), size=vp.vec(0.5, 1, 1)))

            # Binds each side of each piece together, so they rotate together during turns
            pieces[y][z][x] = vp.compound(piece)
            self.__cube__.append(pieces[y][z][x])


        # Binds together the 9 cubes in each of the 6 faces, so they can be turned independent of the cube
        #     THIS IS CAUSING THE OTHER OBJECTS TO APPEAR, NEED TO FIGURE OUT WHY
        if True:
            self.__faces__ = [vp.compound([copy.copy(pieces[2][0][0]), copy.copy(pieces[2][0][1]), copy.copy(pieces[2][0][2]),
                                           copy.copy(pieces[2][1][0]), copy.copy(pieces[2][1][1]), copy.copy(pieces[2][1][2]), 
                                           copy.copy(pieces[2][2][0]), copy.copy(pieces[2][2][1]), copy.copy(pieces[2][2][2])]),    # White

                              vp.compound([copy.copy(pieces[0][0][0]), copy.copy(pieces[0][0][1]), copy.copy(pieces[0][0][2]),
                                           copy.copy(pieces[0][1][0]), copy.copy(pieces[0][1][1]), copy.copy(pieces[0][1][2]),
                                           copy.copy(pieces[0][2][0]), copy.copy(pieces[0][2][1]), copy.copy(pieces[0][2][2])]),    # Yellow

                              vp.compound([copy.copy(pieces[0][0][0]), copy.copy(pieces[0][1][0]), copy.copy(pieces[0][2][0]),
                                           copy.copy(pieces[1][0][0]), copy.copy(pieces[1][1][0]), copy.copy(pieces[1][2][0]),
                                           copy.copy(pieces[2][0][0]), copy.copy(pieces[2][1][0]), copy.copy(pieces[2][2][0])]),    # Green

                              vp.compound([copy.copy(pieces[0][0][2]), copy.copy(pieces[0][1][2]), copy.copy(pieces[0][2][2]),
                                           copy.copy(pieces[1][0][2]), copy.copy(pieces[1][1][2]), copy.copy(pieces[1][2][2]),
                                           copy.copy(pieces[2][0][2]), copy.copy(pieces[2][1][2]), copy.copy(pieces[2][2][2])]),    # Blue

                              vp.compound([copy.copy(pieces[2][2][0]), copy.copy(pieces[2][2][1]), copy.copy(pieces[2][2][2]),
                                           copy.copy(pieces[1][2][0]), copy.copy(pieces[1][2][1]), copy.copy(pieces[1][2][2]),
                                           copy.copy(pieces[0][2][0]), copy.copy(pieces[0][2][1]), copy.copy(pieces[0][2][2])]),    # Red

                              vp.compound([copy.copy(pieces[2][0][0]), copy.copy(pieces[2][0][1]), copy.copy(pieces[2][0][2]),
                                           copy.copy(pieces[1][0][0]), copy.copy(pieces[1][0][1]), copy.copy(pieces[1][0][2]),
                                           copy.copy(pieces[0][0][0]), copy.copy(pieces[0][0][1]), copy.copy(pieces[0][0][2])])]    # Orange

        #self.__cube__ = [self.__faces__ +  [pieces[1][1][1]]]

        # Binds all pieces together, so whole cube can be rotated
        self.__cube__ = vp.compound(self.__cube__)

        # Axes for cube rotations, all are reverse of pyramid 
        self.__rotational_axes__ = [[1,0,0], [-1,0,0], [0,1,0], [0,-1,0], [0,0,1], [0,0,-1], [0,0,0]]

        # Current turn being made and number of rotations left, if no turn is being made both are 0
        self.current_turn = 0
        self.turns_remaining = 0


    # Renders the cube, checking for user rotation and cube moves every frame
    def render(self):

        # Individual frame, allowing rotation and turns
        while True:
    
            # Check which keys have been pressed, and complete appropriate rotation ()
            keys = [-1]
            if kb.is_pressed("w"): keys.append(1)
            if kb.is_pressed("s"): keys.append(0)
            if kb.is_pressed("a"): keys.append(3)
            if kb.is_pressed("d"): keys.append(2)
            if kb.is_pressed("q"): keys.append(4)
            if kb.is_pressed("e"): keys.append(5)

            # If a turn is being made, turn the cube
            if self.current_turn != 0 and self.turns_remaining != 0:
                self.__turn__(self.current_turn)
            elif self.current_turn != 0 or self.turns_remaining != 0:
                bin = input("Erorr")

            # Rotate the cube
            self.__rotate__(keys)

            # Time between frames
            time.sleep(0.02)


    # Turn the face of the cube chosen by the user
    def __turn__(self, turn):
        
        self.__faces__

        self.turns_remaining -= 1
        if self.turns_remaining == 0:
            self.current_turn = 0


    # Rotate the cube based on user input
    def __rotate__(self, keys):

        # Add together rotations
        rotation = [0,0,0]
        for key in keys:
            rotation = [sum(x) for x in zip(rotation, self.__rotational_axes__[key])]

        # Rotate cube
        self.__cube__.rotate(angle=vp.radians(1.5), axis=vp.vec(*rotation), origin=vp.vec(0,0,0))


render = Cube_Renderer()
render.render()