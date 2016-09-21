'''
1.12.E01a
Gallery of Mathematical Surfaces

required:
func (function) - surface parametrization function taking u,v parameters
ival_u (Interval) - domain interval in u parameter
ival_v (Interval) - domain interval in v parameter

result:
surface defined by Surf(func, ival_u, ival_v)

'''

"""
Graph 
Product of lines
[noprint]
"""
ival_u, ival_v = Interval(a,b), Interval(c,d)    
def func(u,v):
    x = u, y = v
    z = (u - a)*(u - b)*(v - c)*(v - d)
    return Point(x,y,z)


""" 
Cylinder
[noprint]
"""
ival_u, ival_v = Interval.twopi(), Interval(0,h)    
def func(u,v):
    r = const, theta = u, z = v
    return CS().eval_cyl(r,theta,z)

    


"""
Spherical Patches
[noprint]
"""
ival_u, ival_v = Interval(theta_0, theta_1), Interval(phi_0,phi_1)    
def func(u,v):
    rho = const, phi = v, theta = u
    return CS().eval_sph(rho,phi,theta)



"""
Cone 
"""
ival_u, ival_v = Interval.twopi(), Interval(0,len)
def func(u,v):
    return CS().eval_sph(v, const, u)


    
"""
Helicoid
Constructs a helix-like Surface given parameters r1, r2 that define the inner and outer radii, n that defines the number of turns, and b that relates to the overall height.
"""
ival_u, ival_v = Interval(0, 2*pi*n), Interval(r1,r2)
def func(u,v):
    return CS().eval_cyl( v, u, b*u )
    
    
"""
Catenoid
Constructs an hourglass-like Surface given parameters h that defines the height, and c that defines the curvature and horizontal extents. 
"""
ival_u, ival_v = Interval.twopi(), Interval(-h/2,h/2)   
def func(u,v):
    return CS().eval_cyl( cosh(v/c), u, v )


 
"""
Torus
Constructs an doughnut-like Surface given parameters r1 (shown as R in equation) that defines the primary radius and r2 (shown as r) that defines the secondary radius.
"""
ival_u, ival_v = Interval(theta0,theta1), Interval.twopi()
def func(u,v):
    x = (r1 + r2*cos(v))*cos(u)
    y = (r1 + r2*cos(v))*sin(u)
    z = r2*sin(v)
    return Point(x,y,z)


"""
Superellipsoid
Constructs a pillow-like Surface given parameters dim_x, dim_y, and dim_z that describe the dimensions of the bounding box, and parameters m and n that describe the 'puffiness' of the resulting form.
"""
ival_u, ival_v = Interval.twopi(), Interval(0, pi)

def sgn_pow(x, alpha):
    if x == 0: return 0
    return abs(x)**alpha * (x/abs(x))
    
def func(u,v):
    x = sgn_pow(sin(v),m) * sgn_pow(cos(u),n)
    y = sgn_pow(sin(v),m) * sgn_pow(sin(u),n)
    z = sgn_pow(cos(v),m)
    return Point(dim_x * x, dim_y * y, dim_z * z)
    

