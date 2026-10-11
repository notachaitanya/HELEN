import pyttsx3 

def speak(text):
    text_speach = pyttsx3.init()
    text_speach.say(text)
    text_speach.runAndWait()