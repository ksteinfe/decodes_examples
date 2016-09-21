'''
1.10.E01f
Field Development Step Three

members:
member (Type) description

methods:
method_name (Return Type) description

'''

"""
Field Class v0.3
In this version, functionality is added for retrieving all sub-Bounds of this Field that are adjacent to the bounds that encompasses a given Point. This constructor is unaltered from the Field Class v0.2
"""

class Field():
    
    def __init__(self, bnd, res):
        self.bnds = bnd
        self._ivals_u = bnd.ival_x // res
        self._ivals_v = bnd.ival_y // res
                
    """
    Bounds Near
    Returns a list of sub-Bounds of this Field relevant to a given Point, including the sub-Bounds encompassing this Point and those adjacent to it.
    """
    def bnds_near(self,pt):
        u,v = self.bnds_of(pt)
        # an error has been left intentionally on this line of code
        crds = [\
            (u-1,v-1),(u,v-1),(u+1,v-1),\
            (u-1,v+1),(u,v),(u+1,v),\
            (u-1,v+1),(u,v+1),(u+1,v+1)\
        ]
            
        def is_valid(crd):
            if crd[0]<0 or crd[1]<0 : return False
            if or crd[0]>=self.res or crd[1]>=self.res: return False 
            return True
            
        return [ self.bnds_at(crd[0],crd[1]) for crd in crds if is_valid(crd) ]
        
    """
    Unaltered Methods
    [noprint]
    """
    @property
    def res(self): return len(self._ivals_u)    
    
    def bnds_at(self,u,v):
        return Bounds(ival_x = self._ivals_u[u], ival_y = self._ivals_v[v])
        
    def bnds_of(self,pt):
        if not pt in self.bnds: return False
        
        for u, ival_u in enumerate(self._ivals_u):
            if pt.x in ival_u: break
        for v, ival_v in enumerate(self._ivals_v):
            if pt.y in ival_v: break
        
        return(u,v)

    def to_plines(self):
        coords = [(u,v) for u in range(self.res) for v in range(self.res)]
        return [self.bnds_at(u,v).to_pline() for u,v in coords]           