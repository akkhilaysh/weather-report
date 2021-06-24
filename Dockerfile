FROM python:3.8.2-slim

ADD . .

RUN pip install -r requirements.txt

CMD ["python", "./main.py", "data.csv"]