import features.hot_word_detection.hot_word_detection as wake_word

class AIPOCAI:
    def __init__(self):
        pass

    def hot_word_detect(self, lang='en'):
        """
        Hot word (wake word / background listen) detection
        :param lang: str
            default 'en'
        :return: Bool, str
            status, command
        """
        try:
            status, command = wake_word.hot_word_detection(lang=lang)
            print(status, command)
        except Exception as e:
            status = command = False
        return status, command

    def mic_input(self, lang='en'):
        pass

Ai = AIPOCAI()
status,command = Ai.hot_word_detect()
