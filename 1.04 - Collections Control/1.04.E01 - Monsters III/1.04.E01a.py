'''
1.04.E01a
Monsters III

required:


result:


'''

"""
Constructing a Multi-Dimensional Array
"""
pt_grid = []
for u in Interval.twopi()/count_u:
    pt_grid.append([])
    for v in Interval.twopi()/count_v:
        x = ( (a+1)*cos(u) + cos(u*(a+1)) ) * (v + 1)
        y = ( (a+1)*sin(u) + sin(u*(a+1)) ) * (v + 1)
        z = 3.0*sin(v*b)   
        pt_grid[-1].append(Point(x,y,z))

"""
Walking a Multi-Dimensional Array
"""        
seg_grid = []
for row in pt_grid:
    segs = [Segment(pa,pb) for pa,pb in zip(row[:-1],row[1:])]
    if row_periodic: segs.append(Segment(row[-1],row[0]))
    seg_grid.append(segs)
    






