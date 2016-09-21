'''
1.03.E01a
todo

required:


result:

'''

"""
Determine Cross Product Direction
For each Vertex in the PGon, construct a cross product of vectors oriented toward neighbors, and store a boolean indicating its orientation.
"""
cp_points_up = []
for n in range(len(pgon)):
    ray_a, ray_b = pgon.cnr(n)
    vec_crs = ray_a.vec.cross(ray_b.vec)
    cp_points_up.append(vec_crs.z > 0)

"""
Assign Convexity to Each Vertex
Determine if most cross products are up or down, and then label any points in the minority as convex
"""    
# if most cross products point up
if sum(cp_points_up) >= len(pgon)/2 :
    # each pt is convex if cross product points down
    is_concave = [not d for d in cp_points_up]
# if most cross products point down
else:
    # each pt is convex if cross product points up
    is_concave = cp_points_up

"""
Construct List of Convex Points
"""    
concave_pts = []
for n in range(len(pgon)):
    if is_concave[n]: concave_pts.append(pgon.pts[n])