import math
import numpy as np
class Cube:
    def __init__(self):

        # Defines the colours and side labels
        self.colours = [[255,255,255], [255,255,0], [255,128,0], [255,0,0], [0,255,0], [0,0,255]]
        #              White           Yellow       Orange       Red        Green      Blue
        self.side_labels = ["U", "D", "L", "R", "F", "B"]

        # Defines the cube surface

        self.faces = [np.full((3, 3), 0),
                      np.full((3, 3), 1),
                      np.full((3, 3), 2),
                      np.full((3, 3), 3),
                      np.full((3, 3), 4),
                      np.full((3, 3), 5)]

        # Define the surface changes for each rotation
        self.links = [
            [(5, "Uf"), (3, "Uf"), (4, "Uf"), (2, "Uf")],
            [(0, "Lf"), (4, "Lf"), (1, "Rr"), (5, "Rr")],
            [(0, "Df"), (3, "Lf"), (1, "Dr"), (2, "Rr")]
            ]


    # Rotates the chosen side in the desired direction   
    def rotate_face(self, side, direction):

        # Finds the face to turn
        face_index = self.side_labels.index(side)

        # Finds the correct series of movements
        cycle = self.links[math.floor(face_index / 2)]

        # rotates the turning face in the chosen direction
        self.faces[face_index] = np.rot90(self.faces[face_index], k=(2 * direction + 1))

        # Moves the edges of the faces connected to the rotating face
        "Change it to make temp from end of cycle, not start"
        temp = self.get_edge(cycle[0][0], cycle[0][1][0])
        # Reversible for loop
        for i in range(1 * direction, 4 * direction, direction):
            "Add Reverser"
            
            placeholder = self.get_edge(cycle[i][0], cycle[i][1][0])



    def get_edge(self, side, edge):
        return 1


def main():
    myCube = Cube()
    myCube.rotate_face("U", 1)
    myCube.rotate_face("U", -1)

main()