import logging
from pathlib import Path

from api_aeroplanes import Api_Aeroplanes
from api_coord import Api_Coord
from information_processing import Aircraft_Creation

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
print(coordinates)

api_aeroplanes = Api_Aeroplanes(coordinates)
api_aeroplanes.obtaining_information()

aeroplanes = Aircraft_Creation()
a = aeroplanes.aeroplanes_list
print(a)
print(len(a))
print(type(a[0]))
