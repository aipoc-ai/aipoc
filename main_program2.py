import gtts
import playsound
import speech_recognition as sr
import os
def speak(text,count):
    txt = gTTS(text = text,lang="en")
    file_name = "voice"+str(count)+".mp3"
    txt.save(file_name)
    playsound.playsound(file_name)

