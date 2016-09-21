'''
1.10.E01c
Node Development Step Three

members:
member (Type) description

methods:
method_name (Return Type) description

'''

"""
Node Class v1.0
Constructor Unaltered
[noprint]
"""

class Node(Point):
    rov = 1.0
    max_step = rov * 0.5
    max_dist = 4.0

    def __init__(self, pos, pnt=False):
        self.set_pos(pos)
        self.parent = pnt
        # inform the parent of this Node that this Node is his child
        if pnt: pnt.child = self
        self.child = False
        self.tvec = Vec()
        


    """
    Set Translation Vector v0.3
    Version three of our Node alters only this method to account for collisions with unrelated Nodes. Two types of movement are defined: one type if there are unconnected Nodes in the vicinity, and another if there are not.
    """
    def set_tvec(self,others):
        # find unconnected Nodes in the vicinity of this Node
        bnds = Bounds.unit_square(Node.rov*2,self)
        def is_nearby_and_unrelated(other, bnds):
            if other is self: return False
            if other is self.parent or other is self.child: return False
            if other not in bnds: return False
            return other.distance(self) < Node.rov
        
        nears = [nod for nod in others if is_nearby_and_unrelated(nod, bnds)]
        
        # if unconnected Nodes are too close, move to avoid collision
        if len(nears) > 0:
            nearest = Point.near(self,nears)
            self.tvec = Vec(nearest,self).normalized(Node.rov*0.25)
        # if there are not, move to expand length of yarn
        else:
            if self.parent: self.tvec += Vec(self.parent,self).normalized()
            if self.child: self.tvec += Vec(self.child,self).normalized()
        
        self.tvec = self.tvec.limited(Node.max_step)
        
        
        