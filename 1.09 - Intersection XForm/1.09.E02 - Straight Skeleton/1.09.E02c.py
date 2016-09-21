'''
1.09.E02c
Routine for a "straight-skeleton" offset which can handle "edge" and "split" events. Terminology from Aichholzer (1995) A novel type of skeleton for polygons. 

required:

result:

'''

"""
Straight Skeleton Main Loop
Given the collection of Rays rays that represents the bisectors of each corner of a PGon, and the collection of PGon edges edges, at each cycle of the main loop of our straight-skeleton routine, a pair of rays and the edge shared by them are identified for "reduction", whereby they are replaced with a single ray that lies at their intersection. Once the given collection has been reduced to just two rays, we may connect these with a Segment and terminate the loop.
"""
xsec = Intersector()
nice_bones = []
while True:
    if len(rays) <= 2:
        nice_bones.append( Segment(rays[0].spt,rays[1].spt) )
        break
    
"""
Neighborhood Intersections
Each Ray finds the parameters of its intersection with neighbors. This information is stored as a List of Dicts that each describe the t-value intersection parameter of the 'prev' and 'next' Rays.
"""    
    xsec_prms = []
    for ry_this, ry_prev, ry_next in match(rays,[0,-1,1]):
        t_prev, t_next = False, False
        if xsec.of(ry_this, ry_prev): t_prev = xsec.ta
        if xsec.of(ry_this, ry_next): t_next = xsec.ta
        xsec_prms.append({'prev':t_prev,'next':t_next})


"""
Identification of Reducible Pairs
Not every neighboring pair of Rays may be reduced. To be a candidate for reduction, two Rays must intersect each other before they intersect their other neighbor. Below, each pair of Rays is interrogated, and if found to be a candidate for reduction, the pair is recorded in a sortable Tuple of the sum of the the distance to the Point of intersection and a Dict that stores required information about the Rays.
"""
    reducables = []
    for n, pair in enumerate(match(xsec_prms,[0,-1])):
        this, prev = pair
        # if this ray does not intersect the previous, continue
        if not this['prev']: continue
        # if this ray intersects the previous before the next
        if not this['next'] or appx_less_than(this['prev'],this['next']):
            # if the previous intersects this one before its other neighbor
            if not prev['prev'] or appx_less_than(prev['next'], prev['prev']):
                # this is an appropriate ray to reduce. log it.
                rank = this_prms['prev'] + prev_prms['next']
                reducables.append( (rank,{'param':this_prms['prev'],'idx':n}) )
            
            
"""
Ray Pair Reduction
If at least one reducible pair of Rays has been identified, here we preform the actual reduction. First, the list of possible reducibles is sorted, and the one that exhibits the smallest summed distance is selected. Next, trimmed Segments are constructed that terminate with the Point of intersection. Finally, the replacement bisecting Ray is constructed and added to the main collection of Rays at the proper index. Finally, the Rays and edge targeted for reduction are removed. If no reducible Rays have been identified, something has gone wrong.
"""
    if len(reducables)>0:
        # select the reducable with the smallest summed distance
        choice = sorted(reducables)[0][1]
        t,idx = choice['param'], choice['idx']
        
        # construct "nice bone" Segments behind the reduction
        pt = rays[idx].eval(t)
        sa,sb = Segment(rays[idx].spt,pt), Segment(rays[idx-1].spt,pt)
        nice_bones.extend([sa,sb])
        
        # find the best replacement Ray bisector
        bsecs = Vec.bisectors(edges[idx].vec, edges[idx-2].vec)
        guide = Vec.bisector(sa.vec,sb.vec)
        vec = guide.best_match(bsecs)
        
        # remove replaced Rays and edge
        edges.pop(idx-1)
        rays[idx] = Ray(pt,vec)
        rays.pop(idx-1)
    else:
        break