import unittest
from helper.weather_helper import WeatherHelper

class TestWeather(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Setting Up the DB")
        cls.weather_helper = WeatherHelper(test=True)

    def test_weather_service_one(self):
        self.assertEqual(self.weather_helper.get_station_date_with_lowest_temp(), [471, 2014.042])

    def test_weather_service_two(self):
        self.assertEqual(self.weather_helper.get_station_max_fluctuation(), 425)

    def test_weather_service_three(self):
        self.assertEqual(self.weather_helper.get_station_max_fluctuation(start=2000.042, end=2003.458), 425)

if __name__ == '__main__':
    unittest.main()