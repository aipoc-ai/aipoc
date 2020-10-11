import smtplib, ssl
from text_to_voice import speak,command

def mail():
    speak("Who do you want to mail?")
    while True:
        receiver_name = command()
        speak("you said"+receiver_name+"."+"is it ok")
        speak("Iss it okk")
        permission = command()
        if "yes" in permission:
            break
        else:
            speak("say again receiver name")
    while True:
        speak("what is the message")
        message = command()
        speak("i am repeating the message."+message+"Is it ok?")
        permission = command()
        if "yes" in permission:
            break
        else:
            speak("say again receiver name") 

    sender_mail = "email"
    passw = "password"   
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls() 
    s.login(sender_mail, passw) 
    s.sendmail(sender_mail,"abhishek.sharmar112@gmail.com", message) 
    s.quit() 
    speak("mail send")