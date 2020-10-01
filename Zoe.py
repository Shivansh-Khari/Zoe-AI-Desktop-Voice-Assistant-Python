import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia     #pip install pyaudio
import webbrowser
import os
import smtplib
from pygame import mixer

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<6:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I Am Zoe. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@email.com', 'your-password')
    server.sendmail('youremail@email.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'zoe' in query:
            print("Hello Sir. How Are You?")
            speak("Hello Sir. How Are You?")

        elif 'i am good' in query:
            print("Thats great")
            speak('Thats great')

        elif 'shut up' in query:
            print("Sorry Sir, Are You Upset? You Can Talk To Me")
            speak('Sorry Sir, Are You Upset? You Can Talk To Me')

        elif 'i am fine' in query:
            print("Thats great")
            speak('Thats great')

        elif 'main theek hoon' in query:
            print("badiya")
            speak('badiya')

        elif 'kaise ho' in query:
            print("main badiya")
            speak('main badiya')

        elif 'what you can do' in query:
            print("i can do a search on wikipedia if you like to")
            speak('i can do a search on wikipedia if you like to')

        elif 'tum kya kar sakti ho' in query:
            print("main wikipedia par kuch dhund sakti hoon")
            speak('main wikipedia par kuch dhund sakti hoon')
        
        elif 'website' in query:
            print("Which Website?")
            speak('Which Website?')
            website = takeCommand()
            webbrowser.open(website)

        elif 'play music' in query:
            speak('Playing Music ')
            music_dir = 'full_path_of_song'
            mixer.init()
            mixer.music.load(music_dir)
            mixer.music.play()
        
        #stop music   
        elif 'stop music' in query:
            mixer.music.stop()
            
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)    
            speak(f"Sir, the time is {strTime}")

        elif 'chrome' in query:
            codePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\Chrome.exe"
            os.startfile(codePath)

        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak('Enter The Email Address')
                print('Enter The Email Address')
                to = input()
                sendEmail(to, content)
                speak("Email has been sent!")
                print("Email has been sent!")
            except Exception as e:
                print(e) 
                speak("Sorry Sir, I Am Not Able To Send Email")
                print("Sorry Sir, I Am Not Able To Send Email")
                
        elif 'turn off' in query:
                speak('Good Bye Master')
                break
