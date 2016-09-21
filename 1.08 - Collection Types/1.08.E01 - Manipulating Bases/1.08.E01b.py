'''
1.08.E01b
TODO

required: 
todo

result: 
todo

'''

"""
By assigning alternative bases to existing Polylines, we may perform basic translations and rotations.
"""

plines = []
for theta in Interval(0,math.pi*2)/count:
    basis = CS().on_xy(rot=theta)
    plines.append(PLine(pl.pts,basis))

a.put(plines)

