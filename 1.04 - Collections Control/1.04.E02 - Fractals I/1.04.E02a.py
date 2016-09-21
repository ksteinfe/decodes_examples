'''
1.04.E02a
Fractals I

required:


result:


'''

"""
Initialize Parameters and Collections
Two Lists are used in the course of the script: The first collects the line segments we seek to output. The second acts as a queue, and stores the information needed for a progressive subdivision. This information is structured as a Dictionary of two values: a coordinate system that indicates the position and orientation of a branch, and a float that indicates its scale.
"""
# angle constants of the tree branches
RADS = ( 0, math.pi/2, 3*math.pi/2 ) #0,90,270 deg
# factor to scale branches at each step
scale_fac = 0.5
# minimum length of tree branches
min_length = 0.02

# collects line segments we week to output
segs = []
#{a} acts as a "queue"
nodes = [ {"cs":CS(),"size":0.5} ]


"""
Alternative Branch Configuration
Specifying four branches generates a space-filling curve, but also produces overlapping lines.
[noprint]
"""
RADS = ( 0, math.pi/2, math.pi, 3*math.pi/2 ) #0,90,180,270 deg


"""
Main Loop
The main cycle of the routine progressively processes the oldest available node into smaller nodes, scaling the branch length down by a given factor at each subdivision. If the branch length falls below a given threshold, no subdivision occurs, no new nodes are produced, and the queue is eventually emptied.
"""
# exit if there are no nodes to process
while len(nodes) > 0:
    # {b} retrieve the oldest node in the queue
    node = nodes.pop(0)
    # calculate the scale for any tip nodes
    tip_size = node["size"]*scale_fac
    
    # for each given angle:
    for rad in RADS:
        # construct a segment at this angle
        pa = node["cs"].origin
        # note the use of cylindrical coordinates
        pb = node["cs"].eval_cyl(node["size"],rad)
        seg = Segment(pa,pb)
        segs.append(seg)
        
        # if the tip node is above threshold length
        if tip_size > min_length:
            # construct a CS at the tip of this segment
            origin, vec_x, vec_y = seg.ept, seg.vec, seg.vec.cross(UZ)
            tip_cs = CS(origin,vec_x,vec_y)
            # create a new node as a dict
            node = {"cs":tip_cs,"size":tip_size}
            # {c} add the newly created node to the queue
            nodes.append(node)
            
