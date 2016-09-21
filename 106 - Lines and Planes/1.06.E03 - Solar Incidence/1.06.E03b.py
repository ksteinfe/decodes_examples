'''
1.06.E03b

required:

result:

'''

"""
Mesh Coloring by AOI of a Single Vector
Given a single-face Mesh and a single vector, the function defined here calculates the angle of incidence, constructs a Color as the interpolation of two given colors (rad and blue), and assigns the Color to the Mesh.
"""

def color_by_angle(tar_msh,src_vec):
    # a Plane through the Points of the first (and only) face
    pln = Plane.from_pts(tar_msh.face_pts(0))
    ang = aoi(pln,src_vec)**2
    clr = Color.interpolate( blue, red, ang )
    if ang == 0: clr = black
    
    tar_msh.set_color(clr)
    return clr

for m in mshs:
    color_by_angle(m,sun_vec)
    
    
"""
Mesh Coloring by AOI of Weighted Vectors
Given a single-face Mesh and a collection of suns, the function defined here calculates the amount of radiation that strikes the given mesh face by summing solar radiation and accounting for angle of incidence. The face is then colored according to a given scale interval (sum_ival). If the amount of radiation is zero, black is assigned.
"""
sun_a = (vec_a, 10.0)
sun_b = (vec_b, 8.0)

def color_by_angle(tar_msh,suns):
    pln = Plane.from_pts(tar_msh.face_pts(0))
    # {a} the weighted sum of solar radiation, accounting for AOI
    val = sum( [sun[1]*aoi(pln,sun[0])**2 for sun in suns] )
    clr = Color.interpolate( blue, red, sum_ival.deval(val) )
    if val == 0: clr = black
    tar_msh.set_color(clr)
    return clr

for m in mshs:
    color_by_angle(m,[sun_a,sun_b])