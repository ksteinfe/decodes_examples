'''
1.12.E03a
Cone (Parametrized) 3 ways
Demonstrates the non-uniqueness of parametrization

required:

result:
function
'''


""" 
Cylindrical Cone
Parametrized using cylindrical coordinates
"""
ival_u, ival_v = Interval.twopi(), Interval(0,h)
def func(u,v):
    return CS().eval_cyl( v/sqrt(3), u, v )
    


"""
Spherical Cone 
Parametrized using spherical coordinates
"""
ival_u, ival_v = Interval.twopi(), Interval(0,2*h/sqrt(3))   
def func(u,v):
    return CS().eval_sph( v, pi/6, u )


"""
Construct Domain Curve
Given a height, twist amount, and an inflection Point, construct a two-dimensional Bezier Curve that lies within the rectangular domain of a cylindrical cone.
"""
ival_u, ival_v = Interval(0,pi*2*twist), Interval(0,h)
crds = [(0,0),(infl_pt.x,infl_pt.y),(1,1)]
pts = [Point(ival_u.eval(x),ival_v.eval(y)) for x,y in crds]
dom_crv = Curve.bezier(pts)


"""
Construct Curve on Cone
Given a Curve dom_crv that lies in the rectangular domain of a cylindrical cone, reconstruct this Curve such that it lies along the surface of the cone.
"""
def func_crv(t):
    dom_pt = dom_crv.eval(t)
    return CS().eval_cyl( dom_pt.y / sqrt(3), dom_pt.x, dom_pt.y )

cone_crv = Curve(func_crv)


"""
Construct Surface by Rotation
Given a Curve on the cone, construct a Surface through the evaluation of this Curve on the v, and through the rotation of this Curve on the u. The domain_u of this Surface relates to the rotation of the curve about the central axis (0-\>2pi), and the domain_v relates to the evaluation of the Curve along its length (0-\>1)
"""
def func_srf(u,v):
    xf = Xform.rotation( angle = u )
    return cone_crv.eval(v) * xf
    
ival_u, ival_v = Interval.twopi(), Interval()
srf = Surface(func_srf, ival_u, ival_v)