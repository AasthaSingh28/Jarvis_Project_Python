import speech_recognition as sr
import webbrowser
import pyttsx3

#recognizer object
recognizer = sr.Recognizer()
ttsx = pyttsx3.init()

#speech to text func
def speak(text):
    ttsx.say(text)
    ttsx.runAndWait()

#command processing func
def processCommand():
    pass

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    #listen for the wake word "Jarvis"
    #obtain audio from the microphone
    r = sr.Recognizer()
    

    #recognize speech using Sphinx
    print("Recognizing...")
    try:
        with sr.Microphone() as source:
           print("Listening...")
           audio = r.listen(source, timeout=2, phrase_time_limit=1)
        word = r.recognize_google(audio)
        if(word.lower()== "Jarvis"):
            speak("Yah,how can I help you?")
            #listen for command
            with sr.Microphone() as source:
               print("Activated Jarvis...")
               audio = r.listen(source)
               command = r.recognize_google(audio)

               processCommand()

    except Exception as e:
        print("Error; {0}".format(e))
