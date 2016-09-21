'''
1.10.E01h
Field Development Step Five

members:
member (Type) description

methods:
method_name (Return Type) description

'''

"""
Field Class v1.0
A Field is recomposed as a Bounds, two sets of Intervals, a dictionary of sub-Bounds, and a dictionary of Point-like objects
This constructor is unaltered from the Field Class v0.4, with the exception of the codeblock noted below.
"""

class Field():
    
    def __init__(self, bnd, res):
        self.bnds = bnd
        self._ivals_u = bnd.ival_x // res
        self._ivals_v = bnd.ival_y // res
                
        self._sbnds = {}
        for u in range(self.res):
            for v in range(self.res):
                self._sbnds[(u,v)] = Bounds(\
                ival_x = self._ivals_u[u],\
                ival_y = self._ivals_v[v]\
                )
        
        """
        Establish Point Dictionary
        In the constructor, a dictionary is initialized for storing Point-like objects. Dictionary keys are established for each possible u,v coordinate combination, and are related to empty arrays into which we will append Points.
        """
        self.pt_dict = {}
        for u in range(self.res):
            for v in range(self.res):
                self.pt_dict[(u,v)] = []        
        
        
    """
    Append Point
    Adds a given Point to the proper bin in this Field's pt_dict
    """
    def append(self,pt):
        crd = self.bnds_of(pt)
        if not crd: return False
        else:
            if pt in self.pt_dict[crd[0],crd[1]]: return False
            self.pt_dict[crd[0],crd[1]].append(pt)
            return True
        
    """
    Points At
    Returns Points from the pt_dict dictionary at a given coordinate-pair key.
    """        
    def pts_at(self,u,v): 
        return self.pt_dict[(u,v)]         
        
        
    """
    Bounds Near & Points Near
    Returns the list of sub-Bounds or the Points contained within a sub-Bounds relevant to a given Point.
    [pseudo]
    """   
    def _crds_near(self,u,v):
        crds = [ (u-1,v-1),(u,v-1),(u+1,v-1),(u-1,v),(u,v),(u+1,v),(u-1,v+1),(u,v+1),(u+1,v+1) ]
        # return a list of valid coord-pairs adjacent to a given coord-pair
        return [crd for crd in crds if crd[0]>=0 and crd[1]>=0 and crd[0]<self.res and crd[1]<self.res ]
        
    def bnds_near(self,pt):
        u,v = self.bnds_of(pt)
        # return a list of sub-Bounds adjacent to or encompassing a given Point
        return [ self.bnds_at(crd[0],crd[1]) for crd in self._crds_near(u,v) ]
        
    def pts_near(self,pt):
        ret = []
        u,v = self.bnds_of(pt)
        for crd in self._crds_near(u,v): ret.extend(self.pts_at(crd[0],crd[1]))
        # return Points contained by adjacent or encompassing sub-Bounds
        return ret
        
    """
    Unaltered Methods
    [noprint]
    """
    @property
    def res(self): 
        return len(self._ivals_u)
    
    def bnds_at(self,u,v):
        return self._sbnds[(u,v)]
        
    def bnds_of(self,pt):
        if not pt in self.bnds: return False
        
        for u, ival_u in enumerate(self._ivals_u):
            if pt.x in ival_u: break
        for v, ival_v in enumerate(self._ivals_v):
            if pt.y in ival_v: break
        
        return(u,v)
        
        

        