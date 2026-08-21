import logging

from requests import get

from api_adapter import APIAdapter

logger = logging.getLogger(__name__)


class Api_Coord(APIAdapter):
    """Класс объекта, отвечающего за получение координат определенной страны"""

    def __init__(self, country: str):
        super().__init__()
        self.openstreetmap_url = "https://nominatim.openstreetmap.org/search"
        self.country = country

    def obtaining_information(self) -> dict:
        """Получает из api-ресурса координаты определенной страны"""

        headers_nominatim = {"User-Agent": "test-app/1.0"}

        params_nominatim = {
            "country": self.country,
            "format": "json",
            "limit": 1,
        }
        try:
            for i in range(3):
                logger.info(f"Делаю запрос - {i + 1} попытка")
                response = get(url=self.openstreetmap_url, params=params_nominatim, headers=headers_nominatim)
                if str(response.status_code)[0] == "2":
                    logger.info(f"Ответ получен: код {response.status_code}")
                    geo_coordinates = response.json()[0].get("boundingbox")
                result = {
                    "lamin": geo_coordinates[0],
                    "lamax": geo_coordinates[1],
                    "lomin": geo_coordinates[2],
                    "lomax": geo_coordinates[3],
                }
                break
        except Exception as e:
            logger.error(e)
            return {}

        return result
