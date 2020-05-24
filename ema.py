#!/usr/bin/python3
import requests, gtts, bs4, configparser, playsound
from metar import Metar

BASE_URL = "http://tgftp.nws.noaa.gov/data/observations/metar/stations"
config = configparser.ConfigParser()

def main():
    config.read('ema.ini')
    airport = config['DEFAULT']['Airport']
    language = config['DEFAULT']['Language']
    url = "%s/%s.TXT" % (BASE_URL, airport)
    req = requests.get(url).text
    for line in req.splitlines():
        if line.startswith(airport):
            obs = Metar.Metar(line)
            obs = Metar.Metar(
                "METAR KEWR 111851Z VRB03G19KT 2SM R04R/3000VP6000FT TSRA BR FEW015 "
                "BKN040CB BKN065 OVC200 22/22 A2987 RMK AO2 PK WND 29028/1817 WSHFT "
                "1812 TSB05RAB22 SLP114 FRQ LTGICCCCG TS OHD AND NW-N-E MOV NE "
                "P0013 T02270215")
            text = obs.string()
            print(text)
            tts = gtts.gTTS(text, lang=language)
            tts.save('ema.mp3')
            playsound.playsound('ema.mp3', True)
            break

if __name__ == "__main__":
    main()