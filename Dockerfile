FROM python:3.9.6-slim-bullseye

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 9090

USER weather_user

CMD python app.py
