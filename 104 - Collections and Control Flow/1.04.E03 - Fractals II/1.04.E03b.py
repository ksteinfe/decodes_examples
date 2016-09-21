'''
1.04.E03b
Fractals II

required:
segs ([Segment]) A list of Segments to divide

result:

http://ecademy.agnesscott.edu/~lriddle/ifs/ksnow/flowsnake.htm
'''

"""
True Parameter Values
Given here are the parameter values calculated to five decimal places
[noprint]
"""

prm = [\
    (0,0),\
    (0.07143,0.37115),\
    (0.42857,0.49487),\
    (0.78571,0.61859),\
    (0.71428,0.24743),\
    (0.35714,0.12372),\
    (0.64286,-0.12372),\
    (1,0)\
    ]

"""
Peano-Gosper Curves
A Segment substitution rule is defined in the production of a Gosper Curve fractal, wherein a given Segment is replaced with seven smaller Segments. The direction of this non-symmetrical replacement is critical, as the resulting pattern will overlap if not orchestrated properly. 
"""
# parameters to plot subdivisions along a given Segment
prm = [\
    (0,0),(0.07,0.31),(0.48,0.47),(0.78,0.69),\
    (0.71,0.23),(0.34,0.12),(0.66,-0.12),(1,0)\
    ]
#{d} flags that indicate the direction of resulting Segments
flips = [True, False, False, False, True, True, False]

for n in range(count):
    new_segs = []
    for seg in segs:
        u_vec = seg.vec
        v_vec = u_vec.cross(UZ)
        
        # to house the end Points of new Segments
        pts = []
        #{e} unpack and iterate over parameter Tuples
        for u,v in prm:
            pt = seg.spt + (u_vec * u) + (v_vec * v)
            pts.append(pt)
            
        
        #{f} zip up point pairs with flip parameters & iterate
        for pa,pb,flip in zip(pts[:-1],pts[1:],flips): 
            if flip: new_segs.append(Segment(pb,pa))
            else: new_segs.append(Segment(pa,pb))
        
    segs = new_segs