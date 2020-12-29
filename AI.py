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
engine.setProperty("voice", voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()
    print(text)


def greet():
    time = int(datetime.datetime.now().hour)
    if