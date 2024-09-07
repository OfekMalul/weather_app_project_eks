# Author: Ofek Malul
# Date: 3/19/2024

FROM python:3.11.9-slim-bullseye

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 9090

CMD python app.py
