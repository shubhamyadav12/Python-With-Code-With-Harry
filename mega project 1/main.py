import speech_recognition as sr
import webbrowser
import pyttsx3


recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source, timeout=2)
        print("recognizing...")

    #recognise speech using sphinx

        try:
           command = ("jarvis thinks you said" + r.recognize_google(audio))
           print(command)

        except sr.UnknownValueError:
            print("jarvis could not understand audio")

        except Exception as e:
            print("error; {0}".format(e))   