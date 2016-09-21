'''
1.04.E03a
Fractals II

required:
segs ([Segment]) A list of Segments to divide

result:


'''

"""
Gosper Islands
A Segment substitution rule is defined in the production of a Gosper Island fractal, wherein a given Segment is replaced with three smaller Segments. These three new Segments are strung between four Points: the start and end Points of the Segment, and two new subdivision Points plotted via a manipulation of the Vec of the given Segment.
"""
#{a} parameters to plot subdivisions along a given Segment
prm = [ (0.357,0.124), (0.643,-0.124) ]

for n in range(count):
    new_segs = []
    for seg in segs:
        # displaces center Points along Segment
        u_vec = seg.vec
        # displaces center Points away from Segment
        v_vec = u_vec.cross(UZ)
        
        #{b} construct end Points of new Segments by displacement
        pts = [\
            seg.spt,\
            seg.spt + (u_vec * prm[0][0]) + (v_vec * prm[0][1]),\
            seg.spt + (u_vec * prm[1][0]) + (v_vec * prm[1][1]),\
            seg.ept\
        ]
        
        #{c} zip together two modified copies of point list
        for pa,pb in zip(pts[:-1],pts[1:]): 
            new_segs.append(Segment(pa,pb))
        
    segs = new_segs
    
    
"""
SUPERSEDED
A Segment substitution rule is defined in the production of a Gosper Island fractal, wherein a given Segment is replaced with three smaller Segments. These three new Segments are strung between four Points: the start and end Points of the Segment, and two new 'center' Points plotted via a manipulation of the Vec of the given Segment.
[noprint]
"""
# values used to plot center Points along each given Segment
height_ratio = 0.124
prm_a = 0.357
prm_b = 0.643

for n in range(count):
    new_segs = []
    for seg in segs:
        # calculate the displacement of center Points
        height = seg.length*height_ratio
        # a displacement vector
        d_vec = seg.vec.cross(UZ).normalized(height)
        
        # construct through four points
        pts = [\
            seg.spt,\
            seg.spt + (seg.vec * prm_a) + d_vec,\
            seg.spt + (seg.vec * prm_b) - d_vec,\
            seg.ept\
        ]
        
        # zip together two modified copies of point list
        for pa,pb in zip(pts[:-1],pts[1:]): 
            new_segs.append(Segment(pa,pb))
        
    segs = new_segs