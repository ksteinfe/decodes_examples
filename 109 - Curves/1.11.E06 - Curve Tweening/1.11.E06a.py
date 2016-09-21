'''
1.11.E06a
Approaches and applications for curve interpolation.

required: 
crv_a (Curve) A Curve at interpolation value 0
crv_b (Curve) A Curve at interpolation value 1
m (float) Interpolation value.
cnt (int) The number of Curves to stack
floorheight (float) The vertical distance between Curves

result:
crv (Curve) An interpolated Curve. 

'''


"""
Tweened Curve
Defines a curve that interpolates between crv_a and crv_b at parameter m
"""
def func(t):
    return crv_a.eval(t)*(1-m) + crv_b.eval(t)*m 

crv = Curve(func,Interval())



"""
An Ordinary Rectangle Curve
Parametrizes a Curve as a rectangle such that t=0 coincides with the bottom right corner
"""
def func(t):
    # divide a normalized domain into four subintervals
    sub_ivals = Interval()//4
    
    # point on right edge
    if t in sub_ivals[0]:
        x = rec_w/2
        y = Interval.remap(t, sub_ivals[0], Interval(-rec_h/2,rec_h/2) )
    # point on top edge
    elif t in sub_ivals[1]:
        x = Interval.remap(t, sub_ivals[1], Interval(rec_w/2,-rec_w/2) )
        y = rec_h/2
    # point on left edge
    elif t in sub_ivals[2]:
        x = -rec_w/2
        y = Interval.remap(t, sub_ivals[2], Interval(rec_h/2,-rec_h/2) )
    # point on bottom edge
    elif t in sub_ivals[3]:
        x = Interval.remap(t, sub_ivals[3], Interval(-rec_w/2,rec_w/2) )
        y = -rec_h/2
        
    return Point(x,y)

"""
A Bespoke Rectangle Curve
Parametrizes a Curve as a rectangle such that it aligns with the parametrization of a regular circle
"""
def func(t):
    # projections onto the bounding lines of the rectangle
    if t != 0 : proj_x = 0.5 * rec_h * cos(t)/sin(t)
    if t != half_pi : proj_y = 0.5 * rec_w * sin(t)/cos(t)
    
    # an angle related to the aspect ratio of this rectangle
    atn = atan(rec_h/rec_w)
    
    # point on top half of right edge
    if t in Interval(0,atn): return Point(rec_w/2,proj_y)
    # point on top edge
    elif t in Interval(atn,pi-atn): return Point(proj_x,rec_h/2)
    # point on left edge
    elif t in Interval(pi-atn,pi+atn): return Point(-rec_w/2,-proj_y)
    # point on bottom edge
    elif t in Interval(pi+atn,two_pi-atn): return Point(-proj_x,-rec_h/2)
    # point on bottom half of right edge
    elif t in Interval(two_pi-atn,two_pi): return Point(rec_w/2,proj_y)
    return Point(x,y)
