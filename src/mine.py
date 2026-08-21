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
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    api_coord = Api_Coord("Germany")
    a = api_coord.obtaining_information()
    print(a)

    api_aeroplanes = Api_Aeroplanes(a)
    json_path = Path(__file__).resolve().parent.parent / "data" / "aeroplanes.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(api_aeroplanes.obtaining_information(), f, indent=4, ensure_ascii=False)
    logger.info(f'Создан json-файл со списком самолетов')