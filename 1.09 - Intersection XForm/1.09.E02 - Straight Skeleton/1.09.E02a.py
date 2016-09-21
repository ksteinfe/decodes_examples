'''
1.09.E02a

required:

result:

'''

"""
PGon Angle Bisector
Calculates the bisector of one corner of a Polygon. Returns the Vec that bisects the two edges that make up the corner, and the angle between this bisector and either edge.
"""
def angle_bisector(self,index):
    v0,v1 = self.edges[index-1].vec, self.edges[index].vec
    bisec =  Vec.bisector(v0,v1).cross(UZ)
    return (bisec, bisec.angle(v1))


"""
Basic Offset Routine
Allows bisectors to cross each other, and allows polygon to become self-intersecting.
"""
def offset(pg,dist):
    # Lists of Vecs and angles for each corner
    vecs, angs = zip(*[pg.angle_bisector(i) for i in range(len(pg))])
    # calculate offset distances to maintain parallel lines
    ds = [offset_dist/math.sin(angle) for angle in angs]
    # construct offset bones
    bones = [Segment(p,p+v.normalized(d)) for v,d,p in zip(vecs,ds,pg.pts)]
    return PGon([bone.ept for bone in bones])

