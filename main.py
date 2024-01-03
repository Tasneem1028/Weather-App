import requests
import json
import pyttsx3
city=input("Enter the name of the city:\n")
url=f"https://api.weatherapi.com/v1/current.json?key=1bdf290138e941c2a6695820240301&q={city}"
r=requests.get(url)


# print(r.text)
wdic=json.loads(r.text)
w=wdic["current"]["temp_c"]
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":

    speak(f" The current weather in {city} is {w} degrees")

