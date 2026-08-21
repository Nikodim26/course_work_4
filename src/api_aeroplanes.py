from requests import get

from api_adapter import APIAdapter


class Api_Aeroplanes(APIAdapter):

    def __init__(self, coordinates: dict) -> None:
        super().__init__()
        self.coordinates = coordinates
        self.openstreetmap_url = "https://opensky-network.org/api/states/all?"

    def obtaining_information(self) -> list:
        """Получение информации о самолетах в координатах страны"""

        return get(url=self.openstreetmap_url, params=self.coordinates).json()
