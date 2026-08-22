import logging

logger = logging.getLogger(__name__)


class Airplane():
    """Класс для создания объекта - самолета"""

    def __init__(self, ICAO24, Country_of_registration, velocity, geo_altitude):
        self.ICAO24 = ICAO24
        self.Country_of_registration = Country_of_registration
        self.velocity = 0 if velocity is None else velocity
        self.geo_altitude = 0 if geo_altitude is None else geo_altitude

        # Валидация данных
        if (self.velocity < 0 or self.geo_altitude < 0) or (
                self.velocity == 0 and self.geo_altitude != 0) or ICAO24 is None or Country_of_registration is None:
            raise ValueError('Недопустимые значения')

    def __gt__(self, other):
        """Определяет какой самолет выше и быстрее летит"""

        return self.velocity > other.velocity and self.geo_altitude > other.geo_altitude
