'''
1.10.E01g
Field Development Step Four

members:
member (Type) description

methods:
method_name (Return Type) description

'''

"""
Field Class v0.4
A Field is recomposed as a Bounds, two sets of Intervals, and a dictionary of sub-Bounds that decompose the Bounds of this Field indexed by u-v coordinates.
This constructor is unaltered from the Field Class v0.4, with the exception of the codeblock noted below.
"""

class Field():
    
    def __init__(self, bnd, res):
        self.bnds = bnd
        self._ivals_u = bnd.ival_x // res
        self._ivals_v = bnd.ival_y // res
        
        """
        Establish Bounds Dictionary
        A dictionary of sub-Bounds that decompose the Bounds of this Field, indexed by coordinate-pairs.
        """
        self._sbnds = {}
        for u in range(self.res):
            for v in range(self.res):
                bnds = Bounds( ival_x=self._ivals_u[u] , ival_y=self._ivals_v[v] )
                self._sbnds[(u,v)] = bnds
        
    """
    Bounds At
    Modified to use pre-computed sub-Bounds dictionary
    """
    def bnds_at(self,u,v):
        return self._sbnds[(u,v)]        
        
        
    """
    Unaltered Methods
    [noprint]
    """
    @property
    def res(self): return len(self._ivals_u)    
    
        
    def bnds_of(self,pt):
        if not pt in self.bnds: return False
        
        for u, ival_u in enumerate(self._ivals_u):
            if pt.x in ival_u: break
        for v, ival_v in enumerate(self._ivals_v):
            if pt.y in ival_v: break
        
        return(u,v)
        
    def bnds_near(self,pt):
        u,v = self.bnds_of(pt)
        # an error has been intentionally left on this line of code
        crds = [ (u-1,v-1),(u,v-1),(u+1,v-1),(u-1,v+1),(u,v),(u+1,v),(u-1,v+1),(u,v+1),(u+1,v+1) ]
        def is_valid(crd):
            return crd[0]>=0 and crd[1]>=0 and crd[0]<self.res and crd[1]<self.res
        return [self.bnds_at(crd[0],crd[1]) for crd in crds if is_valid(crd) ]    