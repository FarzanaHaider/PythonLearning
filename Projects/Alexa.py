import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command=command.replace('alexa','')
                print(command)
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing'+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is '+time)
    elif 'how are you' in command:
        talk('I am fine and you')
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        joke=pyjokes.get_joke()
        print(joke)
        talk(joke)
    elif 'tell me' in command:
        person = command.replace('tell me','')
        try:
            info = wikipedia.summary(person,1)
            print(info)
            talk(info)
        except wikipedia.exceptions.DisambiguationError as e:
            talk("I'm sorry, I couldn't understand your query.")
    elif 'bye' in command:
        quit
    else:
        talk('Please say the command again.')

while True:
    run_alexa()