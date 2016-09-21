'''
1.11.E02a
A Gallery of Parametrized Curves.  There are many parametrizations that have been "discovered" already.  
These can be "plugged in" as a Decodes curve 

required:
various parameters to define the parametrization function

result:
parametrization function 
domain interval

sample usage:
tol = ival.delta/pt_count
crv = Curve(func,ival,tol)


'''


""" 
Ellipse
"""
ival = Interval.twopi()
def func(t):
    x = len_x*cos(t)
    y = len_y*sin(t)
    return Point(x,y)


"""
Spiral
"""
ival = Interval.twopi()
def func(t):
    x = rad*num_turns*t*cos(num_turns*t)
    y = rad*num_turns*t*sin(num_turns*t)
    return Point(x,y)

"""
Loop
"""
eps = 0.05
ival = Interval(-pi/3 + eps, pi/3 - eps)
def func(t):
    t_value = (1-t)*(-pi/3 +eps) + t*(pi/3 - eps)
    c = cos(t_value)
    s = sin(t_value)
    tan = tan(t_value)
    x = len_x*(1-tan*tan)*c
    y = len_y*(1-tan*tan)*s
    return Point(x,y)

"""
Teardrop
"""
ival = Interval.twopi()
def func(t):
    x = len_x*cos(t)
    y = len_y*(sin(t)*sin(0.5*t)**n)
    return Point(x,y)


"""
Diamond
"""
ival = Interval.twopi()
def func(t):
    c = cos(t)
    s = sin(t)
    x = len_x*abs(c)*c
    y = len_y*abs(s)*s
    return Point(x,y)

"""
Blob
Blob-shaped curve family with all curves of fixed radius having same area.  
"""
ival = Interval()
def func(t):
    c = cos(two_pi*t)
    s = sin(two_pi*t)
    c_theta = cos(two_pi*alpha)
    s_theta = sin(two_pi*alpha)
    fac = 1.0/sqrt(2)
    r = 30*(1 + rad*fac*c_theta*cos(4*pi*t) + rad*fac*s_theta*cos(6*pi*t))
    x = r*cos(two_pi*t)
    y = r*sin(two_pi*t)
    return Point(x,y)

"""
Hypocycloid
"""
ival = Interval()
def func(t):
    t_value = two_pi*t
    c = cos(t_value)
    s = sin(t_value)
    c_n = cos((num_cusps-1)*t_value)
    s_n = sin((num_cusps-1)*t_value)
    factor = rad/num_cusps
    x = factor*((num_cusps-1)*c - c_n)
    y = factor*((num_cusps-1)*s + s_n)
    return Point(x,y)

"""
Spherical Knot
A family of spherical knot curves
"""
ival = Interval()
def func(t):
    rho = rad_min + (rad_max - rad_min)*sin(pi*t)
    phi = pi*sin(pi*n_phi*t)
    theta = 2*pi*n_theta*t
    x = rho*sin(phi)*cos(theta)
    y = rho*sin(phi)*sin(theta)
    z = rho*cos(phi)
    return Point(x,y,z)

