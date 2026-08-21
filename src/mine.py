import json
import logging
from pathlib import Path

from api_aeroplanes import Api_Aeroplanes
from api_coord import Api_Coord

log_path = Path(__file__).resolve().parent.parent / "logs" / "main.log"
logging.basicConfig(
    level=logging.INFO,
    filemode="w",
    encoding="UTF8",
    filename=log_path,
    datefmt="%d-%m-%Y в %H:%M:%S",
    format="%(levelname)s: %(asctime)s %(name)s %(message)s",
)

if __name__ == "__main__":
    api_coord = Api_Coord("Germany")
    a = api_coord.obtaining_information()
    print(a)

    # api_aeroplanes = Api_Aeroplanes(a)
    # print(json.dumps(api_aeroplanes.obtaining_information(), indent=4))
