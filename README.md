# weather-cli

## Configure
* Get your OpenWeatherMap API key with your city from openweathermap.org.
* Create `.env` file:
```
OPENWEATHERAPI=http://api.openweathermap.org/YOUR_API_KEY
```

## Usage
* Start script `./weathercli.py` with argument `--help` or `-h` (you may have to use `chmod +x weathercli.py`).
* Flag `-r` or `--request` is required always to connect with API.

Example usage:
```
./weathercli.py -r --temp
```
Output:
```
5.0
```

