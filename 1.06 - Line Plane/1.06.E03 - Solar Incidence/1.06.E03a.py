'''
1.06.E03a

required:

result:

'''

"""
Angle of Incidence Between Ray and Plane
This function does not return the actual angle, but rather the cosine of the angle of incidence between a given plane and vector. If the vector is "behind" the plane, a value of 0.0 is returned, thereby constraining the result to a range of [0-\>1]
"""
def aoi(pln,vec):
    return max(0, vec.dot(pln.normal))

"""
Color by Angle of Incidence
A given Plane is assigned a color by its angle of incidence to a given Vec. Planes oriented perpendicular to the Vec are red, those parallel to it are blue, and those in-between are colored by interpolation. Planes facing away from the Vec are assigned black.
"""

def color_by_angle(tar_plane,src_vec):
    ang = aoi(tar_plane,src_vec)**2
    clr = Color.interpolate( blue, red, ang )
    if ang == 0: clr = black
    tar_plane.set_color(clr)
    return clr
    
color_by_angle(pln,sun_vec)

