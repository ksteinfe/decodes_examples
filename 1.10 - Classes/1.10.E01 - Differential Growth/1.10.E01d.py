'''
1.10.E01d
Field Development Step One

members:
member (Type) description

methods:
method_name (Return Type) description

'''

"""
Field Class v0.1
A Field is composed of a Bounds and a resolution (an integer number of divisions to perform on the Bounds). The same number of divisions will be made in both the x- and y-axes.
"""

class Field():
    
    def __init__(self, bnd, res):
        self.bnds = bnd
        self.res = res
        
    def to_plines(self):
        return [sbnds.to_pline() for sbnds in self.bnds.subbounds(self.res)]
        
        
        
"""
Field Test Rig v0.1
"""
fld = Field( bnd , res )
plns = fld.to_plines()

