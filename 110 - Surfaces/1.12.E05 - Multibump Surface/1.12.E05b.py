'''
1.12.E05b

required:

result:

'''

"""
Bounds Displacement
Given a u,v location within a Bounds bnds, returns the displacement that corresponds to this location as a function of a cosine surface that evaluates to zero at the boundary of the given Bounds, and evaluates to a maximum value at its center that is governed by the given factor.
"""
def displace(u,v,bnds,factor):
    upi = Interval.remap(u, bnds.ival_x, Interval.twopi())
    vpi = Interval.remap(v, bnds.ival_y, Interval.twopi())
    h = factor*bnds.dim_x*bnds.dim_y
    return h*(1-cos(upi))*(1-cos(vpi))

"""
Graph Multi-Displacement Surface
Given a collection of Bounds bnds_disp, constructs a graph surface that fits a given Bounds bnds_srf with a height that is determined by the sum of displacements on each given bnds_disp.
"""
def func(u,v):
    #initialize pt with no height
    pt = bnds_srf.eval(u,v)
    for bnds in bnds_disp:
        #{a} increase z-height of plotted pt if it is contained in bnds
         if pt in bnds: pt.z += displace(pt.x,pt.y,bnds,h_fac)
    return pt

    srf = Surface(func)


"""
Flat Multi-Displacement Surface
Given a Surface srf with arbitrary two-dimensional boundary curves, and a collection of Bounds bnds_disp, constructs a Surface as a displacement of srf by the sum of displacements on each given bnds_disp.
"""
    for bnds in bnds_disp:
        #{b} displace plotted pt if u,v is contained in bnds
        if Point(u,v) in bnds: pt.z += displace(u,v,bnds,h_fac)

"""
Three-Dimensional Multi-Displacement Surface
Given an arbitrary Surface srf and a collection of Bounds bnds_disp, constructs a Surface as a displacement of srf by the sum of displacements on each given bnds_disp.
"""
    for bnds in bnds_disp:
        # a vector normal to the Surface
        vec = -base_surf.eval_pln(u,v).normal
        #{c} translate plotted pt along vec if u,v is contained in bnds
        if Point(u,v) in bnds: pt += vec * displace(u,v,bnds,h_fac)


"""
Multi-bump Flat Surface
[noprint]
"""
def func(u,v):
    pt = base_surf.eval(u,v)
    for bnds in bnds_disp:
         if Point(u,v) in bnds: pt.z += displace(u,v,bnds,h_fac)
    return pt

srf = Surface(func)



"""
Multi-bump Arbitrary Surface
[noprint]
"""
def func(u,v):
    pt = base_surf.eval(u,v)
    for bnds in bnds_disp:
        vec = base_surf.eval_pln(u,v).normal
        if Point(u,v) in bnds: pt += vec * displace(u,v,bnds,h_fac)
    return pt

srf = Surface(func)