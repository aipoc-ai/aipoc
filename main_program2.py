from main_program import command,speak
from play_audio import play_music_func
from time import sleep
from ques_ans import get_ans

while True:
    speak("Yes sir?")
    x = command()
    #play music
    if "(play music" in x ) or ("play song" in x):
        speak("please tell me song?")
        query = command()
        t = play_music_func(query)
    
    #get ans
    elif list(x.split(' '))[0] in ['what','who','tell','whose']:
        speak(get_ans(x))

    elif x in "exit":
        break
    elif x in "exit":
        break
    elif x in "exit":
        break
    elif x in "exit":
        break
    elif x in "exit":
        break
    elif x in "exit":
        break
    elif x in "exit":
        break
    elif x in "exit":
        break
    elif x in "exit":
        break
    elif x in "exit":
        break
    elif x in "exit":
        break
    elif x in "exit":
        break
    elif x in "exit":
        break
    elif x in "exit":
        break
    elif x in "exit":
        break
    elif ("stop music" in x) or ("stop song" in x):
        try:
            t.kill()
        except:
            speak("no music is playing. I can play music for you only you have to say play music aipoc")
    
    else:
        speak("I am learning this right know?")