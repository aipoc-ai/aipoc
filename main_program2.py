from main_program import command,speak
from play_audio import play_music_func
from time import sleep

while True:
    speak("hello sir what do you want?")
    x = command()
    if x in "play music":
        speak("please tell me song?")
        query = command()
        t = play_music_func(query)
        sleep(20)
    elif x in "exit":
        break
    else:
        try:
            t.kill()
        except:
            speak("no music is playing")