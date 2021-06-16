"""
Code borrowed from: https://www.youtube.com/watch?v=x8xjj6cR9Nc&ab_channel=TraversyMediaTraversyMediaVerified
"""
import speech_recognition as sr
import time
from time import ctime
import webbrowser
from gtts import gTTS
import playsound
import random
import os

r = sr.Recognizer()

def record_audio(ask=False):
    if ask:
        friday_speak(ask)
    with sr.Microphone() as source:
        audio = r.listen(source)
        voice_data = ""
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            friday_speak("Sorry, I did not get that")
        except sr.RequestError:
            friday_speak("Sorry, my speech service is down")
        return voice_data
def friday_speak(audio_string):
    tts = gTTS(text=audio_string, lang="en")
    r = random.randint(1, 1000000)
    audio_file = "audio-" + str(r) + ".mp3"
    tts.save(audio_file)
    print(audio_string)
    playsound.playsound(audio_file)
    os.remove(audio_file)
    
# sr does not recognize punctuations and uppercase letters
def respond(voice_data):
    if "what is your name" in voice_data:
        friday_speak("My name is Friday")
    if "what time is it" in voice_data:
        friday_speak(ctime())
    if "search" in voice_data:
        search = record_audio("What do you want to search for?")
        url = "https://google.com/search?q=" + search
        webbrowser.get().open(url)
        friday_speak("Here is what I found for %s" % search)
    if "find location" in voice_data:
        location = record_audio("What location are you looking for?")
        url = "https://google.com/maps/place/" + location + "/&amp;"
        webbrowser.get().open(url)
        friday_speak("Here is the location of %s" % location)
    if "exit" in voice_data:
        friday_speak("Goodbye!")
        raise SystemExit(0)

time.sleep(1)
friday_speak("How can I help you?")
while True:
    voice_data = record_audio()
    respond(voice_data)
        