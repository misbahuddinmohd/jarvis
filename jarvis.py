import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib


mail_id = {1:'mail_id_1@gmail.com', 2: 'mail_id_2@gmail.com'}

# setting a voice using sapi5 speak API
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# function to speak or give audio output to user
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# function to wish the user
def wishMe():
    # gettinh the current hour
    hour = int(datetime.datetime.now().hour)
    # wishing the user according to the current user
    if hour>=0 and hour<=12:
        speak('good morning')
    elif hour>12 and hour<=18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("I am Jarvis. How can i help you")

# function to take microphone audio commands and return string output
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        # setting pause time after execution (program start listening after pause threshlod)  
        r.pause_threshold = 1
        # listening to the source4
        audio = r.listen(source)
    try:
        print("recognizing...")
        # recognizing the audio context using google engine
        query = r.recognize_google(audio, language='en=in')
        print(f'user said: {query}\n')
    except Exception as e:
        print(e)
        print("please say that again.. ")
        return "None"
    return query

# function to send email
def sendEmail(to, text):
    server = smtplib.SMTP('smtp.google.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your_email@gmail.com', 'your_password')
    server.send('your_email@gmail.com', to, text)
    server.close()


# main function
if __name__ == "__main__":
    wishMe()
    if 1:
        query = takeCommand().lower()
        # logic to perform task based on query
        if "wikipedia" in query:
            speak("searching wikipedia")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=3)
            speak("according to wikipedia")
            print(result)
            speak(result)
        elif "open youtube" in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")
        elif "open google" in query:
            speak("opening google")
            webbrowser.open("google.com")
        elif "open university" in query:
            speak("opening osmania university")
            webbrowser.open("osmania.ac.in")
        elif "open amazon" in query:
            speak("opening amazon")
            webbrowser.open("amazon.com")
        elif "open music" in query:
            music_dir = 'D:\\mp3_player\\audio'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f'the time is {strTime}')
        elif "open chrome" in query:
            speak("opening chrome")
            chromePath = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            os.startfile(chromePath)
        elif "send email" in query:
            speak("to whom you want to send the email")
            person = takeCommand()
            if "person_name" in person:
                try:
                    speak("what should i send")
                    text = takeCommand()
                    sendEmail(mail_id[1], text)
                    speak("email has been sent")
                except Exception:
                    print(Exception)
                    speak("unable to send email")     
                                   