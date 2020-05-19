#!/bin/python3
import requests, gtts, bs4, configparser, pygame
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
        if not isinstance(line, str):
            line = line.decode()  # convert Python3 bytes buffer to string
        if line.startswith(airport):
            report = line.strip()
            obs = Metar.Metar(line)
            text = obs.string()
            tts = gtts.gTTS(text, lang=language)
            tts.save('ema.mp3')
            pygame.mixer.init()
            pygame.mixer.music.load("ema.mp3")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() == True:
                continue
            break

if __name__ == "__main__":
    main()
