from gtts import gTTS
import playsound
import pyttsx3
import speech_recognition as sr
import os
import cv2
from time import sleep

def speak(text):
    txt = gTTS(text = text,lang="en")
    file_name = "voice.mp3"
    txt.save(file_name)
    playsound.playsound(file_name)
    os.remove(os.path.join(os.getcwd(),file_name))


def speak2(text):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate',170)
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.say(text)
    engine.runAndWait()

def command():
    r1 =sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning...")
        r1.pause_threshold = .8
        r1.energy_threshold = 8000
        audio = r1.listen(source)
    try:
        print("Recognizing...")
        query = r1.recognize_google(audio, language ='en-in')
        print("user said:",query)
    except:
        speak("sorry sir ,i dont understand that can you speak it again")
        return "None"
    return query
