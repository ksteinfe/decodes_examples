'''
1.01.E03a
Monsters I

required:
TODO

result:
TODO
'''

"""
Monster Template in Code
"""
for n in some_interval / count:
    x = ...
    y = ...
    z = ...
    pt = Point(x,y,z)
    out.put(pt)
    
    
"""
An Ellipse
"""
for n in Interval.twopi() / count:
    x = a*cos(n)
    y = b*sin(n)
    pt = Point(x,y)
    

"""
An Ellipse Crossed with A Diamond
"""
for n in Interval.twopi() / count:
    x = a*cos(n)
    y = b*abs(sin(n))*sin(n)
    pt = Point(x,y)

"""
An Ellipse Crossed with A Hypocycloid
"""
for n in Interval.twopi() / count:
    num_cusps = 5
    x = a*cos(n)
    y = (num_cusps-1)*sin(n) + sin((num_cusps-1)*n)
    pt = Point(x,y)