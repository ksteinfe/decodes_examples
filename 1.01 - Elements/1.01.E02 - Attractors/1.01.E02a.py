'''
1.01.E02a
Pulls a set of points toward an attractor point.

required:
pts [Point]A list of points to displace.
attr_pt Point An "attractor" point that influences a given list of points.
power float The strength of the attraction, described as the exponent number to raise the distance between a given point and the attractor point. For example, a power value of 0.5 will apply a square root function to the measured distance, while a power value of 3.0 will raise the measured distance to the power of three.
max_dist_pct float The maximum distance that any point may move, described as a percentage of the distance between a given point and the attractor point. This has the effect of ensuring that no point overshoots the attractor point.

result:
outie	An outie containing a list of points that have been moved
'''

"""
Attract Points
Given an attractor Point and a list of Points to attract, iterates through each Point using a list and applies the attractor routine to each point in succession.
"""
# 1. create a container to store the translated points
new_pts = []
for grid_pt in pts: # 2. iterate over each point in pts
    # 3. create a vector from 'grid_pt' to the attractor point
    vec = Vec(grid_pt,attr_pt)
    
    max_dist = vec.length * max_dist_pct
    desired_dist = vec.length ** power
    dist = min( max_dist , desired_dist )
    
    # 4. create a new displaced point
    new_pt = grid_pt + vec.normalized(dist)
    
    # 5. add this newly constructed Point to our list 
    new_pts.append(new_pt)
    