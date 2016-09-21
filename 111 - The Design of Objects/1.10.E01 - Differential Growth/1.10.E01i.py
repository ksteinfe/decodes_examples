'''
1.10.E01i
Incorporation of Field Class Step One

members:
member (Type) description

methods:
method_name (Return Type) description

'''

"""
Node Class v2.0
Node is initialized with a position and a bounds
"""

class Node(Point):
    max_step = 0.25
    max_dist = 1.0
    
    def __init__(self, pos, bnds):
        self.set_pos(pos)
        self.bnds = bnds
        
        self.tvec = Vec()
        
    """
    Set Translation Vector
    
    """
    def set_tvec(self,others):
        others = [node for node in others if node is not self]
        
        self.tvec = Vec(self).normalized(0.1)
        if len(others) == 1: self.tvec += Vec(others[0], self).normalized(0.1)
        if len(others) > 1:
            others = sorted(others, key=lambda other: self.distance2(other))
            # vector away from nearest node
            vec_a = Vec(others[0],self).normalized()
            # vector away from second-nearest node            
            vec_b = Vec(others[1],self).normalized()
            v =  vec_a + vec_b
            if v.length > 0: self.tvec += v
        
        self.tvec = self.tvec.limited(Node.max_step)
    
    """
    Node Is In Bounds    
    """
    @property
    def in_bds(self):
        return self in self.bnds
        
    """
    Unaltered Methods
    [noprint]
    """
    def set_pos(self,pos): self.x, self.y, self.z = pos.x, pos.y, pos.z
    
    def translate(self):
        self.set_pos(self + self.tvec)
        self.tvec = Vec()
        
        

        
"""
===================================
Thread Simulation v1.1
[noprint]
"""

"""
Initialize Field and Thread
"""
fld = Field( bnd , FIELD_RES )

thread = []
for pt in initial_pts:
    u,v = fld.bnds_of(pt)
    node = Node(pt,fld.bnds_at(u,v))
    thread.append(node)
    fld.append(node)


"""
Simulate Thread Expansion
"""
for t in range(SIM_STEPS):
    # calculate translation for each node
    for node in thread: node.set_tvec(fld.pts_near(node))
    
    # translate each node
    for node in thread: node.translate()
    
    # update field
    for (u,v) in fld.pt_dict:
        # remove out of bounds nodes from the dictionary
        fld.pt_dict[(u,v)] = [node for node in fld.pt_dict[(u,v)] if node.in_bds]
    # update the bounds of any out of bounds nodes
    for node in thread:
        if not node.in_bounds:
            # node has exited our canvas
            if node not in fld.bnds: node.set_pos(fld.bnds.near_pt(node)) 
            u,v = fld.bnds_of(node)
            node.bnds = fld.bnds_at(u,v)
            fld.append(node)
                
    # add extra nodes where needed
    next_thread = [thread[0]]
    for n in range(1,len(thread)):
        # node has exited our canvas
        if thread[n].distance(thread[n-1]) > Node.max_dist:
            pt = Point.interpolate(thread[n],thread[n-1])
            u,v = fld.bnds_of(pt)
            node = Node(pt,fld.bnds_at(u,v))
            next_thread.append(node)
            fld.append(node)
            
        next_thread.append(thread[n])
    thread = next_thread
    