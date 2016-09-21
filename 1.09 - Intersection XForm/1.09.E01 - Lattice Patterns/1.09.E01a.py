'''
1.09.E01a
Arab Lattice Pattern

required:
TODO

result:
TODO


'''

"""
Tile Definition
A collection of Segments is defined that form the base_tile for a pattern that suggests overlaid grids. The outer edges of a unit square are defined, and then transformed to produce an inner set of edges. These are then connected to produce the base_tile. 
"""
cnr_pts = [Point(x,y) for x,y in [(0,0),(1,0),(1,1),(0,1)]]
cpt = Point(0.5,0.5)
out_edges = [Segment(pa,pb) for pa,pb in match(cnr_pts,[0,1])]

xf_scl = Xform.scale(factor,cpt)
xf_rot = Xform.rotation(center=cpt,angle=math.pi/6)
in_edges = [edge*xf_rot*xf_scl for edge in out_edges]

base_tile = [Segment(sa.spt,sb.ept) for sa,sb in zip(out_edges,in_edges)]


"""
Mirrored Tessellation
A given base_tile is transformed along the x- and y-axis to produce a tessellation. Tiles of alternating rows and columns are mirrored about their center before being placed.
"""
for u,v in itertools.product(range(cols),range(rows)):
    xf = Xform.translation(UX * u) * Xform.translation(UY * v)
    if (u+v)%2 == 0: xf *= Xform.mirror(Plane(cpt,Vec(1,0)))
    tile = [seg * xf for seg in base_tile]
    
    
"""
Selectively Mirrored Tessellation
Two given base_tiles are transformed along the x- and y-axis to produce a tessellation. The Segments described by mir_tile are mirrored in alternating rows and columns, while those contained in stb_tile are not.
"""
for u,v in itertools.product(range(cols),range(rows)):
    xf = Xform.translation(UX * u) * Xform.translation(UY * v)
    tile = [seg * xf for seg in stb_tile]
    if (u+v)%2 == 1: xf *= Xform.mirror(Plane(Point(),Vec(1,0)))
    tile.extend([seg * xf for seg in mir_tile])