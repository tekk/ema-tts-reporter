#!/usr/bin/python3
import requests, gtts, gpiozero, configparser, playsound
from metar import Metar

BASE_URL = "http://tgftp.nws.noaa.gov/data/observations/metar/stations"
config = configparser.ConfigParser()

def main():
    config.read('ema.ini')
    airport = config['DEFAULT']['Airport']
    language = config['DEFAULT']['Language']
    port = config['DEFAULT']['PTT-Pin']
    ptt = gpiozero.LED(port)
    ptt.off()
    url = "%s/%s.TXT" % (BASE_URL, airport)
    req = requests.get(url).text
    for line in req.splitlines():
        if line.startswith(airport):
            obs = Metar.Metar(line)
            text = obs.string()
            print(text)
            tts = gtts.gTTS(text, lang=language)
            tts.save('ema.mp3')
            ptt.on()
            playsound.playsound('ema.mp3', True)
            ptt.off()
            break

if __name__ == "__main__":
    main()
