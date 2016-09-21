'''
1.05.E03a
Subdivsion

required:


result:


'''

"""
A Library of Functions
With a set of subdivision functions defined that are isomorphic (accepting common arguments and return values), we may call on them in a modular way. Here we store two sets of subdivision functions in a library which differentiates those that operate on quads from those that operate on triangles.
"""     
quad_funcs = [quadsub_corner_to_ctr, quadsub_diagonal]
tri_funcs = [trisub_corner_to_ctr, trisub_edge_to_edge, trisub_edge_to_ctr]

"""
General Subdivision by Generation
Here, the style of subdivision is determined by the generation of division, and proceeds in a repeating pattern.
"""     
def subdivide(gen):
    subfaces = []
    for fac in faces:
        # if this face is a quad
        if len(fac) == 4: subfaces.extend( quad_funcs[gen%2](fac) )
        # if this face is a tri
        if len(fac) == 3: subfaces.extend( tri_funcs[gen%3](fac) )
            
    return subfaces

for n in range(gens): faces = subdivide(n)

"""
General Subdivision by Attractor
Here, the style of subdivision applied is determined by the distance from the centroid of each face to an attractor Point. Two threshold distance values quad_dist and tri_dist control the selection of subdivision style.
"""  
def subdivide():
    subfaces = []
    while faces:
        fac = faces.pop()
        dist = face_cen(fac).dist(attr_pt)
        # if this face is a quad
        if len(fac) == 4:
            if dist > quad_dist: subfaces.extend(quadsub_corner_to_center(fac))
            else: subfaces.extend(quadsub_diagonal(fac))
            continue
        # if this face is a tri
        if len(fac) == 3:
            if dist < tri_dist: subfaces.extend(trisub_edge_to_center(fac))
            else: subfaces.extend(trisub_edge_to_edge(fac))
            continue
            
    return subfaces

for n in range(gens): faces = subdivide()

"""
Corner-to-Center Rectangular Subdivision
"""
def quadsub_corner_to_ctr(fac):
        subfaces = []
        cen = face_cen(fac)
        csubs = [Segment(seg.ept,cen) for seg in fac]
        subfaces.append( (fac[0],csubs[0],csubs[3].inverted())  )
        subfaces.append( (fac[1],csubs[1],csubs[0].inverted())  )
        subfaces.append( (fac[2],csubs[2],csubs[1].inverted())  )  
        subfaces.append( (fac[3],csubs[3],csubs[2].inverted())  )  
        return subfaces
        
"""
Edge-to-Center Triangular Subdivision
Subdivides a triangular face into three quadrilateral faces connected at the center of the given face.
"""     
def trisub_edge_to_ctr(fac):
        subfaces = []
        cen = face_cen(fac)
        # split edges at the middle
        pts, ssubs, esubs = split_edges(fac)
        msubs = [Segment(pt,cen) for pt in pts]
        
        subfaces.append( (ssubs[0],msubs[0],msubs[2].inverted(),esubs[2]) )
        subfaces.append( (ssubs[1],msubs[1],msubs[0].inverted(),esubs[0]) )
        subfaces.append( (ssubs[2],msubs[2],msubs[1].inverted(),esubs[1]) )
        return subfaces

"""
Diagonal Rectangular Subdivision
Subdivides a quadrilateral face into two triangular faces by connecting the corners that result in the shortest possible diagonal.
"""
def quadsub_diagonal(fac):
        subfaces = []
        if fac[0].spt.dist(fac[1].ept) < fac[1].spt.dist(fac[2].ept):
            subfaces.append( (fac[0],fac[1],Segment(fac[1].ept,fac[0].spt)) )
            subfaces.append( (fac[2],fac[3],Segment(fac[3].ept,fac[2].spt)) )
        else:
            subfaces.append( (fac[1],fac[2],Segment(fac[2].ept,fac[1].spt)) )
            subfaces.append( (fac[3],fac[0],Segment(fac[0].ept,fac[3].spt)) )        
        return subfaces


        
"""
Corner-to-Center Triangular Subdivision
Subdivides a triangular face into three triangular faces connected at the center of the given face.
"""
def trisub_corner_to_ctr(fac):
        subfaces = []
        cen = face_cen(fac)
        csubs = [Segment(seg.ept,cen) for seg in fac]
        subfaces.append( (fac[0],csubs[0],csubs[2].inverted())  )
        subfaces.append( (fac[1],csubs[1],csubs[0].inverted())  )
        subfaces.append( (fac[2],csubs[2],csubs[1].inverted())  )  
        return subfaces

"""
Edge-to-Edge Triangular Subdivision
Subdivides a triangular face into four triangular faces that connect the midpoint of each edge of the given face.
"""
def trisub_edge_to_edge(fac):
        subfaces = []
        # split edges at the middle
        pts, ssubs, esubs = split_edges(fac)
        msubs = [Segment(pa,pb) for pa,pb in zip(pts,pts[-1:]+pts[:-1])]
        
        subfaces.append( tuple([sub.inverted() for sub in msubs]) )
        subfaces.append( (ssubs[0],msubs[0],esubs[2]) )
        subfaces.append( (ssubs[1],msubs[1],esubs[0]) )
        subfaces.append( (ssubs[2],msubs[2],esubs[1]) )
        return subfaces
        
"""
Face Center
Returns the center of a given face
"""
def face_cen(fac):
    return Point.centroid([seg.ept for seg in fac])
    
"""
Split Face Edges
Returns the division Points, starting starting sub-segments and ending sub-segments that result from division of each given edge at a given t-value.
"""
def split_edges(fac, tval=0.5):
    pts = [seg.eval(tval) for seg in fac]
    ssubs = [Segment(seg.spt,pt) for seg,pt in zip(fac,pts)]
    esubs = [Segment(pt,seg.ept) for seg,pt in zip(fac,pts)]
    return pts, ssubs, esubs

