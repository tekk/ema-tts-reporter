#!/usr/bin/python3
import requests, gtts, configparser, gpiozero, os, time
from metar import Metar

BASE_URL = "http://tgftp.nws.noaa.gov/data/observations/metar/stations"
config = configparser.ConfigParser()

def main():
    config.read('ema.ini')
    airport = config['DEFAULT']['Airport']
    language = config['DEFAULT']['Language']
    port = config['DEFAULT']['PTT-Pin']
    ptt = gpiozero.LED(port)
    url = "%s/%s.TXT" % (BASE_URL, airport)
    req = requests.get(url).text
    for line in req.splitlines():
        if line.startswith(airport):
            obs = Metar.Metar(line)
            text = obs.string()
            print('-------------------')
            print(text)
            tts = gtts.gTTS(text, lang=language)
            tts.save('ema.mp3')
            ptt.on()
            time.sleep(0.25)
            os.system('play -q roger.wav')
            os.system('play -q ema.mp3')
            ptt.off()
            break

if __name__ == "__main__":
    main()
