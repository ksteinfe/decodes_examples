'''
1.05.E04a
Subdivsion

required:


result:


'''

"""
Sort By Angle
"""
def sort_by_angle(origin,*args):
    spts = sorted(args,key=lambda pt: UX.angle(Vec(origin,pt)))
    return origin, spts

"""
Determine Convexity
"""    
def tip_is_ccw_concave(pts):
    pa, pb, pc = pts[-3],pts[-2],pts[-1]
    return Vec(pa,pb).cross(Vec(pb,pc)).z < 0    

    
"""
Convex Hull by Graham Scan
Given a set of two-dimensional Points, 
"""    
# sort points by their y-coordinate
pts = sorted(pts,key=lambda pt: pt.y)
# slice off first point, and sort by angle
opt, pts = sort_by_angle(*pts)

# initialize collection of convex Points
cvx_pts = [opt,pts[0],pts[1]]
for pt in pts[2:]:
    # append a new Point to convex collection
    cvx_pts.append(pt)
    # check if new segment produces concavity 
    while tip_is_ccw_concave(cvx_pts):
        # if so, remove second-to-last Point
        cvx_pts.pop(-2)