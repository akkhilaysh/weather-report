# weather-report
Backend service to read data from a csv, create a database and output data for some scenarios


# Getting Started:

## Run using Docker

```bash
git clone https://github.com/akkhilaysh/weather-report.git
```

```bash
cd weather-report
```

## Important Step: Add into this folder the csv file data.csv containing weather data.

```bash
docker build -t weather-report .
```

```bash
docker run weather-report
```

The program will then run and print the outputs accordingly.


## Running Locally

```bash
git clone https://github.com/akkhilaysh/weather-report.git
```

```bash
cd weather-report
```

## Important Step: Add into this folder the csv file data.csv containing weather data.

```bash
pip install -r requirements.txt
```

```bash
python main.py data.csv
```

The program will then run and print the outputs accordingly.


## Tests

The repository also contains a test file "test_weather.py" that contains basic tests written against a test database provided in this repository.


## Authors

Akkhilaysh Shetty
