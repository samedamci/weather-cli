#!/usr/bin/env python3

import os

import requests
from dotenv import load_dotenv
from requests.exceptions import ConnectionError

from arguments import args

load_dotenv()
APIKEY = os.getenv("OPENWEATHERAPI")


if args.request:
    try:
        response = requests.get(APIKEY)

        if args.temp:
            temp = float(round(response.json()["main"]["temp"] - 273.15, 1))
            print(temp)

        elif args.tmax:
            temp_max = float(
                round(response.json()["main"]["temp_max"] - 273.15, 1))
            print(temp_max)

        elif args.tmin:
            temp_max = float(
                round(response.json()["main"]["temp_min"] - 273.15, 1))
            print(temp_max)

        elif args.pressure:
            pressure = response.json()["main"]["pressure"]
            print(pressure)

        elif args.humidity:
            humidity = response.json()["main"]["humidity"]
            print(humidity)

        elif args.wind:
            wind = response.json()["wind"]["speed"]
            print(wind)

        elif args.clouds:
            clouds = response.json()["weather"][0]["description"]
            print(clouds)

        elif args.coords:
            coords_lon = response.json()["coord"]["lon"]
            coords_lat = response.json()["coord"]["lat"]
            print("lon", coords_lon)
            print("lat", coords_lat)

    except ConnectionError:
        print("E01: Failed to connect with OpenWeatherMap API.")
