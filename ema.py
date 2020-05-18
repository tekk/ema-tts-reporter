#!/bin/python3
import requests, gtts, bs4, configparser
from metar import Metar

BASE_URL = "http://tgftp.nws.noaa.gov/data/observations/metar/stations"
config = configparser.ConfigParser()

def translator(txt):
    s = "The quick brown fox jumps over the lazy dog"
    for r in (
        ("brown", "red"),
        ("lazy", "quick")):
        s = s.replace(*r)
    

def main():
    config.read('ema.ini')
    airport = config['DEFAULT']['Airport']
    lang = config['DEFAULT']['Language']
    url = "%s/%s.TXT" % (BASE_URL, airport)
    req = requests.get(url).text
    for line in req.splitlines():
        if not isinstance(line, str):
            line = line.decode()  # convert Python3 bytes buffer to string
        if line.startswith(airport):
            report = line.strip()
            obs = Metar.Metar(line)
            print(obs.string())
            break

if __name__ == "__main__":
    main()
