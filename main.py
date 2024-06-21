import cube
import visualise

myCube = cube.Cube()
myCube.rotate_face(0,1)
myCube.rotate_face(0,-1)

myCube.rotate_face(1,1)
myCube.rotate_face(1,-1)

myCube.rotate_face(2,1)
myCube.rotate_face(2,-1)

myCube.rotate_face(3,1)
myCube.rotate_face(3,-1)

myCube.rotate_face(4,1)
myCube.rotate_face(4,-1)

myCube.rotate_face(5,1)
myCube.rotate_face(5,-1)
visualise.display_cube(myCube)