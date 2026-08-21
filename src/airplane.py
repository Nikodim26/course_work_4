class Airplane():
    """Класс для создания объекта - самолета"""

    def __init__(self, ICAO24, Country_of_registration, velocity, geo_altitude):
        self.ICAO24=ICAO24
        self.Country_of_registration=Country_of_registration
        self.velocity=velocity
        self.geo_altitude=geo_altitude

