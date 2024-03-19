# Author: Ofek Malul
# Date: 3/19/2024

FROM python:3.9.6-slim-bullseye

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 9090

USER weather_user

CMD python app.py
