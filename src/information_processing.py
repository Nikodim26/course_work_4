import json
import logging
from pathlib import Path

from airplane import Airplane

logger = logging.getLogger(__name__)


class Aircraft_Creation():
    """Класс для объекта, обрабатывающего информацию о самолетах"""

    def __init__(self):
        self.aeroplanes_list = self.creating_a_list_of_aircraft()

    def creating_a_list_of_aircraft(self) -> list:
        """Создает список самолетов - объектов"""
        try:
            json_path = Path(__file__).resolve().parent.parent / "data" / "aeroplanes.json"
            with open(json_path, "r") as f:
                data = json.load(f)

            airplanes = []
            for dt in data:
                airplanes.append(Airplane(dt[0], dt[2], dt[9], dt[13]))

        except FileNotFoundError as e:
            logger.error(e)
            return []

        logger.info(f'После валидации получен список из {len(data)} самолетов')
        return airplanes
