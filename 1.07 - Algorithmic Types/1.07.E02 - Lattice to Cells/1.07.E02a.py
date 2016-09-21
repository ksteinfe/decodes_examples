'''
1.07.E02a
Lattice to Cells

required:


result:


'''


"""
Graph Initialization
A SpatialGraph is initialized from a given set of 2d Segments. It is assumed that the Segments have been "shattered" such that all intersections occur at termination Points.
"""    
gph = SpatialGraph()
for seg in segs: gph.add_edge(seg.spt,seg.ept)


"""
Selection Function
A function that selects and returns one of a set of candidate Points as the next location in a right-hand walk. Given a collection of at least two Points that have been walked and a set of possible Points to walk next, the Point that represents the rightmost possible next step, as given by the lowest two-dimensional angle, is selected. A 180 degree return step is permitted, but is the least preferred and assigned an artificial angle of 1/EPSILON.
"""
def choose(walked_pts,suitors):
    vec_base = Vec(walked_pts[-2], walked_pts[-1])
    def angle_to(pt):
        vec_suit = Vec(walked_pts[-1],pt)
        ang = vec_base.angle(vec_suit)
        if abs(ang - math.pi) < EPSILON: return 1/EPSILON
        if vec_base.cross(vec_suit).z >=0 : return ang
        else: return -ang
    
    return sorted(suitors, key=angle_to)[0]

"""
Main Lattice to Cells Routine
Walks a given SpatialGraph in order to find all the smallest possible closed polygonal regions. Walks are initiated at each edge of the given Graph, and proceed by selecting subsequent edges that provide the rightmost turn at each node. 
"""
pgons = []
walked_edges = set()
for pair in gph.node_pairs:
    # if the initial edge has been walked, don't bother walking
    if pair in walked_edges: continue
    # initialize a collection to store Points along this walk
    wpts = list(pair)
    valid = True
    while valid:
        # select next node to walk
        choice = choose(wpts,gph.edges[wpts[-1]])
        
        # dead end: the chosen node has only one edge
        if len(gph.edges[choice]) == 1: valid = False 
        # double-back: the chosen node is present in this walk
        if choice is wpts[-2] : valid = False
        # already walked: the chosen edge has been walked
        if (wpts[-1],choice) in walked_edges: valid = False 
        # success! a closed loop has been found
        if choice is wpts[0] : break 
        
        # no success, but no failure. keep walking.
        wpts.append(choice)
        
    # if the walked Points are valid, construct a PGon and log
    if valid and len(wpts) > 2:
        pgons.append(PGon(wpts))
        for pair in match(wpts,[0,1]): walked_edges.add(pair)