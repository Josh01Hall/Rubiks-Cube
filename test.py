import vpython as vp, keyboard as kb, time, copy, itertools as iter

#box = vp.box(pos=vp.vector(0,0,0), size=vp.vector(10, 10, 10), color=vp.color.red)

background = vp.canvas(background=vp.vec(1,1,1), width=1000, height=800)

cube_ULB = vp.compound([vp.pyramid(color=vp.color.white,  pos=vp.vec(-1,   1.5, -1),   axis=vp.vec( 0, -1,  0), size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.black,  pos=vp.vec(-1,   0.5, -1),   axis=vp.vec( 0,  1,  0), size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.green,  pos=vp.vec(-1.5, 1,   -1),   axis=vp.vec( 1,  0,  0), size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.black,  pos=vp.vec(-0.5, 1,   -1),   axis=vp.vec(-1,  0,  0), size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.black,  pos=vp.vec(-1,   1,   -0.5), axis=vp.vec( 0,  0, -1), size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.orange, pos=vp.vec(-1,   1,   -1.5), axis=vp.vec( 0,  0,  1), size=vp.vec(0.5,1,1))])
cube_UMB = vp.compound([vp.pyramid(color=vp.color.white,  pos=vp.vec( 0,   1.5, -1),   axis=vp.vec( 0, -1,  0), size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.black,  pos=vp.vec( 0,   0.5, -1),   axis=vp.vec( 0,  1,  0), size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.black,  pos=vp.vec(-0.5, 1,   -1),   axis=vp.vec( 1,  0,  0), size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.black,  pos=vp.vec( 0.5, 1,   -1),   axis=vp.vec(-1,  0,  0), size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.black,  pos=vp.vec( 0,   1,   -0.5), axis=vp.vec( 0,  0, -1), size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.orange, pos=vp.vec( 0,   1,   -1.5), axis=vp.vec( 0,  0,  1), size=vp.vec(0.5,1,1))])
cube_URB = vp.compound([vp.pyramid(color=vp.color.white,  pos=vp.vec(1,   1.5, -1),    axis=vp.vec( 0, -1,  0), size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.black,  pos=vp.vec(1,   0.5, -1),    axis=vp.vec( 0,  1,  0), size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.black,  pos=vp.vec(0.5, 1,   -1),    axis=vp.vec( 1,  0,  0), size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.blue,   pos=vp.vec(1.5, 1,   -1),    axis=vp.vec(-1,  0,  0), size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.black,  pos=vp.vec(1,   1,   -0.5),  axis=vp.vec( 0,  0, -1), size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.orange, pos=vp.vec(1,   1,   -1.5),  axis=vp.vec( 0,  0,  1), size=vp.vec(0.5,1,1))])
cube_ULM = vp.compound([vp.pyramid(color=vp.color.white,  pos=vp.vec(-1,   1.5, 0),    axis=vp.vec( 0, -1,  0), size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.black,  pos=vp.vec(-1,   0.5, 0),    axis=vp.vec( 0,  1,  0), size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.green,  pos=vp.vec(-1.5, 1,   0),    axis=vp.vec( 1,  0,  0), size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.black,  pos=vp.vec(-0.5, 1,   0),    axis=vp.vec(-1,  0,  0), size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.black,  pos=vp.vec(-1,   1,   0.5),  axis=vp.vec( 0,  0, -1), size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.black,  pos=vp.vec(-1,   1,  -0.5),  axis=vp.vec( 0,  0,  1), size=vp.vec(0.5,1,1))])
cube_UMM = vp.compound([vp.pyramid(color=vp.color.white,  pos=vp.vec( 0,   1.5, 0),    axis=vp.vec( 0, -1,  0), size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.black,  pos=vp.vec( 0,   0.5, 0),    axis=vp.vec( 0,  1,  0), size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.black,  pos=vp.vec(-0.5, 1,   0),    axis=vp.vec( 1,  0,  0), size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.black,  pos=vp.vec( 0.5, 1,   0),    axis=vp.vec(-1,  0,  0), size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.black,  pos=vp.vec( 0,   1,   0.5),  axis=vp.vec( 0,  0, -1), size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.black,  pos=vp.vec( 0,   1,  -0.5),  axis=vp.vec( 0,  0,  1), size=vp.vec(0.5,1,1))])
cube_URM = vp.compound([vp.pyramid(color=vp.color.white,  pos=vp.vec(1,   1.5, 0),     axis=vp.vec( 0, -1,  0), size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.black,  pos=vp.vec(1,   0.5, 0),     axis=vp.vec( 0,  1,  0), size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.black,  pos=vp.vec(0.5, 1,   0),     axis=vp.vec( 1,  0,  0), size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.blue,   pos=vp.vec(1.5, 1,   0),     axis=vp.vec(-1,  0,  0), size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.black,  pos=vp.vec(1,   1,   0.5),   axis=vp.vec( 0,  0, -1), size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.black,  pos=vp.vec(1,   1,  -0.5),   axis=vp.vec( 0,  0,  1), size=vp.vec(0.5,1,1))])
cube_ULF = vp.compound([vp.pyramid(color=vp.color.white,  pos=vp.vec(-1,   1.5, 1),    axis=vp.vec( 0, -1,  0), size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.black,  pos=vp.vec(-1,   0.5, 1),    axis=vp.vec( 0,  1,  0), size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.green,  pos=vp.vec(-1.5, 1,   1),    axis=vp.vec( 1,  0,  0), size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.black,  pos=vp.vec(-0.5, 1,   1),    axis=vp.vec(-1,  0,  0), size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.red,    pos=vp.vec(-1,   1,   1.5),  axis=vp.vec( 0,  0, -1), size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.black,  pos=vp.vec(-1,   1,   0.5),  axis=vp.vec( 0,  0,  1), size=vp.vec(0.5,1,1))])
cube_UMF = vp.compound([vp.pyramid(color=vp.color.white,  pos=vp.vec( 0,   1.5, 1),    axis=vp.vec( 0, -1,  0), size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.black,  pos=vp.vec( 0,   0.5, 1),    axis=vp.vec( 0,  1,  0), size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.black,  pos=vp.vec(-0.5, 1,   1),    axis=vp.vec( 1,  0,  0), size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.black,  pos=vp.vec( 0.5, 1,   1),    axis=vp.vec(-1,  0,  0), size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.red,    pos=vp.vec( 0,   1,   1.5),  axis=vp.vec( 0,  0, -1), size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.black,  pos=vp.vec( 0,   1,   0.5),  axis=vp.vec( 0,  0,  1), size=vp.vec(0.5,1,1))])
cube_URF = vp.compound([vp.pyramid(color=vp.color.white,  pos=vp.vec(1,   1.5, 1),     axis=vp.vec( 0, -1,  0), size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.black,  pos=vp.vec(1,   0.5, 1),     axis=vp.vec( 0,  1,  0), size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.black,  pos=vp.vec(0.5, 1,   1),     axis=vp.vec( 1,  0,  0), size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.blue,   pos=vp.vec(1.5, 1,   1),     axis=vp.vec(-1,  0,  0), size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.red,    pos=vp.vec(1,   1,   1.5),   axis=vp.vec( 0,  0, -1), size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.black,  pos=vp.vec(1,   1,   0.5),   axis=vp.vec( 0,  0,  1), size=vp.vec(0.5,1,1))])
'''
cube_MLB = vp.compound([vp.pyramid(color=vp.color.white, pos=vp.vec(0,   0.5,0),    axis=vp.vec(0,-1, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.yellow, pos=vp.vec(0,  -0.5,0),    axis=vp.vec(0, 1, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.green,  pos=vp.vec(-0.5,0,  0),    axis=vp.vec(1, 0, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.blue,   pos=vp.vec(0.5, 0,  0),    axis=vp.vec(-1,0, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.red,    pos=vp.vec(0,   0,  0.5),  axis=vp.vec(0, 0,-1),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.orange, pos=vp.vec(0,   0, -0.5),  axis=vp.vec(0, 0, 1),  size=vp.vec(0.5,1,1))])
cube_MMB = vp.compound([vp.pyramid(color=vp.color.white, pos=vp.vec(0,   0.5,0),    axis=vp.vec(0,-1, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.yellow, pos=vp.vec(0,  -0.5,0),    axis=vp.vec(0, 1, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.green,  pos=vp.vec(-0.5,0,  0),    axis=vp.vec(1, 0, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.blue,   pos=vp.vec(0.5, 0,  0),    axis=vp.vec(-1,0, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.red,    pos=vp.vec(0,   0,  0.5),  axis=vp.vec(0, 0,-1),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.orange, pos=vp.vec(0,   0, -0.5),  axis=vp.vec(0, 0, 1),  size=vp.vec(0.5,1,1))])
cube_MRB = vp.compound([vp.pyramid(color=vp.color.white, pos=vp.vec(0,   0.5,0),    axis=vp.vec(0,-1, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.yellow, pos=vp.vec(0,  -0.5,0),    axis=vp.vec(0, 1, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.green,  pos=vp.vec(-0.5,0,  0),    axis=vp.vec(1, 0, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.blue,   pos=vp.vec(0.5, 0,  0),    axis=vp.vec(-1,0, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.red,    pos=vp.vec(0,   0,  0.5),  axis=vp.vec(0, 0,-1),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.orange, pos=vp.vec(0,   0, -0.5),  axis=vp.vec(0, 0, 1),  size=vp.vec(0.5,1,1))])
cube_MLM = vp.compound([vp.pyramid(color=vp.color.white, pos=vp.vec(0,   0.5,0),    axis=vp.vec(0,-1, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.yellow, pos=vp.vec(0,  -0.5,0),    axis=vp.vec(0, 1, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.green,  pos=vp.vec(-0.5,0,  0),    axis=vp.vec(1, 0, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.blue,   pos=vp.vec(0.5, 0,  0),    axis=vp.vec(-1,0, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.red,    pos=vp.vec(0,   0,  0.5),  axis=vp.vec(0, 0,-1),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.orange, pos=vp.vec(0,   0, -0.5),  axis=vp.vec(0, 0, 1),  size=vp.vec(0.5,1,1))])
cube_MMM = vp.compound([vp.pyramid(color=vp.color.white, pos=vp.vec(0,   0.5,0),    axis=vp.vec(0,-1, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.yellow, pos=vp.vec(0,  -0.5,0),    axis=vp.vec(0, 1, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.green,  pos=vp.vec(-0.5,0,  0),    axis=vp.vec(1, 0, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.blue,   pos=vp.vec(0.5, 0,  0),    axis=vp.vec(-1,0, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.red,    pos=vp.vec(0,   0,  0.5),  axis=vp.vec(0, 0,-1),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.orange, pos=vp.vec(0,   0, -0.5),  axis=vp.vec(0, 0, 1),  size=vp.vec(0.5,1,1))])
cube_MRM = vp.compound([vp.pyramid(color=vp.color.white, pos=vp.vec(0,   0.5,0),    axis=vp.vec(0,-1, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.yellow, pos=vp.vec(0,  -0.5,0),    axis=vp.vec(0, 1, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.green,  pos=vp.vec(-0.5,0,  0),    axis=vp.vec(1, 0, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.blue,   pos=vp.vec(0.5, 0,  0),    axis=vp.vec(-1,0, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.red,    pos=vp.vec(0,   0,  0.5),  axis=vp.vec(0, 0,-1),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.orange, pos=vp.vec(0,   0, -0.5),  axis=vp.vec(0, 0, 1),  size=vp.vec(0.5,1,1))])
cube_MLF = vp.compound([vp.pyramid(color=vp.color.white, pos=vp.vec(0,   0.5,0),    axis=vp.vec(0,-1, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.yellow, pos=vp.vec(0,  -0.5,0),    axis=vp.vec(0, 1, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.green,  pos=vp.vec(-0.5,0,  0),    axis=vp.vec(1, 0, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.blue,   pos=vp.vec(0.5, 0,  0),    axis=vp.vec(-1,0, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.red,    pos=vp.vec(0,   0,  0.5),  axis=vp.vec(0, 0,-1),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.orange, pos=vp.vec(0,   0, -0.5),  axis=vp.vec(0, 0, 1),  size=vp.vec(0.5,1,1))])
cube_MMF = vp.compound([vp.pyramid(color=vp.color.white, pos=vp.vec(0,   0.5,0),    axis=vp.vec(0,-1, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.yellow, pos=vp.vec(0,  -0.5,0),    axis=vp.vec(0, 1, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.green,  pos=vp.vec(-0.5,0,  0),    axis=vp.vec(1, 0, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.blue,   pos=vp.vec(0.5, 0,  0),    axis=vp.vec(-1,0, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.red,    pos=vp.vec(0,   0,  0.5),  axis=vp.vec(0, 0,-1),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.orange, pos=vp.vec(0,   0, -0.5),  axis=vp.vec(0, 0, 1),  size=vp.vec(0.5,1,1))])
cube_MRF = vp.compound([vp.pyramid(color=vp.color.white, pos=vp.vec(0,   0.5,0),    axis=vp.vec(0,-1, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.yellow, pos=vp.vec(0,  -0.5,0),    axis=vp.vec(0, 1, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.green,  pos=vp.vec(-0.5,0,  0),    axis=vp.vec(1, 0, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.blue,   pos=vp.vec(0.5, 0,  0),    axis=vp.vec(-1,0, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.red,    pos=vp.vec(0,   0,  0.5),  axis=vp.vec(0, 0,-1),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.orange, pos=vp.vec(0,   0, -0.5),  axis=vp.vec(0, 0, 1),  size=vp.vec(0.5,1,1))])

cube_DLB = vp.compound([vp.pyramid(color=vp.color.white, pos=vp.vec(0,   0.5,0),    axis=vp.vec(0,-1, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.yellow, pos=vp.vec(0,  -0.5,0),    axis=vp.vec(0, 1, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.green,  pos=vp.vec(-0.5,0,  0),    axis=vp.vec(1, 0, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.blue,   pos=vp.vec(0.5, 0,  0),    axis=vp.vec(-1,0, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.red,    pos=vp.vec(0,   0,  0.5),  axis=vp.vec(0, 0,-1),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.orange, pos=vp.vec(0,   0, -0.5),  axis=vp.vec(0, 0, 1),  size=vp.vec(0.5,1,1))])
cube_DMB = vp.compound([vp.pyramid(color=vp.color.white, pos=vp.vec(0,   0.5,0),    axis=vp.vec(0,-1, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.yellow, pos=vp.vec(0,  -0.5,0),    axis=vp.vec(0, 1, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.green,  pos=vp.vec(-0.5,0,  0),    axis=vp.vec(1, 0, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.blue,   pos=vp.vec(0.5, 0,  0),    axis=vp.vec(-1,0, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.red,    pos=vp.vec(0,   0,  0.5),  axis=vp.vec(0, 0,-1),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.orange, pos=vp.vec(0,   0, -0.5),  axis=vp.vec(0, 0, 1),  size=vp.vec(0.5,1,1))])
cube_DRB = vp.compound([vp.pyramid(color=vp.color.white, pos=vp.vec(0,   0.5,0),    axis=vp.vec(0,-1, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.yellow, pos=vp.vec(0,  -0.5,0),    axis=vp.vec(0, 1, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.green,  pos=vp.vec(-0.5,0,  0),    axis=vp.vec(1, 0, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.blue,   pos=vp.vec(0.5, 0,  0),    axis=vp.vec(-1,0, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.red,    pos=vp.vec(0,   0,  0.5),  axis=vp.vec(0, 0,-1),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.orange, pos=vp.vec(0,   0, -0.5),  axis=vp.vec(0, 0, 1),  size=vp.vec(0.5,1,1))])
cube_DLM = vp.compound([vp.pyramid(color=vp.color.white, pos=vp.vec(0,   0.5,0),    axis=vp.vec(0,-1, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.yellow, pos=vp.vec(0,  -0.5,0),    axis=vp.vec(0, 1, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.green,  pos=vp.vec(-0.5,0,  0),    axis=vp.vec(1, 0, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.blue,   pos=vp.vec(0.5, 0,  0),    axis=vp.vec(-1,0, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.red,    pos=vp.vec(0,   0,  0.5),  axis=vp.vec(0, 0,-1),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.orange, pos=vp.vec(0,   0, -0.5),  axis=vp.vec(0, 0, 1),  size=vp.vec(0.5,1,1))])
cube_DMM = vp.compound([vp.pyramid(color=vp.color.white, pos=vp.vec(0,   0.5,0),    axis=vp.vec(0,-1, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.yellow, pos=vp.vec(0,  -0.5,0),    axis=vp.vec(0, 1, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.green,  pos=vp.vec(-0.5,0,  0),    axis=vp.vec(1, 0, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.blue,   pos=vp.vec(0.5, 0,  0),    axis=vp.vec(-1,0, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.red,    pos=vp.vec(0,   0,  0.5),  axis=vp.vec(0, 0,-1),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.orange, pos=vp.vec(0,   0, -0.5),  axis=vp.vec(0, 0, 1),  size=vp.vec(0.5,1,1))])
cube_DRM = vp.compound([vp.pyramid(color=vp.color.white, pos=vp.vec(0,   0.5,0),    axis=vp.vec(0,-1, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.yellow, pos=vp.vec(0,  -0.5,0),    axis=vp.vec(0, 1, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.green,  pos=vp.vec(-0.5,0,  0),    axis=vp.vec(1, 0, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.blue,   pos=vp.vec(0.5, 0,  0),    axis=vp.vec(-1,0, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.red,    pos=vp.vec(0,   0,  0.5),  axis=vp.vec(0, 0,-1),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.orange, pos=vp.vec(0,   0, -0.5),  axis=vp.vec(0, 0, 1),  size=vp.vec(0.5,1,1))])
cube_DLF = vp.compound([vp.pyramid(color=vp.color.white, pos=vp.vec(0,   0.5,0),    axis=vp.vec(0,-1, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.yellow, pos=vp.vec(0,  -0.5,0),    axis=vp.vec(0, 1, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.green,  pos=vp.vec(-0.5,0,  0),    axis=vp.vec(1, 0, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.blue,   pos=vp.vec(0.5, 0,  0),    axis=vp.vec(-1,0, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.red,    pos=vp.vec(0,   0,  0.5),  axis=vp.vec(0, 0,-1),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.orange, pos=vp.vec(0,   0, -0.5),  axis=vp.vec(0, 0, 1),  size=vp.vec(0.5,1,1))])
cube_DMF = vp.compound([vp.pyramid(color=vp.color.white, pos=vp.vec(0,   0.5,0),    axis=vp.vec(0,-1, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.yellow, pos=vp.vec(0,  -0.5,0),    axis=vp.vec(0, 1, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.green,  pos=vp.vec(-0.5,0,  0),    axis=vp.vec(1, 0, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.blue,   pos=vp.vec(0.5, 0,  0),    axis=vp.vec(-1,0, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.red,    pos=vp.vec(0,   0,  0.5),  axis=vp.vec(0, 0,-1),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.orange, pos=vp.vec(0,   0, -0.5),  axis=vp.vec(0, 0, 1),  size=vp.vec(0.5,1,1))])
cube_DRF = vp.compound([vp.pyramid(color=vp.color.white, pos=vp.vec(0,   0.5,0),    axis=vp.vec(0,-1, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.yellow, pos=vp.vec(0,  -0.5,0),    axis=vp.vec(0, 1, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.green,  pos=vp.vec(-0.5,0,  0),    axis=vp.vec(1, 0, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.blue,   pos=vp.vec(0.5, 0,  0),    axis=vp.vec(-1,0, 0),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.red,    pos=vp.vec(0,   0,  0.5),  axis=vp.vec(0, 0,-1),  size=vp.vec(0.5,1,1)),
                        vp.pyramid(color=vp.color.orange, pos=vp.vec(0,   0, -0.5),  axis=vp.vec(0, 0, 1),  size=vp.vec(0.5,1,1))])
'''

