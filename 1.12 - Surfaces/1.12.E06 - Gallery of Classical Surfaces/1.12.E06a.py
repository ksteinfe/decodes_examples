'''
1.12.E06a
Gallery of Translational Surfaces

required:
generator (Curve) - generator curve
directrix (Curve) - directrix curve
origin (Point) - point of intersection for two curves

result:

from decodes.extensions.classical_surfaces import TranslationalSurface
surface defined by TranslationalSurface(generator, directrix, origin)

'''

"""
Parabolic Sine Surface
"""
def func_gen(t):
    return Point( t, 0, sin(t) )

def func_dir(t):
    return Point( 0, 2*t, -t*t )
    
generator = Curve( func_gen, Interval(0,4.5*pi) )
directrix = Curve( func_dir, Interval(-2,2) )
srf = TranslationalSurface( generator, directrix, Point() )

"""
Skew Cosine Surface
Constructs a hat-like Surface given parameters for the height hei, length len, and skew amount skw.
"""
def func_gen(t):
    xf_rot = Xform.rotation( angle = skw*pi/4 )
    return xf_rot*Point(t, 0, (hei/2)*(1-cos(2*pi*t/len)))

def func_dir(t):
    xf_rot = Xform.rotation( angle = -skw*pi/4 )
    return xf_rot*Point(0, t, (hei/2)*(1-cos(2*pi*t/len)))

generator = Curve( func_gen, Interval(0, len) )
directrix = Curve( func_dir, Interval(0, len) )
srf = TranslationalSurface( generator, directrix, Point() )

"""
Elliptic Paraboloid
Constructs a Surface given parameters for the length len, width wid, and height hei.
"""
def func_gen(t):
    return Point( len*t, 0, hei*t*t )

def func_dir(t):
    return Point( 0, wid*t, hei*t*t )

generator = Curve( func_gen, Interval(-1,1) )
directrix = Curve( func_dir, Interval(-1,1) ) 
srf = TranslationalSurface( generator, directrix, Point() )

"""
Hyperbolic Paraboloid
Constructs a Surface given parameters for the length len, width wid, and height hei. Although the parameterization and the boundary conditions differ, this surface is identical to that constructed as a ruled surface by connecting two Segments.
"""
def func_gen(t):
    return Point( len*t, 0, hei*t*t )

def func_dir(t):
    return Point( 0, wid*t, -hei*t*t )
   
generator = Curve( func_gen, Interval(-1,1) )
directrix = Curve( func_dir, Interval(-1,1) )    
srf = TranslationalSurface( generator, directrix, Point() )
