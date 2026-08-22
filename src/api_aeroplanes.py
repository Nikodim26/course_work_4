import json
import logging
from pathlib import Path

from requests import get

from api_adapter import APIAdapter

logger = logging.getLogger(__name__)


class Api_Aeroplanes(APIAdapter):
    """Класс объекта, отвечающего за получение инормации о самолетах в заданном квадрате"""

    def __init__(self, coordinates: dict) -> None:
        super().__init__()
        self.coordinates = coordinates
        self.url = "https://opensky-network.org/api/states/all?"

    def obtaining_information(self) -> None:
        """Получение информации о самолетах в координатах страны"""

        try:
            for i in range(3):
                logger.info(f"Делаю запрос - {i + 1} попытка")
                response = get(url=self.url, params=self.coordinates)
                if str(response.status_code)[0] == "2":
                    logger.info(f"Ответ получен: код {response.status_code}")
                    result = response.json()["states"]

                    # Фильтрация дублей записей (вдруг есть)
                    aeroplanes_list=[]

                    for dt in result:
                        if not dt in aeroplanes_list:
                            aeroplanes_list.append(dt)

                        # Запись в файл
                        json_path = Path(__file__).resolve().parent.parent / "data" / "aeroplanes.json"
                        with open(json_path, "w", encoding="utf-8") as f:
                            json.dump(aeroplanes_list, f, indent=4, ensure_ascii=False)

                        logger.info(f'Создана запись данных самолетов в заданном "квадрате" в файл')

                    break

        except Exception as e:
            logger.error(e)