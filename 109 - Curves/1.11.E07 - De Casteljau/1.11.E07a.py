'''
1.11.E07a
Constructs a Bezier curve using the geometric approach of the deCasteljau algorithm.

required:
cpts ([Point]) control points

result:
func (function)  constructs a curve point for a given parameter t
bezier (function) constructs a bezier curve for given control points
'''

"""
deCasteljau Algorithm
Constructs a curve point for a given parameter t
"""
def func(t):
    pts = cpts
    while len(pts) > 1:
        pts = [Segment(pts[n],pts[n+1]).eval(t) for n in range(len(pts)-1)]
    return pts[0]


"""
deCasteljau Algorithm
Equivalent construction using the Point interpolation method
[noprint]
"""
def func(t):
    pts = cpts
    while len(pts) > 1:
        pts = [Point.interpolate(pts[n],pts[n+1],t) for n in range(len(pts)-1)]
    return pts[0]

"""
Bezier Curve
Constructs a curve for a given set of control point
"""
def bezier(cpts):
    def func(t):
        while len(pts) > 1:
            pts = [Segment(pts[n],pts[n+1]).eval(t) for n in range(len(pts)-1)]
        return pts[0]    
    return Curve(func)
