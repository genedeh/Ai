import sys
import speech_recognition as sr
import datetime
import pyttsx3
import pyaudio
import wikipedia
import webbrowser
import os
import smtplib
import random
MASTER = "Genesis"
print("Initializing V.A")

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)


def speak(text):
    """speak function will pronoun the string which is passed to it"""
    engine.say(text)
    engine.runAndWait()


def wishMe():
    """This is function will wish you as for the current time"""
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good morning" + MASTER)

    elif hour >= 12 and hour < 18:
        speak("Good afternoon" + MASTER)
    else:
        speak("Good Evening" + MASTER)
    # speak("I am VA. How may I help you?")


def takeCommand():
    """This function will take command from the microphone"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listenging...")
        audio = recognizer.listen(source)

    try:
        print("RECOGNIZING...")
        query = recognizer.recognize_google(audio, language="en-un")
        print(f"user said: {query}\n")

    except Exception as e:
        speak("Please say that again")
        query = None
    return query
    

wishMe()
query = takeCommand()
if "hello" in query.lower():
    speak("I am doing okay," + MASTER + ",how are you doing")
    takeCommand()
    takeCommand()
if "quiet" in query.lower():
    speak(f"Okay {MASTER}")
    takeCommand()
    takeCommand() 
if "wikipedia" in query.lower():
    speak("Searching wikipedia...")
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    print(results)
    speak(results)
    takeCommand()
    takeCommand()

elif "open youtube" in query.lower():
    # webbrowser.open("youtube.com")
    url = "youtube.com"
    chrome_path = "c:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open(url)
    takeCommand()
    takeCommand()

elif "open google" in query.lower():
    # webbrowser.open("youtube.com")
    url = "google.com"
    chrome_path = "c:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open(url)
    takeCommand()
    takeCommand()

elif "open w3schools" in query.lower():
    # webbrowser.open("youtube.com")
    url = "w3schools.com"
    chrome_path = "c:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open(url)
    takeCommand()
    takeCommand()

elif "open stackoverflow" in query.lower():
    # webbrowser.open("youtube.com")
    url = "pypi.com"
    chrome_path = "c:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open(url)
    takeCommand()
    takeCommand()

elif "play music" in query.lower():
    songs_dir = r"C:\Users\Genesis\Documents\Sound recordings"
    songs = os.listdir(songs_dir)
    print(songs)
    os.startfile(os.path.join(songs_dir, songs[random.randint(0, 8)]))

elif "the time" in query.lower():
    Time = datetime.datetime.now().strftime("%D:%Y:%H:%M:%S")
    speak(f"{MASTER} the time is, {Time}")
    takeCommand()
    takeCommand()


elif "open file in desktop" in query.lower():
    desktop_dir = r"Desktop"
    desktop = os.listdir(desktop_dir)
    speak(f"please only enter file name, {MASTER}")
    folder = takeCommand()
    os.startfile(r"Desktop\"" + folder)

elif "open file in document" in query.lower():
    documents_dir = r"Documents"
    documents = os.listdir(documents_dir)
    speak(f"please only enter file name, {MASTER}")
    folder = takeCommand()
    os.startfile(r"Documents\"" + folder)

elif "open file in downloads" in query.lower():
    downloads_dir = r"Downloads"
    downloads = os.listdir(downloads_dir)
    speak(f"please only enter file name, {MASTER}")
    folder = takeCommand()
    os.startfile(r"Downloads\"" + folder)

elif "open file in pictures" in query.lower():
    pictures_dir = r"Pictures"
    pictures = os.listdir(pictures_dir)
    speak(f"please only enter file name, {MASTER}")
    folder = takeCommand()
    os.startfile(r"Pictures\"" + folder)

elif "open file in videos" in query.lower():
    Videos_dir = r"C:\Users\Genesis\Videos\Captures"
    Videos = os.listdir(Videos_dir)
    speak(f"please only enter file name, {MASTER}")
    folder = takeCommand()
    os.startfile(r"C:\Users\Genesis\Videos\Captures\"" + folder)    

# elif "open code" in query.lower():
#     vscode = r"C:\Users\Genesis\Downloads\VSCodeUserSetup-x64-1.36.1\Code.exe"
#     os.startfile(vscode)