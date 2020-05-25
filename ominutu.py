#!/usr/bin/python3
import requests, gtts, gpiozero, configparser, os
from metar import Metar

config = configparser.ConfigParser()

def main():
    config.read('ema.ini')
    airport = config['DEFAULT']['Airport']
    language = config['DEFAULT']['Language']
    port = config['DEFAULT']['PTT-Pin']
    ptt = gpiozero.LED(port)
    ptt.off()
    ptt.on()
    os.system('play -q ominutu.mp3')
    ptt.off()


if __name__ == "__main__":
    main()
