'''
1.12.E05a
Single smooth bump on a rectangle

required:
h (float) - height of bump


result:
ival_u (Interval) - domain in u
ival_v (Interval) - domain in v
func (function) - surface parametrization function

'''


"""
Graph Displacement
A Surface of displacement is described as a cosine graph on the z-y plane.
"""
bnds = Bounds(ival_x = Interval(a,b), ival_y = Interval(c,d))

def func(u,v):
    upi = Interval.remap(u, bnds.ival_x, Interval.twopi())
    vpi = Interval.remap(v, bnds.ival_y, Interval.twopi())
    z = h*(1-cos(upi))*(1-cos(vpi))
    return Point(u,v,z)

srf = Surface(func, bnds.ival_x, bnds.ival_y)

    
