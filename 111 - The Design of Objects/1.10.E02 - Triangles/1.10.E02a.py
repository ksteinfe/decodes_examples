'''
1.10.E02a
This file is not downloadable, and is only to be used to generate marked-up code

members:
None

methods:
None

'''

"""
"""
class Triangle():
    
    def __init__(self, pt_a, pt_b, pt_c):
        self.pa = pt_a
        self.pb = pt_b
        self.pc = pt_c
        

"""
Secondary Attributes
The properties and methods defined here are directly derivative of the three Points that define this triangle, and require little computational overhead to produce. 
"""
@property
def pts(self): return [self.pa,self.pb,self.pc]

@property
def edges(self): 
    e0 = Segment(self.pa,self.pb)
    e1 = Segment(self.pb,self.pc)
    e2 = Segment(self.pc,self.pa)
    return [e0,e1,e2]

def edge(self,index):
    if index == 0 : return Segment(self.pa,self.pb)
    elif index == 1 : return Segment(self.pb,self.pc)
    elif index == 2 : return Segment(self.pc,self.pa)
    else: return False    
    


"""
Derivative Attributes
The properties and methods defined here are directly derivative of the three Points that define this triangle, and require little computational overhead to produce. 
"""

"""
"""
@property
def centroid(self): return Point.centroid(self.pts)


"""
"""   
@property
def plane(self): 
    vec = self.edges[0].vec.cross(Vec(self.pa,self.pc))
    return Plane(self.centroid,vec)

    
"""
"""
@property
def perimeter(self): return sum([e.length for e in self.edges])


"""
"""
@property
def area(self):
    #http://www.mathopenref.com/heronsformula.html
    p = self.perimeter/2.0
    a = self.edge(0).length
    b = self.edge(1).length
    c = self.edge(2).length
    return (p*(p-a)*(p-b)*(p-c))**0.5