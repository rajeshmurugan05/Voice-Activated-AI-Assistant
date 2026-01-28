
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import requests
import listener
import sys
import json

listener = sr.Recognizer()
def engine_talk(text):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty('voice', voices[2].id)
    engine.say(text)
    engine.runAndWait()


def user_commands():
    command = ""
    try:
        with sr.Microphone() as source:
            print("listening!!")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'mybot' in command:
                command = command.replace('mybot', '')
                print(command)
    except Exception:
        pass
    return command


def weather(city):
    # API key
    api_key = "use your API key"

    # base_url variable to store url
    base_url = "http://api.openweathermap.org/data/2.5/weather?&q="

    # Give city name
    city_name = city

    # complete_url variable to store
    complete_url = base_url + "appid=" + api_key + city_name

    # get method of requests module
    # return response object
    response = requests.get(complete_url)

    # json method of response object
    # convert json format data into
    # python format data
    x = response.json()

    # Now x contains list of nested dictionaries
    # Check the value of "cod" key is equal to
    # "404", means city is found otherwise,
    # city is not found
    if x["cod"] != "404":
        # store the value of "main"
        # key in variable y
        y = x["main"]

        # store the value corresponding
        # to the "temp" key of y
        current_temperature = y["temp"]
        temp_in_celcius = current_temperature - 273.15
        return str(int(temp_in_celcius))


def talk(param):
    pass


def run_mybot():
    command = user_commands()
    if 'hello' in command:
        engine_talk('Hi! How are you doing!')
    elif 'how are you doing' in command:
        engine_talk('I am doing good! Thanks for asking!')
    elif 'play a song' in command:
        song = command.replace('play', '')
        engine_talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        engine_talk('Current Time is' + time)
    elif 'todays date' in command:
        date = datetime.datetime.today().strftime('%D:%M:%Y')
        print(date)
        engine_talk('Today\'s date is ' + date)
    elif 'joke' in command:
        get_j = pyjokes.get_joke()
        print(get_j)
        engine_talk(get_j)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        engine_talk(info)
    elif 'what is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        engine_talk(info)
    elif 'weather' in command:
        # engine_talk('Please tell name of the city')
        city = 'Hong Kong'
        # city = 'Mumbai'
        engine_talk('The temperature in Hong Kong is' + weather(city) + 'degree celcius')
    elif 'are you single' in command:
        engine_talk('I am in a relationship with wifi')
    elif 'good answer' in command:
        engine_talk("Thanks")
    elif 'bye' in command:
        engine_talk("Good bye")
    else:
        engine_talk('I could not hear you properly, Can you repeat it again')
        print("I could not hear you properly, Can you repeat it again")


while True:
    run_mybot()
