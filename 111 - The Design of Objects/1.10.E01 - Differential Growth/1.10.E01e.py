'''
1.10.E01e
Field Development Step Two

members:
member (Type) description

methods:
method_name (Return Type) description

'''

"""
Field Class v0.2
A Field is recomposed as a Bounds and two sets of Intervals that decompose the x- and y-intervals of the Bounds of this Field. Rather than storing the resolution as a member, we may leave it implied by the number of divisions in these sets of Intervals.
"""

class Field():
    
    def __init__(self, bnd, res):
        self.bnds = bnd
        # ivals are not expected to change,
        self._ivals_u = bnd.ival_x // res
        # and so we mark them here as 'private' members
        self._ivals_v = bnd.ival_y // res

    @property
    # Field.res appears inherent, but is actually derivative
    def res(self): return len(self._ivals_u)
        
    """
    Bounds At
    Returns the sub-Bounds of this Field that corresponds with a given coordinate-pair. U and V are not spatial coordinates, but rather are integer numbers that index the stored lists of Intervals defined above.
    """
    def bnds_at(self,u,v):
        return Bounds(ival_x = self._ivals_u[u], ival_y = self._ivals_v[v])
        
    """
    Bounds Of
    Returns the u-v coordinates related to the sub-Bounds of this Field that encompasses a given spatial Point. Returns False if the given Point does not lie within the Bounds of this Field.
    """
    def bnds_of(self,pt):
        if not pt in self.bnds: return False
        for u, ival_u in enumerate(self._ivals_u): if pt.x in ival_u: break
        for v, ival_v in enumerate(self._ivals_v): if pt.y in ival_v: break
        return(u,v)
        
    """
    To Polyline
    Returns a PLine demarcating the boundary of each sub-Bounds of this Field
    """
    def to_plines(self):
        coords = [(u,v) for u in range(self.res) for v in range(self.res)]
        return [self.bnds_at(u,v).to_pline() for u,v in coords]   
        
        
"""
Field Test Rig v0.1
"""
fld = Field( bnd , res )
plns = fld.to_plines()

