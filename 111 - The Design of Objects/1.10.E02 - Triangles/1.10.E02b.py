'''
1.10.E02b
TODO

members:
None

methods:
None

'''

"""
"""
class RightTriangle(Triangle):
    
    def __init__(self, cs, width, height):
        self.basis = cs
        self.w = width
        self.h = height

"""
"""        
    @property
    def pa(self): return self.basis.origin
        
    @property
    def pb(self): return self.basis.eval(self.w,0)
    
    @property
    def pc(self): return self.basis.eval(0,self.h)


"""
"""    
    @property
    def area(self):
        return (self.w*self.h)/2.0