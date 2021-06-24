from db.weather_database import WeatherDatabase

class WeatherHelper:
    def __init__(self, test=False):
        self.weather_database = WeatherDatabase(test)

    def get_station_date_with_lowest_temp(self):
        station_id, date = self.weather_database.get_one_db_temperature_c_desc()

        return [station_id, date]

    def get_station_max_fluctuation(self, start=None, end=None):
        max_station = 0
        max_fluctuation = 0

        data = self.weather_database.get_many_db_date_in_asc_range(start, end)
        dict = {}

        for station, temperature in data:
            if station not in dict:
                dict[station] = []
            dict[station].append(temperature)

        for station in dict:
            station_fluctuation = self.fluctuation(dict[station])

            total_fluctuation = 0
            # Iteration of consecutive fluctuation values and calculating the sum to get the total fluctuation for a station.
            for _ in station_fluctuation:
                total_fluctuation += _

            # Updating maximum fluctuation value and the station with the maximum fluctuation.
            if total_fluctuation > max_fluctuation:
                max_fluctuation = total_fluctuation
                max_station = station

        # print(f'The station with Maximum fluctuation is {max_station} and it is {max_fluctuation}')
        return max_station

    def fluctuation(self, A):
        prev = A[0]
        for el in A:
            yield abs(el - prev)
            prev = el