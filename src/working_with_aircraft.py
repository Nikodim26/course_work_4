import json
import logging
from pathlib import Path

from airplane import Airplane
from working_with_files import Working_With_Files

logger = logging.getLogger(__name__)


class Working_with_Aircraft(Working_With_Files):
    """Класс для объекта, обрабатывающего информацию о самолетах"""

    def __init__(self, file: str, data: list):
        super().__init__(file, data)
        self.path = Path(__file__).resolve().parent.parent / "data" / file
        self.data = data

    def write_file(self):
        aeroplanes_list = []

        for dt in self.data:
            try:
                aeroplane = Airplane(dt[0], dt[2], dt[9], dt[13])

                aeroplanes_list.append(
                    {"ICAO24": aeroplane.ICAO24,
                     "Country": aeroplane.Country_of_registration,
                     "Velocity": aeroplane.velocity,
                     "Altitude": aeroplane.geo_altitude
                     }
                )
                with open(self.path, "w", encoding="utf-8") as f:
                    json.dump(aeroplanes_list, f, indent=4, ensure_ascii=False)

                logger.info(f'Создана запись данных самолетов в заданном "квадрате" в файл')

            except Exception as e:
                logger.error(e)

    def write_file_add(self, *args):
        try:
            new_aeroplane = Airplane(*args)
            aeroplane = {
                "ICAO24": new_aeroplane.ICAO24,
                "Country": new_aeroplane.Country_of_registration,
                "Velocity": new_aeroplane.velocity,
                "Altitude": new_aeroplane.geo_altitude
            }

            with open(self.path, "r", encoding="utf-8") as f:
                data = json.load(f)

                data.append(aeroplane)
            with open(self.path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)

            logger.info(f'Добавлена информация о самолете в файл')

        except Exception as e:
            logger.error(e)
