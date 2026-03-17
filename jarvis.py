import speech_recognition as sr
import pyttsx3
import logging
import os
import datetime
import wikipedia
import webbrowser
import random
import subprocess


#Logging configuration
LOG_DIR="logs"
LOG_FILE_Name =  "application.log"

os.makedirs(LOG_DIR, exist_ok=True)
log_path=  os.path.join(LOG_DIR,LOG_FILE_Name)

logging.basicConfig(
    filename=log_path,
    format = "[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
    level=  logging.INFO
)

#Activating voice from our  system
engine= pyttsx3.init("sapi5")
engine.setProperty('rate',170)
voices=engine.getProperty("voices")
engine.setProperty('voice',voices[1].id)

#This is speak function
def speak(text):
    """"This function converts text to voice

    Args:
        text
    Returns:
       voice
    """
    engine.say(text)
    engine.runAndWait()
    
# This function recognize the speech and convert it to text

def takeCommand():
    """This function takes command & recognize

    Returns:
        text as query
    """
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio= r.listen(source)
    try:
        print("recognizing...")
        query=  r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        logging.info(e)
        print("say that again please")
        return "None"
    
    return  query
    
def greetings():
    hour=(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!How are you doing?")
    elif hour>=12 and hour<18:
        speak("Good  Afternoon Sir! How are you doing?")
    else:
        speak("Good Evening Sir!How are you doing?")

    speak("I am Jarvis.How may I help you today? ")
    
def music():
   music_dir="C:\\Users\\User\\Downloads\\python\\project\\Voice-Assistant-System\\music"
   try:
        songs=os.listdir(music_dir)
        if songs:
            random_songs=random.choice(songs)
            speak("Playing a random  song sir!:{random_song}")
            os.startfile(os.path.join(music_dir,random_songs))
            logging.info(f"playing music:{random_songs}")
        else:
           speak("No music found in your music directory")
   except Exception :
        speak("Sorry Sir,I couldn't find your music folder")

greetings()
while True:
  query= takeCommand().lower()
  exit
  print(query)
 
  if "your name" in query:
    speak("My name is jarvis")
    logging.info("User asked for assistant's name.")
  elif "time" in query:
    strTime=datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"Sir the time is {strTime}")
#small talks
  elif "how are you" in query:
     speak("I'm functioning at full capasity sir!")
  elif "who made you" in query:
     speak("I was  created by Zarin sir,a briliant mind")
  elif "thank you" in query:
     speak("It's my pleasure sir!Always happy to help.")
#google
  elif"google" in query:
     speak("ok sir.Please type what doyou want to read?")
     webbrowser.open("google.com")
     logging.info("user requested to open google")
#calculator
  elif"calculator"  in query:
     speak("opening calculator")
     subprocess.Popen("calc.exe")
     logging.info("user requested to open calculator")
#Notepad
  elif"notepad" in query:
     speak("opening notepad")
     subprocess.Popen("notepad.exe")
     logging.info("user requested to open notepad ")
#Command prompt
  elif"open  terminal" in query or "cmd" in  query:
     speak("opening command prompt terminal")
     subprocess.Popen("cmd.exe")
     logging.info("user requested to open prompt")
#Calendar
  elif"calendar" in query:
     speak("opening windows calendar")
     webbrowser.open("https://calendar.google.com")
     logging.info("user requested to open calendar")
 
#facebook
  elif "facebook" in query:
     speak("ok,sir.Opening facebook")
     webbrowser.open("facebook.com")
     logging.info("User requested to open facebook")
#youtube
  elif "youtube" in query:
     speak("opening youtube for you")
     query=query.replace("youtube", "")
     webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
     logging.info("User requested to open youtube")
     
#github
  elif "github"in query:
     speak("ok,sir.Opening github")
     webbrowser.open("github.com")
     logging.info("User requested to open github.")
#jokes
  elif "jokes" in query:
     jokes=[
        "WHY DON'T PROGRAMMER LIKE NATURE? TOO MANY BUGS.",
        "I TOLD MY COMPUTER I  NEEDED A BREAK.IT SAID NO PROBLEM.I'LL GO TO  SLEEP",
        "WHY DO JAVA  DEVELOPERS WEAR GLASSES? BECAUSE THEY DON'T C SHARP."
     ] 
     speak(random.choice(jokes)) 
#songs
  
  elif "play music"in query or "music" in query:
    music()
    
  elif "exit" in query:
    speak("Thank you for your time sir.Have a great day.")
    logging.info("User exited the programme")
    exit()

  else:
    speak("I am  sorry,I can't help you with that.")
    logging.info("User asked for a  unsupported command.")
