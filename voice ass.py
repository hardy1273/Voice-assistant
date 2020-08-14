import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good evening")
    

    speak("I am your assistant Hardit, How may i help you?")
print("It is",datetime.datetime.now())

wishMe()

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing")
        query=r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please.......")
        return "None"
    return query

if __name__=="__main__":
    while True:
        query=takeCommand().lower()

        if 'Wikipedia' in query:
            speak("Searching Wikipedia..")
            query=query.replace("Wikipedia","")
            results=wikipedia.summary(query, sentences=2)
            speak("Wikipedia Says")
            print(results)
            speak(results)
        elif 'youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'google' in query:
            webbrowser.open("google.com")
        
        elif 'stackoverflow' in query:
            webbrowser.open('stackoverflow.com')
        
        elif 'coffee' in query:
            webbrowser.open("https://www.zomato.com/ncr/restaurants/coffee")
        
        elif 'order food' in query:
            webbrowser.open("https://www.zomato.com/ncr/order-food-online?delivery_subzone=239")
           
        elif 'play music' in query:
            music_dir='C:\\Users\\hardi\\Downloads\\Yandhi Fulls-20200514T091700Z-001\\Yandhi Fulls'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        
        elif 'time' in query:
            strTime= datetime.datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is",strTime)