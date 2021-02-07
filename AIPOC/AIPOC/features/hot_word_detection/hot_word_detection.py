import speech_recognition as sr
import re


class Error(Exception):
    """Base class for other exceptions"""
    pass


class DefaultFileNotFound(Error):
    """Raised when the Default File Not Found"""
    pass


def hot_word_detection(lang='en'):
    """
    Hot word (wake word / background listen) detection
    What is Hot word detection?
    ANSWER: Hot word listens for specific key words chosen to activate the “OK Google” voice interface. ...
    Voice interfaces use speech recognition technologies to allow user input through spoken commands.
    You can set your custom HOT WORD just by calling setup(). Your bot_name is your Hot word
    :param lang: str
        default 'en'
    :return: Bool, str
        status, command
    """

    bot_name = ["ipog","poke","i pok","epoch","iphone","i pop","pok","pop","ipod","ipop"]

    while(True):
        try:
            r = sr.Recognizer()
        
            with sr.Microphone() as source:
                print("Background listening")
                r.pause_threshold = 1
                r.adjust_for_ambient_noise(source,duration=0.8)
                audio = r.listen(source)
                command = r.recognize_google(audio, language=lang).lower()
                k = 0
                for i in bot_name:
                    if i in command:
                        k=1
                
                if k==1:
                    print("Waking up...")
                    querywords = command.split()

                    resultwords  = [word for word in querywords if word.lower() not in bot_name]
                    command = ' '.join(resultwords)

                    return True, command
                else:
                    print(command)

        except Exception:
            pass


if __name__ == '__main__':
    hot_word_detection()
