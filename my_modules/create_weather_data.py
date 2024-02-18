# Author: Ofek Malul
# Date: 5/11/2023

from flask import redirect
import requests
from datetime import datetime


KEY = 'UQR46ZB6953HCZWEMSNVFLN2M'
URL = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/'


def convert_date_to_day_of_week():
    """Converts dates to days of the week"""
    week_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_of_the_week = datetime.now().weekday()
    week_list = week_list[day_of_the_week:] + week_list[:day_of_the_week]
    return week_list


def icon_generator(icon):
    """ Converts api icons to font awsome icons"""
    if icon == "rain":
        return "cloud-rain"
    if icon == "snow":
        return "snowflake"
    if icon == "fog":
        return "smog"
    if icon == "cloudy":
        return "cloud"
    if icon == "partly-cloudy-day" or icon == "clear-day":
        return "sun"
    if icon == "partly-cloudy-night" or icon == "clear-night":
        return "moon"
    return 'sun'


def weather_data_dict(city):
    """ calling weather api and returning filtered information to app.py or returning error in case of an error """
    week_list = convert_date_to_day_of_week()
    try:
        response = requests.get(f'{URL}{city}/next7days?unitGroup=metric&key={KEY}&contentType=json')
        response.raise_for_status()

        data = response.json()
        location = data['resolvedAddress']
        current_temp = data['days'][0]['temp']

        data_dict = {}
        for i in range(0, 7):
            day = data['days'][i]
            icon = day['icon']
            icon = icon_generator(icon)

            data_dict[i] = [{"day": week_list[i]}, {"temp": day['temp']}, {"humid": day['humidity']},
                            {"day": day['hours'][0]['temp']},
                            {"night": day['hours'][13]['temp']},
                            {"icon": icon}]
        return data_dict, location, current_temp
    except requests.exceptions.RequestException as error:
        error = str(error)
        remove_after = error.index(":")
        error = error[:remove_after]

        return {"error": error}
