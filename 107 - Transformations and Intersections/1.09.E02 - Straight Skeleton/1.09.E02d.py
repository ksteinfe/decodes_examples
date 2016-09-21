'''
1.09.E02d
Does not work. 

required:

result:

'''



"""
Offset Routine Handling Edge and Split Events
Additionally handles split events which result in polygons split upon shrinking
[noprint]
"""
def offset(self,offset_dist,flip=False):
    vecs, angles = zip(*[self.angle_bisector(i) for i in range(len(self))])
    off_dists = [offset_dist/math.sin(angle) for angle in angles]
    if flip: off_dists = [-d for d in off_dists]
    
    bones = [Segment(p, p + v.normalized(d)) for v,d,p in zip(vecs,off_dists,self.pts) ]
    dead_bones = []
    while True:
        still_cleaning = clean_crossed_bisectors(bones,offset_dist)
        if not still_cleaning: break
        else: 
            bones = still_cleaning[0]
            dead_bones.extend(still_cleaning[1])
    pgons = [PGon([bone.ept for bone in bones])]
    clean_pgons = []
    while pgons:
        split_result = split_pgon(pgons.pop(0))
        if len(split_result) > 1: pgons.extend(split_result)
        else: clean_pgons.extend(split_result)
        
    # any pgons crossed by a bone is inside-out, and should be removed
    clean_pgons = [pg for pg in clean_pgons if is_boneless(pg,bones)]
    
    return clean_pgons

"""
Is Boneless
Checks which polygons are not crossed by a bone
[noprint]
"""
def is_boneless(pg,bones):
    return all( [bone.eval(0.99) not in pg for bone in bones] )

"""
Split Polygon
[noprint]
"""    
def split_pgon(pg):
    xsec = Intersector()
    for n,edge in enumerate(pg.edges):
        for other in pg.edges[n+2:]:
            if xsec.of(edge,other):
                if xsec[0] == edge.spt: continue
                idx = pg.edges.index(other)
                print "XSEC:", n, idx
                clean_pts = list(pg.pts[:n+1]) + [xsec[0]] + list(pg.pts[idx+1:])
                dirty_pts = [xsec[0]] + [p for p in pg.pts if p not in clean_pts]
                return [PGon(clean_pts),PGon(dirty_pts)]                
    return [pg]

