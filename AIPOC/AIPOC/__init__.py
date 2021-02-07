import features.hot_word_detection.hot_word_detection as wake_word
import features.speaker.speaker as speaker

class AIPOCAI:
    def __init__(self):
        pass

    def hot_word_detect(self, lang='en'):
        try:
            status, command = wake_word.hot_word_detection(lang=lang)
            print(status, command)
        except Exception as e:
            status = command = False
        return status, command

    def mic_input(self, lang='en'):
        pass

while(True):
    Ai = AIPOCAI()
    status,command = Ai.hot_word_detect()
    if status:
        if len(list(command.split(" ")))<2:
            speaker.speak("Yes sir")
            query = speaker.command()
            print("ok1")
        else:
            query = command
            print("ok")
        

