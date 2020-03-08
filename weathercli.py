#!/usr/bin/env python3

import requests, argparse, os
from dotenv import load_dotenv

load_dotenv()
APIKEY = os.getenv("OPENWEATHERAPI")

parser = argparse.ArgumentParser()
parser.add_argument("-r", "--request", help="send api request", action="store_true")
parser.add_argument("-t", "--temp", help="get your city temperature (*C)", action="store_true")
parser.add_argument("-p", "--pressure", help="get pressure (hPa)", action="store_true")
parser.add_argument("--humidity", help="get humidity (percents)", action="store_true")
parser.add_argument("--wind", help="get wind speed", action="store_true")
parser.add_argument("--clouds", help="get info about clouds", action="store_true")
parser.add_argument("--tempmax", help="get info about max temperature (*C)", action="store_true")
parser.add_argument("--tempmin", help="get info about min temperature (*C)", action="store_true")
parser.add_argument("--coords", help="get info about geo coords", action="store_true")

args = parser.parse_args()

if args.request:
    response = requests.get(APIKEY)

if args.temp:
    temp = float(round(response.json()['main']['temp']-273.15, 1))
    print(temp)

if args.tempmax:
    temp_max = float(round(response.json()['main']['temp_max']-273.15, 1))
    print(temp_max)

if args.tempmin:
    temp_max = float(round(response.json()['main']['temp_min']-273.15, 1))
    print(temp_max)

if args.pressure:
    pressure = response.json()['main']['pressure']
    print(pressure)

if args.humidity:
    humidity = response.json()['main']['humidity']
    print(humidity)

if args.wind:
    wind = response.json()['wind']['speed']
    print(wind)

if args.clouds:
    clouds = response.json()['weather'][0]['description']
    print(clouds)

if args.coords:
    coords_lon = response.json()['coord']['lon']
    coords_lat = response.json()['coord']['lat']
    print("lon", coords_lon)
    print("lat", coords_lat)
