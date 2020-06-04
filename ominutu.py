#!/usr/bin/python3
import gpiozero, configparser, os, time
from metar import Metar

config = configparser.ConfigParser()

def main():
    config.read('ema.ini')
    airport = config['DEFAULT']['Airport']
    language = config['DEFAULT']['Language']
    port = config['DEFAULT']['PTT-Pin']
    ptt = gpiozero.LED(port)
    ptt.on()
    time.sleep(0.25)
    os.system('play -q ominutu.mp3')
    ptt.off()


if __name__ == "__main__":
    main()
