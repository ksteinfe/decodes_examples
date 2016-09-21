'''
1.09.E03a
TODO

required:

result:

'''




"""
Ray-Circle Intersection
The Decod.es library does not, at the time of writing, provide a ray-circle intersection, so we implement one here that is limited to two-dimensional Circles and Segments on the xy-plane. This function returns False in the case on no intersection, or a tuple of the t-value of the intersection Point as it lies along the Ray, as well as the intersection Point itself.
"""
def ray_circle_2d_intersection(ray, circle):
    vert_pln = Plane(ray.spt,ray.vec.cross(UZ))
    xsec = Intersector()
    if not xsec.of(bound,vert_pln) or len(xsec) != 2: return False
        
    for pt in xsec:
        near = ray.near(pt)
        if near[1]>0: return ( (near[1],pt) )
    
    return False
    
"""
Limit Function
Given a circular bound, returns a Segment which represents the valid portion of a given Ray within an existing ice-ray composition (as described by a given collection of Segments). 
"""
def limit(ray, segs=[]):
    #{a} returns a tuple of the t-value and Point of intersection
    bound_xsec = ray_circle_2d_intersection(ray, bound)    
    results = [bound_xsec]
    
    # for each Segment in the composition,
    for seg in segs:
        # if an intersection with this Ray is found,
        xsec = Intersector()
        if xsec.of(ray,seg) and xsec.ta > xsec.tol:
            # record the t-value and Point of intersection
            results.append((xsec.ta, xsec[0]))
    
    # sort the intersection events, and return the valid Segment
    result = sorted(results)[0]
    return Segment(ray.spt,result[1])

    
"""
Ice Ray Lattice Routine
"""    
seed_line.gen = 0
drawn_segs = [seed_line]
brnch_segs = [seed_line]
for n in range(gens):
    loop_segs = []
    for seg in brnch_segs:
        for bdict in branches:
            pt = seg.eval(bdict["t"])
            vec = seg.vec*bdict["xf"]
            nseg = limit(Ray(pt,vec), drawn_segs )
            if nseg.length > min_length:
                nseg.gen = n+1
                loop_segs.append(nseg)
                drawn_segs.append(nseg)
    brnch_segs = loop_segs
