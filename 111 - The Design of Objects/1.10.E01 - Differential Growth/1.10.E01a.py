'''
1.10.E01a
Node Development Step One

members:
member (Type) description

methods:
method_name (Return Type) description

'''

"""
Node Class v0.1
A Node is a special kind of Point that is capable of translating its spatial position.
"""

class Node(Point):
    #a maximum translation, applicable to all Nodes.
    max_step = 0.5
    
    def __init__(self, pos):
        self.set_pos(pos)
        
    """
    Set Position
    Defines the position of this Node to match the position of a given Point.
    """
    def set_pos(self,pos): self.x, self.y, self.z = pos.x, pos.y, pos.z
        
    """
    Translate Node
    Moves this node along its desired vector. This initial version of the translate method simply moves the Node away from a Point at (0,0).
    """        
    def translate(self):
        tvec = Vec(Point(),self).limited(Node.max_step)
        self.set_pos(self + tvec)
    


"""
===================================
Thread Simulation v0.1
[noprint]
"""
    
"""
Thread Initialization v0.1
Our "thread" is not formalized as a type, but rather is simply an ordered collection of Nodes.
"""
thread = [Node(pt) for pt in initial_pts]

"""
Thread Expansion Simulation v0.1
This collection of Nodes may "grow" simply by calling the translate function of each Node for as many steps as we wish to simulate. We may visualize this "thread" simply by constructing a PLine.
"""
for t in range(sim_steps):
    for nod in thread: nod.translate()

pl = PLine(thread)