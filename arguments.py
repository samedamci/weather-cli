#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(prog="weather-cli")


class Arg:
    def __init__(self, full, help, short, isrequired=False, action="store_true"):
        self.short = short
        self.full = full
        self.help = help
        self.action = action
        self.isrequired = isrequired

        parser.add_argument(short, full, help=help, action=action, required=isrequired)


Arg("--request", "send API request", "-r", True)
Arg("--temp", "get temperature (*C)", "-t")
Arg("--pressure", "get pressure (hPa)", "-p")
Arg("--humidity", "get humidity (percents)", "-u")
Arg("--wind", "get wind speed (m/s)", "-w")
Arg("--clouds", "get clouds info", "-c")
Arg("--tmax", "get max temperature (*C)", "-x")
Arg("--tmin", "get min temperature (*C)", "-m")
Arg("--coords", "get min temperature (*C)", "-y")


args = parser.parse_args()
