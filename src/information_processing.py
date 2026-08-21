import json
import logging
from pathlib import Path

from airplane import Airplane

logger = logging.getLogger(__name__)


class Information_Processing():
    """Класс для объекта, обрабатывающего информацию о самолетах"""

    def __init__(self):
        self.aeroplanes_list = self.creating_a_list_of_aircraft()

    def creating_a_list_of_aircraft(self)->list:
        """Создает список самолетов - объектов"""
        try:
            json_path = Path(__file__).resolve().parent.parent / "data" / "aeroplanes.json"
            with open(json_path, "r") as f:
                data = json.load(f)
        except FileNotFoundError as e:
            logger.error(e)
            return []

        airplanes = []
        logger.info(f'Получен список данных о {len(data)} самолетах')

        for dt in data:
            good: bool = True  # Годность записи для создания объекта
            try:
                # Замена значений скорости и высоты с Null на 0
                dt[9] = 0 if dt[9] is None else dt[9]
                dt[13] = 0 if dt[13] is None else dt[13]

                # Исключение абсурдных случаев
                if dt[9] < 0 or dt[13] < 0 or dt[0] is None or dt[2] is None:
                    good = False
                if dt[9] == 0 and dt[13] > 0:
                    good = False

            except Exception as e: # непредвиденные случаи
                logger.error(e)
                return []

            if good:
                airplanes.append(Airplane(dt[0], dt[2], dt[9], dt[13]))

        logger.info(f'После валидации получен список из {len(data)} самолетов')
        return airplanes
