import numpy as np, copy


class Cube:


    # Defines cube, colours, and moves
    def __init__(self):

        # Defines the colours and side labels
        self.__colours__ = [[1,1,1], [1,1,0], [1,0.5,0], [1,0,0], [0,1,0], [0,0,1]]
        #                   White    Yellow   Orange     Red      Green    Blue
        self.__side_labels__ = ["U", "D",   "L",   "R",   " F",    "B"]
        #                        Up   Done   Left   Right   Front   Back

        # Defines the cube surface

        self.faces = [np.full((3, 3), 0),
                      np.full((3, 3), 1),
                      np.full((3, 3), 2),
                      np.full((3, 3), 3),
                      np.full((3, 3), 4),
                      np.full((3, 3), 5)]

        # Define the surface changes for each rotation
        self.__links__ = [
            [(5, "Uf"), (3, "Uf"), (4, "Uf"), (2, "Uf")],
            [(2, "Df"), (4, "Df"), (3, "Df"), (5, "Df")],
            [(0, "Lf"), (4, "Lf"), (1, "Rr"), (5, "Rr")],
            [(5, "Lr"), (1, "Lr"), (4, "Rf"), (0, "Rf")],
            [(0, "Df"), (3, "Lf"), (1, "Dr"), (2, "Rr")],
            [(2, "Lr"), (1, "Ur"), (3, "Rf"), (0, "Uf")]
        ]


    # Rotates the chosen side in the desired direction
    def rotate_face(self, side, direction):

        # Finds the correct series of movements
        cycle = self.__links__[side]

        # rotates the turning face in the chosen direction
        self.faces[side] = np.rot90(self.faces[side], k=(direction + 2))

        # Moves the edges of the faces connected to the rotating face, either clockwise or anticlockwise
        # Gets tiles to be moved to current face
        first_placeholder = copy.deepcopy(self.get_edge(cycle[int(1.5 * direction + 1.5)][0], cycle[int(1.5 * direction + 1.5)][1][0]))
        # Reverses tiles depending on orientation
        if cycle[0][1][1] != cycle [3][1][1]:
            first_placeholder = first_placeholder[::-1]
        
        # Reversible for loop
        for i in range(int(1.5 * direction + 1.5), int(-1.5 * direction + 1.5), -1 * direction):   
            # Gets tiles to be moved to current face         
            placeholder = self.get_edge(cycle[i - direction][0], cycle[i - direction][1][0])
            # Reverses tiles depending on orientation
            if cycle[i][1][1] != cycle [i - direction][1][1]:
                placeholder = placeholder[::-1]

            self.set_edge(placeholder, cycle[i][0], cycle[i][1][0])

        self.set_edge(first_placeholder, cycle[int(-1.5 * direction + 1.5)][0], cycle[int(-1.5 * direction + 1.5)][1][0])


    # Gets the edge values to be moved
    def get_edge(self, face, edge):
        edge_index = self.__side_labels__.index(edge)
        # Up and Down edge can pull the entire list, but Left and Right need to pull individual value from each list
        if edge in "UD":
            return self.faces[face][int((edge_index % 2) * -1)]
        else:
            return [i[int((edge_index % 2) * -1)] for i in self.faces[face]]

    
    # Moves the edge values onto their new side
    def set_edge(self, values, face, edge):
        edge_index = self.__side_labels__.index(edge)
        # Up and Down edge can input the entire list, but Left and Right need to input individual value to each list
        if edge in "UD":
            self.faces[face][int((edge_index % 2) * -1)] = values
        else:
            for i in range(3):
                self.faces[face][i][int((edge_index % 2) * -1)] = values[i]
    

    # Gives RGB colour of an indivual tile
    def get_colour(self, face, x, y):
        return self.__colours__[self.faces[face][x][y]]