from main_program import command,speak,speak2
from play_audio import play_music_func
from time import sleep
from ques_ans import get_ans
from get_weather import get_weather
from remove_stop_words import remove_words
from basic_question import name_owner
from send_mail import mail
while True:
    try:
        speak2("     Yes    sir?")
        x = command()
        x = x.lower()
        #play music
        if ("play music" in x) or ("play song" in x):
            speak2("please tell me song?")
            query = command()
            t = play_music_func(query)
        elif "play" in x:
            music = list(x.split(' '))
            music.remove("play")
            t = play_music_func(" ".join(music))

        
        #get ans
        elif list(x.split(' '))[0] in ['what','who','tell','whose']:
            if ("weather" in x) or ("temperature" in x):
                try:
                    city_name = remove_words(x)
                    temperature,list_ = get_weather(str(city_name))
                    speak2("the temperature of "+str(city_name)+ "is "+str(temperature)+" at "+str(list_[0])+" and the weather is "+str(list_[1])+".")
                except:
                    speak2("i don't understand the name of the city please ask again?")
            elif ("my name" in x) or ("your ownwer" in x):
                x = name_owner()
                speak2(x)
            else:
                speak2(get_ans(x))

        elif "wait" in x: 
            speak2("ok sir?")
            sleep(60)

        elif "send mail" in x:
            mail()

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
                speak2("no music is playing. I can play music for you only you have to say play music aipoc")
        
        else:
            speak2("I am learning this right now?")

    except:
        speak2("hello i am aipoc")
        speak2("there is no internet connection please connect me?")
        break