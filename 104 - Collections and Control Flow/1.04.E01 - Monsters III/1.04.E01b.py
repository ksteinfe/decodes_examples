'''
1.04.E01b
Monsters III

required:


result:


'''


"""
Walking a Transposed Multi-Dimensional Array
"""
segs_transposed = [[] for v in range(len(pt_grid[0]))]
for u,v in itertools.product(range(count_u),range(count_v)):
    pa = pt_grid[u][v]
    pb = pt_grid[u-1][v]
    segs_transposed[v].append(Segment(pa,pb))





"""
SUPERSEDED
[noprint]
"""
seg_grid_transposed = []
for col_idx in range(len(pt_grid[0])):
    pts = [row[col_idx] for row in pt_grid]
    
    segs = [Segment(pa,pb) for pa,pb in zip(pts[:-1],pts[1:])]
    if col_periodic: segs.append(Segment(pts[-1],pts[0]))
    seg_grid_transposed.append(segs)
