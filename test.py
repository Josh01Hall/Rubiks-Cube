import vpython as vp, keyboard as kb, time

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

    