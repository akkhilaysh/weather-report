import os
import sqlite3
import pandas as pd

def processDB():
    db_name = 'data.db'

    # Remove an already existing database
    try:
        os.remove(db_name)
    except FileNotFoundError:
        pass

    return db_name

def createDB(file, db_name):
    fp = open(file)
    connection = sqlite3.connect(db_name)
    chunksize = 10 ** 5

    print(f'\n1. Processing the csv file data.csv to store data to a database in chunks of {chunksize}..')

    for chunk in pd.read_csv(fp, chunksize=chunksize):
        # Append all rows in chunks to a new database table, which we name 'weather':
        chunk.to_sql('weather', connection, if_exists='append', index=False)

    print(f"2. Sqlite db named {db_name} created to store the data")

    # Creating an Index on the column station_id
    # This is done once during initialization

    print("3. Creating an index on the station_id column.")
    with connection:
        cursor = connection.cursor()
        cursor.execute('CREATE INDEX station_idx ON weather(station_id);')

    print("4. Closing the Connection to the DB as initial processing is done.\n\n")
    connection.close()