# Create 3 layers of faces for each 6 side, 1 colour then 2 black, figure out how to properly assign these to the right piece

# Colours for the 3 layers of each set of pyramids
colours = [x + [vp.color.black, vp.color.black] for x in [[vp.color.white], [vp.color.yellow], [vp.color.blue], [vp.color.green], [vp.color.red], [vp.color.orange]]]
# Axis of each pyramid making up each piece
axis = [[0, -1, 0], [0, 1, 0], [-1, 0, 0], [1, 0, 0], [0, 0, -1], [0, 0, 1]]
# Position of each pyramid, relative to centre of piece
position_vectors = [[0, 0.5, 0], [0, -0.5, 0], [0.5, 0, 0], [-0.5, 0, 0], [0, 0, 0.5], [0, 0, -0.5]]

face_vector = [[[], [], []],
               [[], [], []],
               [[], [], []]]


layer_vector = []

pieces = [3 * [3 * [3 * []]]]
faces = [6 * [3 * [3 * []]]]



# Layers of the cube, top to bottom
for l in range(3):
    # Faces of the cube
    face = []
    for fy, fx, in iter.product(range(3), range(3)):
        # Sides of each piece of the cube
        piece = []
        for s in range(6):
            piece.append(vp.pyramid(color=colours[s][l], pos=vp.vec(position_vectors[l]) + vp.vec(face_vector[fy][fx]) + vp.vec(layer_vector[l]), axis=vp.vec(axis[s], size=vp.vec(0.5, 1, 1))))

        # Binds each face of each piece together
        pieces[0] = vp.compound(piece)

    # Binds each piece of each face together
    faces[0] = ""


cube = vp.compound([cube_ULB, cube_UMB, cube_URB, cube_ULM, cube_UMM, cube_URM, cube_ULF, cube_UMF, cube_URF])


rotations = [[-1,0,0], [1,0,0], [0,-1,0], [0,1,0], [0,0,1], [0,0,-1], [0,0,0]]

while True:
    keys = -1
    if kb.is_pressed("w"):
        keys = 0
    elif kb.is_pressed("s"):
        keys = 1
    elif kb.is_pressed("a"):
        keys = 2
    elif kb.is_pressed("d"):
        keys = 3
    elif kb.is_pressed("q"):
        keys = 4
    elif kb.is_pressed("e"):
        keys = 5

    cube.rotate(angle=vp.radians(1.5), axis=vp.vec(rotations[keys][0], rotations[keys][1], rotations[keys][2]), origin=vp.vec(0,0,0))

    time.sleep(0.02)

    