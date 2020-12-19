#!/usr/bin/python3
import requests, gtts, configparser, gpiozero, os, time
from metar import Metar
from google.cloud import texttospeech

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/opt/ema-tts-reporter/credentials.json"

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
            client = texttospeech.TextToSpeechClient()
            input_text = texttospeech.SynthesisInput(text=text)
            voice = texttospeech.VoiceSelectionParams(
                language_code="sk-SK", ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
            )
            audio_config = texttospeech.AudioConfig(
                audio_encoding=texttospeech.AudioEncoding.MP3
            )
            response = client.synthesize_speech(
                request={"input": input_text, "voice": voice, "audio_config": audio_config}
            )
            # The response's audio_content is binary.
            with open("ema.mp3", "wb") as out:
                out.write(response.audio_content)
                print('Audio content written to file "ema.mp3"')
            #tts = gtts.gTTS(text, lang=language)
            #tts.save('ema.mp3')
            ptt.on()
            time.sleep(0.5)
            os.system('play -q roger.wav')
            os.system('play -q ema.mp3')
            ptt.off()
            break

if __name__ == "__main__":
    main()
