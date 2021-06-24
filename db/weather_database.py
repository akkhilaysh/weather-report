import sqlite3

class WeatherDatabase:
    """sqlite3 database class that holds testers jobs"""
    __DB_LOCATION = "data.db"
    __TEST_DB_LOCATION = "test_data_10k.db"

    QUERIES = {
        "GET_COLDEST_STATION_DATA" :"SELECT station_id, date FROM weather ORDER BY temperature_c LIMIT 1",
        "GET_STATION_BY_ASC_DATE" : "SELECT station_id, temperature_c from weather ORDER BY date ASC;",
        "GET_STATION_BY_ASC_DATE_RANGE": f"SELECT station_id, temperature_c from weather where date BETWEEN :start AND :end ORDER BY date ASC;",
    }

    def __init__(self, test=False):
        """Initialize db class variables"""
        if test:
            self.__db_connection = sqlite3.connect(self.__TEST_DB_LOCATION)
        else:
            self.__db_connection = sqlite3.connect(self.__DB_LOCATION)

        self.cursor = self.__db_connection.cursor()


    def __del__(self):
        print("Closing DB Connection.\n")
        self.__db_connection.close()

    def process_data(self):
        pass

    def get_one_db_temperature_c_desc(self):
        return self.cursor.execute(self.QUERIES["GET_COLDEST_STATION_DATA"]).fetchone()

    def get_many_db_date_in_asc_range(self, start=None, end=None):
        if start and end:
            try:
                start = float(start)
                end = float(end)
            except ValueError:
                print("Expecting a date in the format \"year.time\" range for relavant data that you'd like to query!")
            self.cursor.execute(
                f"SELECT station_id, temperature_c from weather where date BETWEEN :start AND :end ORDER BY date ASC;",
                {'start': start, 'end': end})
        else:
            self.cursor.execute(self.QUERIES["GET_STATION_BY_ASC_DATE"])

        for row in self.cursor.fetchall():
            yield row


