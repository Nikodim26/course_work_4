import logging
from pathlib import Path

from adding_a_plane import Adding_Plane
from api_aeroplanes import Api_Aeroplanes
from api_coord import Api_Coord
from write_file import Write_File

log_path = Path(__file__).resolve().parent.parent / "logs" / "main.log"
logging.basicConfig(
    level=logging.INFO,
    filemode="w",
    encoding="UTF8",
    filename=log_path,
    datefmt="%d-%m-%Y в %H:%M:%S",
    format="%(levelname)s: %(asctime)s %(name)s %(message)s",
)
logger = logging.getLogger(__name__)

api_coord = Api_Coord("Germany")
coordinates = api_coord.coordinates
# print(coordinates)

api_aeroplanes = Api_Aeroplanes(coordinates)
print(api_aeroplanes.list_info)

a = Write_File('aeroplanes.json',api_aeroplanes.list_info)
a.write_file()

a=Adding_Plane('aeroplanes.json',api_aeroplanes.list_info)

a.write_file_add("aaaa", "Germany", 143.42, 1789.92)

#
# aeroplanes = Aircraft_Creation().aeroplanes_list
#
#
# V_max=0
# H_max=0
# aeroplane_max=aeroplanes[0]
#
# for aeroplane in aeroplanes:
#     if aeroplane>aeroplane_max:
#         aeroplane_max=aeroplane
#
#     if aeroplane.velocity>V_max:
#         V_max=aeroplane.velocity
#
#     if aeroplane.geo_altitude > H_max:
#         H_max = aeroplane.geo_altitude
#
# print(aeroplane_max.velocity)
# print(V_max)
# print(aeroplane_max.geo_altitude)
# print(H_max)

# a1 = Airplane(*["39de4b", "France", 243.42, 10789.92])
# print(a1)

# a2 = Airplane(*["36de4b", "Germany", 143.42, 1789.92])
#
# aircraft_creation = Aircraft_Creation()
# print(aircraft_creation.comparison_by_speed_and_height(a2,a1))
