'''
1.06.E03c

required:

result:

'''


"""
Importing Modules
Two modules are required to acquire information regarding the solar position and intensity for a location: the Solar Geometry module, which facilitates the generation of solar positions, and the EPW parser module, which allows us to access files that contain climate data, including the typical solar intensity on an hourly basis.
"""
from decodes.extensions.solar_geometry import SolarGeom
from decodes.extensions.parse_epw import *

"""
Calculating Suns
Here, we use the Solar Geometry module and EPW parser module to create a collection of "suns", each of which stores information regarding the position and typical intensity of the sun for a selection of days of the year for a given location.
"""
# metadata includes lat, long, and timezone
epw_meta = epw_metadata(filepath)
# a utility for calculating solar positions
sg = SolarGeom(epw_meta["lat"], epw_meta["long"], epw_meta["timezone"])
day_step = 10

# use the EPW parser to record radiation values
radiation_values = parse_epw_file(filepath,"DirNormIrad")

suns = []
#tuples that refer to each hour of selected days
for dy,hr in itertools.product(range(0,365,day_step),range(24)):
    # the solar vector for a given day
    sun_vec = sg.vec_at(dy,hr)
    if sun_vec.z > 0: 
        hour_of_year = dy*24+hr
        suns.append( (sun_vec, radiation_values[hour_of_year] ) )


"""
Visualizing Suns
Given an Interval of radiation values (rad_ival) which provides a scale.
"""        
for sun in suns:
    # the amount of radiation, normalized to a given scale
    t = rad_ival.deval(sun[1])
    # a segment of length related to the amount of radiation
    seg = Segment(sun[0], sun[0]*t )
    clr = Color.interpolate( blue, red, t )
    seg.set_color(clr)


"""
Irradiance on a Mesh
Given a single-face Mesh and a collection of suns, the function defined here calculates the amount of radiation that strikes the given mesh face, colors the face according to a given scale interval (sum_ival), and returns the appropriate Color. If the amount of radiation falls outside the given scale, the function returns False.
"""

def color_by_angle(tar_msh,suns):
    pln = Plane.from_pts(tar_msh.face_pts(0))
    val = sum( [sun[1]*aoi(pln,sun[0])**2 for sun in suns] )
    if val not in sum_ival: return False
    clr = Color.interpolate( blue, red, sum_ival.deval(val) )
    tar_msh.set_color(clr)
    return clr

valid_mshs = []    
for m in mshs:
    if color_by_angle(m,suns):
        valid_mshs.append(m)