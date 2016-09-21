'''
1.12.E04b

required:


result:


'''


"""
Curve on a Surface
Given a Surface srf and a Curve crv_dom that lies within the domain of srf, we define another Curve crv_srf that follows the shape of crv_dom along the surface of srf.
"""
def func_crv_srf(t):
    pt_dom = crv_dom.eval(t)
    u,v = pt_dom.x, pt_dom.y
    return srf.deval(u,v)

crv_srf = Curve(func_crv_srf, Interval())

"""
Unwrapped Curve
Given the same variables and results described above, in addition to a List of Xforms xf_flat that describes a mapping between a developable strip of the Surface srf and its unrolled state (and is indexed by strip), here we define a Curve crv_flt that describes the unwrapping of the Curve crv_srf.
"""
def func_crv_flt(t):
    pt_dom = crv_dom.eval(t)
    u = pt_dom.x
    
    strip_idx = int( floor( (u-u0) / tol_u ) )
    if strip_idx == res_u: strip_idx = res_u-1
    
    return crv_srf.eval(t) * xf_flat[strip_idx]
    
crv_flt = Curve(func_crv_flt, Interval())