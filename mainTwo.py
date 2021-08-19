# from urllib import request
import requests
import json
import pyttsx3

# string + alt +v read from internet


url = "https://official-joke-api.appspot.com/jokes/ten"
# r = request.urlopen(url)
# print(r.getcode())
response = requests.get(url)
print(response.status_code)
# data = r.read()
# data = response.text
jsonData = json.loads(response.text)
print(jsonData)


class Joke:
    def __init__(self, setup, punchline) -> None:
        self.setup = setup
        self.punchline = punchline

    # strg + o to string
    def __str__(self) -> str:
        return f"setup {self.setup} punchline {self.punchline}"


jokes = []
# loop
for j in jsonData:
    setup = j["setup"]
    punchline = j["punchline"]
    joke = Joke(setup, punchline)
    jokes.append(joke)
    print(f"Got {len(jokes)} jokes")

    for joke in jokes:
        print(joke)

pyttsx3.speak("Setup")
pyttsx3.speak(joke.setup)
pyttsx3.speak("The Punchline")
pyttsx3.speak(joke.punchline)
pyttsx3.speak("It was a nice joke")

# print(r.read())

# api call work with json
