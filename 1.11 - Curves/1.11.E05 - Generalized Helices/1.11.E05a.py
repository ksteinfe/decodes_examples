'''
1.11.E05a
Generalized Helix.

required:
TODO

result:
TODO

'''

"""
A Simple Helix
"""
def func(t):
    theta = turns * two_pi * t/height
    return CS().eval_cyl(rad, theta,t)

ival = Interval(0,height)
crv = Curve(func,ival)

"""
Linear Profile Helix
"""

def func(t):
    rad = Interval(rad_bot,rad_top).eval(t/height)
    theta = turns * two_pi * t/height
    return CS().eval_cyl(rad, theta, t)

ival = Interval(0,height)
crv = Curve(func,ival)

   
"""
Sinusoidal Profile Helix
"""
rad_min = 2.0
rad_mult = 2.0
humps = 3.0
def func(t):
    rad = rad_min + rad_mult * ( sin(pi*t*humps) + 1 )
    theta = turns * two_pi * t**k
    return CS().eval_cyl(rad, theta, t*height)

ival = Interval()
crv = Curve(func,ival)
    
"""
Bezier Profile Helix
A helical Curve with a profile that approximates a Bezier Curve through three given Points 
"""
def calc_radius_at(t):
    pt_a = Point(rad_cap,0)
    pt_b = Point(rad_mid,mid_height*height)
    pt_c = Point(rad_cap,height)
    return Curve.bezier([pt_a,pt_b,pt_c]).eval(t).x

def func(t):
    rad = calc_radius_at(t)
    theta = turns * two_pi * t**k
    return CS().eval_cyl(rad, theta, t*height)
    
    
"""
Bespoke Helix
"""

def func(t):
    if t < 0.5:
        tt = t*2
        rad = Interval(rad_bot,rad_top).eval(tt)
        theta = turns * two_pi * tt
        z = Interval(0,height).eval(tt)
    else:
        tt = (t-0.5)*2
        rad = Interval(rad_top,rad_bot).eval(tt)
        theta = (turns * two_pi * tt) + (turns * two_pi)
        z = Interval(height,0).eval(tt)
    return CS().eval_cyl(rad,theta,z)

