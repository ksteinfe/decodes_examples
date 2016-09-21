'''
1.12.E04a
Demonstrates the decomposition of a rotational surface into cones and cylinders. 

required:

rot_surf (Surface) - rotational surface to decompose


result:
apex ([Point])
side ([Segment])
base ([Circle])

'''


"""
Decomposition of Rotational Surface into Cones and Cylinders
Given a RotationalSurface rot_surf, decompose into constituent cones and cylinders as described by the base Circle, side Segment, and apex Point (for cones). Determining which of three cases is at work (cone, cylinder, inverted cone) is accomplished by testing the angle between an edge of a decomposed isopolyline and the center axis of the Surface.
"""
axis = Ray(rot_surf.center, rot_surf.axis)
pline = rot_surf.isopolyline(u_val = 0, res = res)

for seg in pline.edges: 
    cpt, t, rad = axis.near(seg.spt)
    dot = Vec(cpt, seg.spt).dot(seg.vec)
    
    #if part of a cylinder, define a side but no apex
    if dot == 0: side = seg
    else:
        d = rad/tan(seg.vec.angle(axis.vec))
        #if part of a cone, with seg.spt at the base
        if dot < 0:
            apex = cpt + axis.vec*d
            side = Segment(seg.spt, apex)
            
        #if part of a cone, with seg.ept at the base
        if dot > 0:
            # redefine cpt and radius
            cpt, t, rad = axis.near(seg.ept)
            apex = cpt - axis.vec*d
            side = Segment(seg.ept, apex)       
    
    # define the base Circle for cones and cylinders
    base = Circle(Plane(cpt, axis.vec), rad)