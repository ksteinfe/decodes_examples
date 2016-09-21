'''
1.02.E01b
Monsters II

required:
TODO

result:
TODO
'''

"""
A Collection of Segments
Here we see the script in its entirety, for clarity plotted using a standard set of coordinate equations to generate a torus
"""
for u in Interval.twopi()/count_u:
    pts = []
    for v in Interval.twopi()/count_v:
        x = (a+b*cos(v))*cos(u)
        y = (a+b*cos(v))*sin(u)
        z = b*math.sin(v)
        pts.append(Point(x,y,z))
    cent = Point.centroid(pts)
    for spt in pts:
        ept = Point.interpolate(spt,cent,0.5)
        seg = Segment(spt,ept)
        clr = Color.HSB(u/math.pi,1,1)
        seg.set_color(clr)
        out.put(seg)