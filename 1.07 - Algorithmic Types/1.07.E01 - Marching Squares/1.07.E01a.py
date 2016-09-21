'''
1.07.E01a
Marching Squares

required:


result:


'''



"""
Quartet Edge Interpolate
Plots a Point along each edge of a given quartet at a position determined by an interpolation between the values associated with the corner Points of the quartet at a given threshold. A collection of four Point or False values are returned. If the values associated with any pair of corner Points are the same, or if the values do not encompass the given threshold, a value of False is included in the returned collection.
"""
def interpolate_quartet_edges(self,x,y,t):
    vals, pts = self.quartet(x,y)
    ret = []
    # iterate over the pairs of indices that describe edges
    for a, b in [(0,1),(1,2),(2,3),(3,0)]:
        ival = Interval(vals[a], vals[b])
        # the corner values are the same
        if ival.delta == 0: ret.append(False)
        # the corner values do not encompass the given threshold
        elif t not in ival: ret.append(False)
        # plot an interpolated Point along the edge
        else: ret.append( Point.interpolate(pts[a], pts[b], ival.deval(t)) )
    return ret
    

"""
March Quartet
A single quartet of a ValueField is evaluated, and any Segments which describe the given threshold value are returned.
"""
def march(x,y,t):
    vals, pts = vg.quartet(x,y)
    pa,pb,pc,pd = vg.interpolate_quartet_edges(x,y,t)
    case = tuple([int(val > t) for val in vals])
    avg_val = sum(vals)/4.0
    
    # case 5 is ambiguous
    if case == (1,0,1,0):
        if avg_val > t: return [Segment(pb,pa), Segment(pd,pc)]
        else: return [Segment(pd,pa), Segment(pb,pc)]
    # case 10 is ambiguous
    if case == (0,1,0,1):
        if avg_val > t: return [Segment(pa,pd), Segment(pc,pb)]
        else: return [Segment(pc,pd), Segment(pa,pb)]
    
    # simple cases
    if case == (0,0,0,0) or case == (1,1,1,1): return [] # case 0 and 15
    if case == (1,0,0,0): return [Segment(pd,pa)] # case 1
    if case == (0,1,0,0): return [Segment(pa,pb)] # case 2
    if case == (1,1,0,0): return [Segment(pd,pb)] # case 3
    if case == (0,0,1,0): return [Segment(pb,pc)] # case 4
    if case == (0,1,1,0): return [Segment(pa,pc)] # case 6
    if case == (1,1,1,0): return [Segment(pd,pc)] # case 7
    if case == (0,0,0,1): return [Segment(pc,pd)] # case  8
    if case == (1,0,0,1): return [Segment(pc,pa)] # case 9
    if case == (1,1,0,1): return [Segment(pc,pb)] # case 11
    if case == (0,0,1,1): return [Segment(pb,pd)] # case 12
    if case == (1,0,1,1): return [Segment(pb,pa)] # case 13
    if case == (0,1,1,1): return [Segment(pa,pd)] # case 14
    

        
        
        
        
        
        
        
        
        
        