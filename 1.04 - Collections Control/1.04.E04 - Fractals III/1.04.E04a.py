'''
1.04.E04a
Fractals III

required:


result:


'''

"""
Koch Snowflakes
A Segment substitution rule is again defined by defining division parameter values, this time in the service of Koch Snowflake fractal. wherein a given Segment is replaced with three smaller Segments. Rather than limiting the action of this recursive routine by number of iterations, we stop dividing Segments when they fall below a given length threshold.
"""

# parameters to plot subdivisions along a given Segment
prm = [(0,0),(0.33,0.0),(0.5,1.0),(0.66,0.0),(1,0)]

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
    pts = [seg.spt + (u_vec*u) + (v_vec*v) for u,v in prm]
    long_segs.extend([Segment(pa,pb) for pa,pb in zip(pts[:-1],pts[1:])])
        


"""
SUPERSEDED
[noprint]
"""
# a list of segments to divide
long_segs = [seed_seg]
# a list of segments that have already been divided
short_segs = []

while len(long_segs) > 0:
    # remove a segment from the front of the list
    seg = long_segs.pop(0)
    # if this segment is too short: don't divide, set aside
    if seg.length <= min_length: 
        short_segs.append(seg)
    # if the segment is too long: divide it
    else:
        # calculate vector to displace new segments
        height = seg.length*height_ratio
        d_vec = seg.vec.cross(UZ).normalized(height)
        
        # construct end points for the new segments
        s_vecs = [Vec(), seg.vec/3, seg.vec/2 + d_vec, seg.vec*2/3, seg.vec]
        # a list comprehension statement
        pts = [seg.spt+vec for vec in vecs]
        
        # zip together two modified copies of end point list
        for pa,pb in zip(pts[:-1],pts[1:]):
            long_segs.append(Segment(pa,pb))