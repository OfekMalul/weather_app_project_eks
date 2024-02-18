# Author: Ofek Malul
# Date: 8/2/2024

from flask import Flask, render_template, request, redirect, url_for
from my_modules import create_weather_data
from datetime import datetime
from dotenv import load_dotenv
import os
import json

app = Flask(__name__)

def save_query_to_file(query):
    date = datetime.now().strftime('%x %X')
    data = {'city': query, 'date': []}

    file_path = '/tmp/data.json'

    # Trying to get data from file
    try:
        with open(file_path, 'r') as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = []
    
    query_exists = False
    for item in existing_data:
        if item['city'] == query:
            item['date'].append(date)
            query_exists = True
            break
    
    # if no similar query took place
    if not query_exists:
        data['date'].append(date)
        existing_data.append(data) 


    with open(file_path, 'w') as file:
        json.dump(existing_data, file, indent=4)
    return

load_dotenv()
background_color = os.getenv('BACKGROUND_COLOR')
@app.route('/', methods=["GET"])
def index():
    """Renders the index template as our home page"""
    return render_template('index.html', background_color=background_color)


@app.route('/weather', methods=["POST"])
def weather():
    """ Getting city from user and getting data from API. if error we are redirecting to /error else we are
        rendering weather template with data given by the api
    """
    user_city = request.form.get('cityName')
    if user_city == "":
        user_city = "tel aviv"

    response = create_weather_data.weather_data_dict(user_city)
    if "error" in response:
        error = str(response["error"])
        return redirect(url_for("error", message=error))
    else:
        weather_data, location, temp = response
        save_query_to_file(user_city)
        return render_template('weather.html', background_color=background_color, weather_data=weather_data, location=location, temp=temp)

@app.route('/history')
def json_data():
    file_path = '/tmp/data.json'
    IS_DATA_EXIST = False
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            IS_DATA_EXIST = True
    except FileNotFoundError:
        data = []
    if IS_DATA_EXIST:
        return render_template('history.html', background_color=background_color, data=data)
    return render_template('no-data-history.html', background_color=background_color, data=data)


@app.route('/error/<message>')
def error(message):
    """rendering error template with error message given by weather() error"""
    return render_template("error_page.html", background_color=background_color, error=message)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9090)
