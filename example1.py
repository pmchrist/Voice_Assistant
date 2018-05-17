#!/usr/bin/env python3
# Requires PyAudio and PySpeech.
 
import speech_recognition as sr
from time import ctime
import time
import os
import random
import threading
from gtts import gTTS

def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")
 
def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source,0,3.5)
 
    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
 
    return data
 
#GlobalVariableFor-RandomBlubbing()
ImSorry=False

def jarvis(data):
    
    #BasicStuff
    if "how are you" in data:
        speak("I am fine")
 
    if "what time is it" in data:
        speak(ctime())
 
    if "where is" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on dude, I will show you where " + location + " is.")
        os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")
   
    #TalkingInParallell
    if "Drake is talking" in data:
        T=threading.Thread(target=Random_Blubbing)
        T.start()

    if "I'm sorry" in data:
        global ImSorry
        ImSorry=True
        speak("Ok, Let's continue")
  
    #TwitterClient
    if "follow me" in data:
        os.system("chromium-browser https://twitter.com/intent/follow?user_id=2310106205")

    if "tweet" in data:
        data = data.split(" ")
        CurrentTweet = data[1:len(data)]
        speak("Hold on dude, I will tweet it for you")
        os.system("chromium-browser https://twitter.com/intent/tweet?text=%s" % CurrentTweet)

    #BasicCalculator
    if "calculate" in data:
        data = data.split(" ")
        A = float(data[1])
        Operator = data[2]
        B = float(data[3])  
        if Operator == "+":
            Result=A+B
            speak("The result is: %.f" % (Result))
        if Operator == "-":
            Result=A-B
            speak("The result is: %.f" % (Result))
        if Operator == "x":
            Result=A*B
            speak("The result is: %.f" % (Result))
        if Operator == "/":
            Result=A/B
            speak("The result is: %.2f" % (Result))

#NUFF_SAID
def Random_Blubbing():
    global ImSorry
    ImSorry=False
    Phrase=0
    while not ImSorry:
        time.sleep(1)
        Phrase=random.randint(0,2)
        if (Phrase==0):
            speak("Will you stop talking?")
        if (Phrase==1):
            speak("Are you sure will stop?")
        if (Phrase==2):
            speak("Do you get your mistake?")   


# initialization
time.sleep(2)
speak("Hi dude, what can I do for you?")
while 1:
    data = recordAudio()
    jarvis(data)