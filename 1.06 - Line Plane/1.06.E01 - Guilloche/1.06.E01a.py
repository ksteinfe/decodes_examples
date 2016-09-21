'''
1.06.E01a
Creates a wavy chain bound between two line segments. The chain is made up of connected line segments.

required:
seg_a (Segment) line segment representing a boundary for the chain
seb_b (Segment) line segment representing the other boundary for the chain
hump_cnt (int) number of complete waves
t (float) determines the offset of the initial wave

result:
chain ([Segment]) connected line segments 

'''

"""
A Single Guilloche Chain
A Guilloche chain is constructed between two given line segments. The normalized shift argument allows for slightly different sine waves to be described.
"""
def guilloche_chain(seg_a, seg_b, shift):
    pts = []
    #shift is mapped to a range related to the sine frequency
    off = (two_pi / hump_cnt) * shift
    # u [0-\> 1] and t [0-\>2pi] are simultaneously iterated
    for u,t in zip(Interval()/res, Interval.twopi()/res):
        pt_a, pt_b = seg_a.eval(u), seg_b.eval(u)
        #v is calculated as a function of sine[-1-\> 1]
        v = math.sin((t+off)*hump_cnt)
        #normalizing v to a range[0-\> 1], a Point is plotted
        pts.append(Segment(pt_a, pt_b).eval(0.5 + v/2))
    #{a} using zip and slicing, a chain of Segments is constructed
    return [Segment(pa,pb) for pa,pb in zip(pts[:-1],pts[1:])]

"""
Guilloche of Chains
Here, we construct a series of Guilloche chains, each describing a slightly different sine curve, by iterating over a collection of values for the the shift argument
"""
shfts = [n/chain_count for n in range(chain_count)]
guilloche  = [guilloche_chain(seg_top, seg_btm, shft) for shft in shfts]    
               

"""
A Periodic Guilloche Chain
For chains that are able to join seamless at their open ends to form a closed curve, a modification of the construction of the for-loop is required
"""
def periodic_guilloche_chain(seg_a, seg_b, shift):
    pts = []
    off = (two_pi / hump_cnt) * shift
    uu = Interval().divide(res,True)
    vv = Interval.twopi().divide(res,True)
    for u,t in zip(uu,vv):
        pt_a, pt_b = seg_a.eval(u), seg_b.eval(u)
        v = math.sin((t+off)*hump_cnt)
        pts.append(Segment(pt_a, pt_b).eval(0.5 + v/2))
    return [Segment(pa,pb) for pa,pb in zip(pts[:-1],pts[1:])]