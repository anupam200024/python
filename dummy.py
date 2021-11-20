import datetime
import speech_recognition
import pyttsx3
import wikipedia
import webbrowser
import random

engine = pyttsx3.init('sapi5')
# sapi5 are windows supported voices
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour > 0 and hour < 12:
        speak("Good Morning!")

    elif hour > 12 and hour < 17:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    # speak("I'm anver")


def takecommand():
    # it takes microphone input from the user and returns string output

    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        # pause_threshold is seconds of non-speaking audio before a phrase is considered complete
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}",)

    except Exception as e:
        print(e)
        print("Unable to recognize, Please speak again")
        speak("Unable to recognize, Please speak again")
        return "None"

    return query


def wikisearch():
    query = takecommand()
    speak('Searching wikipedia...')
    try:
        p = wikipedia.page(query)
        results = wikipedia.summary(p, sentences=2,)

    except wikipedia.DisambiguationError as err:
        # error occurs when there are multiple pages with same title

        print(err.options[0])
        speak(wikipedia.summary(err.options[0], sentences=2))

    except wikipedia.exceptions.PageError as e:
        # error occurs when no page exists with the title name
        print(e)
        speak(e)


if __name__ == "__main__":
    wishme()
    speak("I'm anver")
    speak("What is your name")

    while True:
        name = takecommand()
        if name != "None":
            break

    speak(f'Hi {name}. how can i help you')

    while True:
        query = takecommand().lower()

        greetlist = ['hi', 'hello', 'hola']
        goodlist = ['good evening', 'goodevening', 'good afternoon',
                    'goodafternoon', 'good evening', 'goodevening', 'good night', 'goodnight']

        # logic for executing tasks based on query
        if 'wikipedia search' in query:
            wikisearch()

        elif 'exit' in query:
            exit(0)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            exit(0)

        elif 'open google' in query:
            webbrowser.open("google.com")
            exit(0)

        elif 'open class' in query:
            webbrowser.open("myclass.lpu.in")
            exit(0)

        elif 'open dashboard' in query:
            webbrowser.open("ums.lpu.in/lpuums/")
            exit(0)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'joke' in query:
            jokeslist = ['Why did Gmail reject the password 14 days. It was two week.', 'How does a tree use Gmail., They log in.', 'What do you call a computer that sings., A Dell.', 'What is a popular search engine for ghosts., Ghoul-gle.', 'What is Googles Favourite snack., Microchips.', 'Why did the google laptop keep sneezing., It has virus.', 'What did the google employee have for lunch., A byte to eat.', 'Where is the best place to hide your sweets., Page 2 of google.', 'What do you call a search engine that sings Christmas songs., Michael Google.', 'What do search engine do babies use., Google Ga ga.',
                         'Why did the chimps share on amazon account., They were Prime mates.', 'Why was the cookie monster upset., Because google asked if he wanted to delete his cookies.', 'What was the old google office covered in., Cobwebs.', 'Why are some internet users so selfish., Because they are all meme meme meme.', 'What does a search engine wear in the water., swimming googles.', 'I searched google for the best way to light a firework., It came up with over a million matches.', 'What did the turkey say to the computer., Google google google.', 'Wht did the spider use Google., To find some cool websites.']
            speak(random.choice(jokeslist))

        elif query in greetlist:
            speak("Hi. how can i help you")

        elif query in goodlist:
            wishme()
            speak("How can i help you")

        elif 'fact' in query:
            factlist = ['More human twins are being born now than ever before.', 'A narwhals tusk reveals its past living conditions.', 'The first person convicted of speeding was going eight miles per hour', 'New car smells is the scent of dozens chemicals', 'The world wastes about 1 billion metric tons of food each year.', 'The severed head of a sea slug can grow a whole new body', 'The smallest reptile was first reported in 2021', ' Many feet bones dont harden until you are an adult', 'Some sea snakes can breathe through their skin',
                        'The heads on easter island have bodies', 'The moon has moonquakes just like earthquakes', 'Goosebumps are meant to ward off predators', 'There is no such thing as pear cider', 'Pineapple works as a natural meat tenderizer', 'Humans are the only animals that blush', 'The wood frog can hold its pee for up to eight months', 'The nottest spot on the planet is in Libya', 'You lose up to 30 percent of your taste buds during flight', 'Your nostrils work one at a time', 'Only two mammals like spicy food. humans and the tree shrew']
            speak(random.choice(factlist))
