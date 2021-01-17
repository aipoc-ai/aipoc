from gtts import gTTS
import playsound
import pyttsx3
import speech_recognition as sr
import os
from time import sleep
import pygame
from play_audio import play_music_func

def speak(text):
    txt = gTTS(text = text,lang="en")
    file_name = "voice.mp3"
    txt.save(file_name)

    pygame.mixer.init()
    pygame.mixer.music.load("myFile.wav")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue


def speak2(text):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate',170)
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.say(text)
    engine.runAndWait()

def command():
    while True:
        try:
            r1 =sr.Recognizer()
            with sr.Microphone() as source:
                print("Listning...")
                r1.pause_threshold = .8
                r1.energy_threshold = 8000
                audio = r1.listen(source)
            print("Recognizing...")
            query = r1.recognize_google(audio, language ='en-in')
            print("user said:",query)
            break
        except:
            speak("sorry sir ,i dont understand that can you speak it again")
    return query

