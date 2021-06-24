import sys
from helper.weather_helper import WeatherHelper
from db.process_database import processDB, createDB

if len(sys.argv) <= 1:
    print('Please add the data.csv file, in the root folder, containing weather data as an argument.')
    exit(1)

if not sys.argv[1].endswith('.csv'):
    print('File should be of type .csv which contains the weather data.')
    exit(1)

file_name = sys.argv[1]
db_name = processDB()

connection = createDB(file_name, db_name)

weather_helper = WeatherHelper()

print("Starting Part 1..")
print("Return station_id, and date pair that reported the lowest temperature:\n")
print(f'Output [station_id, weather]: {weather_helper.get_station_date_with_lowest_temp()}')
print("Finished Part 1.\n\n")

print("Starting Part 2..")
print("Return the station_id that experienced the most amount of temperature fluctuation across "
      "all dates that it reported temperatures for:\n")
print(f'Output Station_id: {weather_helper.get_station_max_fluctuation()}')
print("Finished Part 2.\n\n")

print("Starting Part 3..")
start = 2000.042
end = 2003.458
print('Return the station_id that experienced the most amount of temperature fluctuation for any given range of dates.\n')
print(f'Output Station_id for range {start}-{end}: {weather_helper.get_station_max_fluctuation(start=start, end=end)}')
print("Finished Part 3.\n")


