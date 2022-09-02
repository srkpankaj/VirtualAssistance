import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('LISTENING.........')
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if 'alexa' in command:
                command=command.replace('alexa', '')
                print(command)
    except:
        pass
    return command

def Run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        music = command.replace('play', '')
        talk('playing' + music)
        pywhatkit.playonyt(music)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M%p')
        print(time)
        talk('Currrent time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 5)
        print(info)
        talk(info)
    elif 'are you mad' in command:
        talk('Heh.. you are mad')
    elif 'i love you' in command:
        talk('aww.. i love you too')
    elif 'are you single' in command:
        talk('yes...i am too much single')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('please say it again')



while True:
    Run_alexa()