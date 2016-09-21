'''
1.09.E02b

required:

result:

'''

"""
Merged Bisector Offset
Preforms a simple offset by calculating bisecting "bones" of a a given PGon offset to a given distance. Then, recursively replaces any neighboring bones that intersect with a new "merged" version of the two.
"""
def offset(pg,dist):
    # construct offset bones as before
    vecs, angs = zip(*[pg.angle_bisector(i) for i in range(len(pg))])
    ds = [offset_dist/math.sin(angle) for angle in angs]
    bones = [Segment(p,p+v.normalized(d)) for v,d,p in zip(vecs,ds,pg.pts)]
    
    # iteratively clean neighboring intersecting bones
    while True:
        # returns False when complete, a cleaned List otherwise
        still_cleaning = clean_crossed_bones(bones)
        if not still_cleaning: break
        else:  bones, dead_bone = still_cleaning[0]
    return PGon([bone.ept for bone in bones])


"""
Clean Crossed Neighboring Bones
Given a collection of Segments that describe the offset of each corner of a PGon, find the first neighboring pair that cross one another. If such a pair is found, remove the two intersecting Segments and replace with one that starts at their Point of intersection and is oriented in the average of their directions. If no such pair is found, return False.
""" 
def clean_crossed_bones(bones):
    xsec = Intersector()
    for n, pair in enumerate(match(bones,[0,-1])):
        bone, other = pair
        # if these neighboring bones intersect
        if xsec.of(bone,other):
            xpt = xsec[0]
            # recalculate vector lengths to account for intersection
            va,vb = bone.vec*(1-xsec.ta), other.vec*(1-xsec.tb)
            # construct a merged bone
            bones[n] = Segment(xsec[0],Vec.average([va,vb]))
            # remove dead bones
            bones.pop(n-1)
            # return cleaned List, and a tuple of removed bone fragments
            return bones, [Segment(bone.spt,xpt),Segment(other.spt,xpt)]
    return False
