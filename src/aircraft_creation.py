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
            good: bool = True  # Годность записи для создания объекта

            for dt in data:
                # Замена значений скорости и высоты с Null на 0
                dt[9] = 0 if dt[9] is None else dt[9]
                dt[13] = 0 if dt[13] is None else dt[13]

                # Исключение абсурдных случаев
                if dt[9] < 0 or dt[13] < 0 or dt[0] is None or dt[2] is None:
                    good = False
                if dt[9] == 0 and dt[13] > 0:
                    good = False

                if good:
                    airplanes.append(Airplane(dt[0], dt[2], dt[9], dt[13]))

        except Exception as e:
            logger.error(e)
            return []

        logger.info(f'После валидации получен список из {len(data)} самолетов')
        return airplanes


    def comparison_by_speed_and_height(self, airplane1:Airplane, airplane2:Airplane)->bool:
        """Сравнивает самолеты по высоте полета и скорости. True, если airplane1 выше и быстрее"""

        return True if airplane1 > airplane2 else False