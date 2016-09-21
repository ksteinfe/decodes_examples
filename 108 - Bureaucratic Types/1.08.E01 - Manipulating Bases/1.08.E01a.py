'''
1.08.E01a
Create a Polyline from a golden spiral

required: 
todo

result: 
todo

'''

"""
[noprint]
"""
PHI = 0.69126979252
def fib_pt(theta):
    r = PHI**theta
    return CS().eval_cyl(r,theta)

"""
Constructs a 3d Golden Spiral (a Golden Helix, perhaps?) as a polyline.
[noprint]
"""
pl_ccw = PLine()
ival_theta = Interval(0,math.pi*2*turns)
for theta in ival_theta.divide(segs_per_turn,True):
    pt = fib_pt(theta) * radius
    pt.z = height * ival_theta.deval(theta)**falloff
    pl_ccw.append(pt)
    

"""
Constructs a new Polyline by mirroring the existing one about the world xz plane, and joining the result.
"""
xf = Xform.mirror("world_xz")
pl_cw = PLine([p*xf for p in pl_ccw.pts])
pl_join = pl_cw.join(pl_ccw)
