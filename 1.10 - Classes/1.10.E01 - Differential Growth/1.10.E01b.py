'''
1.10.E01b
Node Development Step Two

members:
member (Type) description

methods:
method_name (Return Type) description

'''

"""
Node Class v0.2
A Node is recomposed as a special kind of Point that has a parent and a child, and is capable of moving away from them.
"""

class Node(Point):
    #a maximum translation distance
    max_step = 0.5
    #a comfortable distance from one Node to another
    max_dist = 2.0
    
    def __init__(self, pos, pnt=False):
        self.set_pos(pos)
        # upon construction, this Node *might* know its parent Node
        self.parent = pnt
        # if present, inform the parent that this Node is his child
        if pnt: pnt.child = self
        # upon construction, all Nodes are childless
        self.child = False
        
        # set an initial desired vector of movement
        self.tvec = Vec()
        
    """
    Translate Node
    Moves this node along its desired vector, and resets desired vector to zero. 
    """
    def translate(self):
        self.set_pos(self + self.tvec)
        self.tvec = Vec()
        
    """
    Set Translation Vector
    Defines a desired vector of movement for this Node so that it moves away from any related Nodes. Collisions with unrelated Nodes are ignored.
    """
    def set_tvec(self,others):
        # if present, move away from parent
        if self.parent: self.tvec += Vec(self.parent,self).normalized()
        # if present, move away from child
        if self.child: self.tvec += Vec(self.child,self).normalized()
        # limit translation vector
        self.tvec = self.tvec.limited(Node.max_step)
        
    """
    Segment Constructor
    Produces a line segment between this Node and its parent Node. This method is necessary because as new Nodes are added to a thread, the order of Nodes in the thread collection is not maintained.
    """
    @property
    def seg(self):
        # if parentless, do nothing
        if not self.parent: return False
        # otherwise, return a line segment
        return Segment(self,self.parent)
        
        
        
"""
===================================
Thread Simulation v0.2
[noprint]
"""

"""
Thread Initialization v0.2
The collection of Nodes is initialized in much the same way as in v0.1, but must account for the assigning of parent-child relationships. Note that the first Node added is explicitly parentless, and that the last Node added is implicitly childless.
"""
thread = [Node(initial_pts[0])]
for pt in initial_pts[1:]:
    thread.append( Node(pt,thread[-1]) )
    

"""
Thread Expansion Simulation v0.2
In contrast with v0.1, Nodes now respond to one another. As a result, we must separate setting the desired vector of translation from the actual movement of the Node. Also, Nodes are added when the distance between child and parent grows too large.
"""
for t in range(sim_steps):
    # ask each Node to set its translation vector
    for nod in thread: nod.set_tvec(thread)
    # ask each Node to translate
    for nod in thread: nod.translate()
    
    # check for segments that are too long
    for nod in thread:
        if nod.parent:
            # if parent is present and too close, insert a new node
            if nod.distance(nod.parent) > Node.max_dist:
                new_node = Node(Point.interpolate(nod,nod.parent), nod.parent)
                
                # tell this new node that i am his son
                new_node.child = nod
                # tell my parent that he has a new child
                nod.parent.child = new_node
                # tell myself to remember that this new node is my parent
                nod.parent = new_node
                # add this new node to the thread
                thread.append(new_node)
        
        
        
