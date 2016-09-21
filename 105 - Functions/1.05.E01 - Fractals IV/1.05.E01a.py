'''
1.05.E01a
Fractals IV

required:


result:


'''


"""
Fractal Segment Decomposition
Given a Segment, returns some number of sub-segments that describe a fractal subdivision.
"""    
def decompose_seg(seg):
    # vecs to displace along and away from given Segment
    uv, vv = seg.vec, seg.vec.cross(UZ)
    #construct division Points by displacement and chain
    subs = Segment.chain( [seg.spt + (uv*u) + (vv*v) for u,v in prms] )
    subsegs.extend(subs)

"""
Main Loop for a Generalized Fractal of Segments
"""    
for n in range(gens):
    subsegs = []
    map(decompose_seg,segs)
    segs = subsegs
    

"""
Calculation of Perpendicular Displacement Vector
Given a Segment, the two neighboring Segments, and a u,v coordinate describing the location of a displacement Point, this function calculates the Vec associated with the displacement Point. The resulting Point will be limited to an area bounded by the bisectors of the given Segment and the two adjacent Segments.
"""
def vv( seg, neis, u, v ):
    prev_seg, next_seg = neis
    fac = seg.length/2
    va = Vec.bisector(seg.vec.inverted(),prev_seg.vec).normalized(fac)
    vb = Vec.bisector(seg.vec,next_seg.vec.inverted()).normalized(fac)
    return Vec.interpolate(va,vb,u)*v

"""
Bounded Fractal Segment Decomposition
Given a Segment and the two neighboring Segments, returns some number of sub-segments that describe a fractal subdivision that is bounded to the bisectors of the given Segment and the two adjacent Segments.
"""
def decompose_seg( seg, neis ):
    # vecs to displace along and away from given Segment
    uv = seg.vec
    #construct division Points by displacement and chain
    subs = Segment.chain([seg.spt+(uv*u)+vv(seg,neis,u,v) for u,v in prms])
    subsegs.extend(subs)

"""
Main Loop for a Bisector-Bound Fractal of Segments 
"""
subsegs = []
for n in range(gens):
    subsegs = []
    segs_prev = [segs[-1]] + segs[:-1]
    segs_next = segs[1:] + [segs[0]]
    map( decompose_seg, segs, segs_prev, segs_next )
    segs = subsegs

    
"""
Gosper Islands
A Segment substitution rule is defined in the production of a Gosper Island fractal, wherein a given Segment is replaced with three smaller Segments. These three new Segments are strung between four Points: the start and end Points of the Segment, and two new subdivision Points plotted via a manipulation of the Vec of the given Segment.
[noprint]
"""
#{a} parameters to plot subdivisions along a given Segment
prms = [ (0.357,0.124), (0.643,-0.124) ]

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
            seg.spt + (u_vec * prms[0][0]) + (v_vec * prms[0][1]),\
            seg.spt + (u_vec * prms[1][0]) + (v_vec * prms[1][1]),\
            seg.ept\
        ]
        
        #{c} zip together two modified copies of point list
        for pa,pb in zip(pts[:-1],pts[1:]): 
            new_segs.append(Segment(pa,pb))
        
    segs = new_segs
    

"""
Koch Snowflakes
A Segment substitution rule is again defined by defining division parameter values, this time in the service of Koch Snowflake fractal. wherein a given Segment is replaced with three smaller Segments. Rather than limiting the action of this recursive routine by number of iterations, we stop dividing Segments when they fall below a given length threshold.
[noprint]
"""

# parameters to plot subdivisions along a given Segment
prms = [(0,0),(0.33,0.0),(0.5,1.0),(0.66,0.0),(1,0)]

# a list of segments to divide
long_segs = [seed_seg]
# a list of segments that have already been divided
short_segs = []

while len(long_segs) > 0:
    # remove a segment from the front of the list
    seg = long_segs.pop(0)
    #{a} if this segment is too short, set it aside
    if seg.length <= min_length:
        short_segs.append(seg)
        continue
        
    #{b} if it is not too short, construct replacement Segments
    u_vec = seg.vec
    v_vec = u_vec.cross(UZ).normalized(seg.length*height_ratio)
    pts = [seg.spt + (u_vec*u) + (v_vec*v) for u,v in prms]
    long_segs.extend([Segment(pa,pb) for pa,pb in zip(pts[:-1],pts[1:])])
        
        


"""
SUPERSEDED
Koch Snowflakes and Gosper Islands can be implemented as two configurations of a single routine.
[noprint]
"""
divs = ( 0 , 1/3 , 0.5 , 2/3 , 1 )
height_ratio = 1/3

for step in range(steps):
    new_lines = []
    for line in seed_lines:
        height = line.length*height_ratio
        pts = [line.eval(t) for t in divs]
        vec = line.vec.cross(Vec(0,0,1)).normalized(height)
        pts[2] += vec
        new_lines.extend([Segment(pts[n],pts[n+1]) for n in range(len(pts)-1)])
    seed_lines = new_lines