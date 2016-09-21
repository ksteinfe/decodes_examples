'''
1.12.E06b
Gallery of Ruled Surfaces

required:

for construction type I (construction by specifying a base curve and director curve)
base_crv (Curve) - base curve along which the lines move
director_crv(Curve) - director curve indicating directions of the line
ival_v (Interval) - controls the length of rulings

for construction type II (construction by connecting points on two curve)
crv_a (Curve) 
crv_b (Curve)

result:
see 3.09.E00e for usage

'''

"""
Conoid
Given a desired height hei, width wid, and integer number of turns trns, a Conoid Surface is defined with a base Curve of a vertical line Segment, a director Curve of a unit circle.
"""
crv_base = Segment(Point(), Point(0, 0, hei)) 
crv_dirc = Curve.circle( ival = Interval(0, trns*two_pi) )

def func(u,v):
    return crv_base.eval(u) + crv_dirc.eval(u)*v
    
surf = Surface( func, Interval(), Interval(0,wid) ) 


"""
Mobius Band
Given a base radius rad, and a width wid, a Mobius Band is constructed with a base Curve of a circle and a director Curve that resembles a spherical bow-tie. 
"""

def func_dirc(t):
    return Point( cos(t/2)*cos(t), cos(t/2)*sin(t), sin(t/2) )

crv_base = Curve.circle(rad = rad)
crv_dirc = Curve(func_dirc, Interval.twopi())

def func(u,v):
    return crv_base.eval(u) + crv_dirc.eval(u)*v
    
surf = Surface( func, Interval(), Interval(-v1,v1) ) 



"""
Torqued Ellipse
Constructs a ruled surface between two perpendicular-facing ellipses given parameters for the length len, width wid, and height hei of each. Note that the center of ellipse B is shifted. Inspired by the Richard Serra sculpture series with same name.
"""

def func_a(t):
    return Point( len*cos(t), wid*sin(t) )

def func_b(t):
    return Point( wid*cos(t)-0.5, len*sin(t), hei )
    
crv_a = Curve(func_a, Interval(0, 1.9*pi))
crv_b = Curve(func_b, Interval(.1*pi, 2*pi))


def func(u,v):
    return Segment( crv_a.eval(u), crv_b.eval(u) ).eval(v)

surf = Surface(func)
    
"""
Hyperbolic Paraboloid
Demonstrates the construction of a hyperbolic paraboloid as a ruled surface by connecting points on two line Segments. Although the parameterization and the boundary conditions differ, this surface is identical to that constructed via translation.
"""
crv_a = Segment(Point(len, 0, hei), Point(0, wid, -hei))
crv_b = Segment(Point(0, -wid, -hei), Point(-len, 0, hei))

def func(u,v):
    return Segment( crv_a.eval(u), crv_b.eval(u) ).eval(v)

surf = Surface(func)



"""
Tangent Surface of a Helix
[noprint]
"""

rad_min = 0.2
rad_mult = 2.0
humps = 1.75

#sinusoidal profile helix
def func_b(t):
    rad = rad_min + rad_mult * ( sin(pi*t*humps) + 1 )
    theta = turns * two_pi * t**k
    return CS().eval_cyl(rad, theta, t*height)
base_crv = Curve(func_b,Interval())

#curve tangent, calculated analytically
def func_d(t):
    rad = rad_min + rad_mult * ( sin(pi*t*humps) + 1 )
    theta = turns * two_pi * t**k
    #derivative of rad with respect to t
    d_rad = rad_mult*pi*humps*cos(pi*t*humps)
    #derivative of theta with respect to t
    d_theta = 2*pi*k*(t**(k-1))
    d_x = d_rad*cos(theta)- rad*d_theta*sin(theta)
    d_y = d_rad*sin(theta)+ rad*d_theta*cos(theta)
    d_z = height
    return Point(d_x, d_y, d_z)
director_crv = Curve(func_d, Interval())

ival_v = Interval(0, v1)
