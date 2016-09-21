'''
1.04.E01c
Monsters III

required:


result:


'''



"""
Non-Standard Weaving Across A Multi-Dimensional Array
"""
off = 2
segs_diag = []
for u,v in itertools.product(range(count_u),range(count_v)):
    pa = pt_grid[u][v]
    pb = pt_grid[u-1][v-off]
    if v-off>=0: segs_diag.append(Segment(pa,pb))




