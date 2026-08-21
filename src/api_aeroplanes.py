import logging

from requests import get

from api_adapter import APIAdapter

logger = logging.getLogger(__name__)


class Api_Aeroplanes(APIAdapter):

    def __init__(self, coordinates: dict) -> None:
        super().__init__()
        self.coordinates = coordinates
        self.url = "https://opensky-network.org/api/states/all?"

    def obtaining_information(self) -> list:
        """Получение информации о самолетах в координатах страны"""

        aeroplanes_list = []
        try:
            for i in range(3):
                logger.info(f"Делаю запрос - {i + 1} попытка")
                response = get(url=self.url, params=self.coordinates)
                if str(response.status_code)[0] == "2":
                    logger.info(f"Ответ получен: код {response.status_code}")
                    result = response.json()["states"]

                    for l in result:
                        if not l in aeroplanes_list:
                            aeroplanes_list.append(l)
                break

        except Exception as e:
            logger.error(e)
            return []

        logger.info(f'Получен список самолетов в заданном "квадрате"')
        return aeroplanes_list
