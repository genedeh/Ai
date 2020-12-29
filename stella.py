import json
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
from pathlib import Path
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)


def speak(text):
    """speak function will pronoun the string which is passed to it"""
    engine.say(text)
    engine.runAndWait()
    print(text)


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
        print("LOADING...")
        command = recognizer.recognize_google(audio, language="en-un")
        print(f"user said: {command}")

    except Exception as e:
        speak(f"Please say that again")
        command = None
    return command


def GreetMe():
    """This is function will Greet you as for the current time"""
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak(f"Good morning {Name}")

    elif hour >= 12 and hour < 18:
        speak(f"Good afternoon {Name}")
    else:
        speak(f"Good Evening {Name}")


greeting = "I am stella, a AI technological companion, what is your name master, i will like to know your name."
speak(greeting)
print(greeting)
Name = takeCommand()
speak("say a password please")
Passcode = takeCommand()
GreetMe()
speak("How can i help you")
command = takeCommand()
if not "stop" == command.lower():
    if "tell me about you" in command.lower():
        speak("I am an intelligent interface, made by two geniuses, called Genesis and Hazzan, who created this smart technology, I can do many things that even crotana cannot do")
        print("I am an intelligent interface, made by two geniuses, called Genesis and Hazzan, who created this smart technology, I can do many things that even crotana cannot do")
    if "wikipedia" in command.lower():
        speak("Searching wikipedia...")
        command = command.replace("wikipedia", "")
        results = wikipedia.summary(command, sentences=2)
        speak(results)
    if "open google" in command.lower():
        url = "google.com"
        chrome_path = "c:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        webbrowser.get(chrome_path).open(url)
    if "open w3schools" in command.lower():
        url = "w3schools.com"
        chrome_path = "c:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        webbrowser.get(chrome_path).open(url)
    if "open stackoverflow" in command.lower():
        url = "stackoverflow.com"
        chrome_path = "c:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        webbrowser.get(chrome_path).open(url)
    if "open youtube" in command.lower():
        url = "youtube.com"
        chrome_path = "c:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        webbrowser.get(chrome_path).open(url)
    if "the time" in command.lower():
        Time = datetime.datetime.now().strftime("today's date is %D month %M year %Y")
        speak(f"{Name}, {Time}")
    if "play music" in command.lower() or "open music" in command.lower():
        songs_dir = r"C:\Users\Genesis\Documents\Sound recordings"
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir, songs[random.randint(0, 8)]))
    if "open desktop" in command.lower():
        desktop_dir = r"C:\Users\Genesis\Desktop"
        desktop = os.listdir(desktop_dir)
        speak(f"please only enter file name, {MASTER}")
        folder = takeCommand()
        os.startfile("C:\\Users\\Genesis\\Desktop\\" + folder)
    if "open maps" in command.lower():
        url = "https://www.google.ng/maps/"
        chrome_path = "c:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        webbrowser.get(chrome_path).open(url)
    if "launch drone" in command.lower():
        speak("where should we launch the drone")
        place = takeCommand()
        speak("to who should we launch the drone to")
        person = takeCommand()
        speak(f"launching drone number {random.randint(0, 10)}, and launching in {place} to {person}")
    if "shutdown" in command.lower():
        speak("shut down mode activate" + Name)
        print("shut down mode activate" + Name)
        print("LOCKING...")
        speak("shuting process finished")
        print("shuting process finished")
    if "activate security mode" in command.lower():
        speak("security mode activated" + Name)
        print("security mode activated" + Name)
        print("SECURING...")
        takeCommand()
    if "deactivate security mode" in command.lower():
        speak(f"please say your password {Name}")
        password = takeCommand()
        if password == Passcode:
            speak("security mode deactivated")
            print("security mode deactivated")
        else:
            speak("Intruder intruder intruder alert, locking paramiter  now, lockdown completed")
    if "switch on light" in command.lower():
        speak("Which light should i switch on")
        print("Which light should i switch on")
        light = takeCommand()
        if "front light" in light.lower():
            speak("switching on front light")
            print("switching on front light")
        if "back light" in light.lower():
            speak("switching on back light")
            print("switching on back light")
        if "left light" in light.lower():
            speak("switching on left light")
            print("switching on left light")
        if "right light" in light.lower():
            speak("switching on right light")
            print("switching on right light")
        if "All light" in light.lower():
            speak("switching on all light")
            print("switching on all light")
    if "switch off light" in command.lower():
        speak("Which light should i switch off")
        print("Which light should i switch off")
        light = takeCommand()
        if "front light" in light.lower():
            speak("switching off front light")
            print("switching off front light")
        if "back light" in light.lower():
            speak("switching off back light")
            print("switching off back light")
        if "left light" in light.lower():
            speak("switching off left light")
            print("switching off left light")
        if "right light" in light.lower():
            speak("switching off right light")
            print("switching off right light")
        if "All light" in light.lower():
            speak("switching off all light")
            print("switching off all light")
    if "open setting" in command.lower():
        speak("Which setting do you want to activate")
        print("Which setting do you want to activate")
        print(f"Name setting :{Name} Password setting: {Passcode}")
        setting_type = takeCommand()
        if "name setting" in setting_type.lower():
            speak("Change Name to:")
            print("Change Name to:")
            name = takeCommand()
            Name = name
        if "password setting" in setting_type.lower() or "passcode setting" in setting_type.lower():
            speak("Change Passcode to:")
            print("Change Passcode to:")
            passcode = takeCommand()
            Passcode = passcode
        else:
            speak(f"NO setting like that {Name}")
    if "order food" in command.lower():
        speak("What do you want to other")
        food = takeCommand()
        speak("how much")
        price = takeCommand()
        speak(f"how many {food} do you want to oder")
        num = takeCommand()
        url = "https://food.jumia.com.ng/?utm_source=jumia&utm_medium=mall&utm_campaign=venturebar" + food
        chrome_path = "c:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        webbrowser.get(chrome_path).open(url)
        speak(f"odering {num} {food} from Jumia")
    if "order appliance" in command.lower():
        speak("What do you want to order")
        appliance = takeCommand()
        speak("how much")
        price = takeCommand()
        speak(f"how many {appliance} do you want to order")
        num = takeCommand()
        url = "https://www.jumia.com.ng/" + appliance + "/"
        chrome_path = "c:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        webbrowser.get(chrome_path).open(url)
        speak(f"odering {num} {appliance} from Jumia")