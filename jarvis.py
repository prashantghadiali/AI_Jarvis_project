import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    
    else:
        speak("Good Evening!")
    
    speak("I am Jarvis. How may i help you?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as sourse:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(sourse)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print("User said: ", query)
        
    except Exception as e:
        # print(e)
        print('Say that again please...')
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            speak("Searching on wikipidia...")
            query = query.replace("wikipidia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipidia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'profile' in query:
            webbrowser.open("prashantghadiali.wordpress.com")
