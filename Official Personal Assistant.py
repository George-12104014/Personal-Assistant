import speech_recognition as sr
import os
import pyttsx3
import webbrowser
import pyautogui
import datetime
import sys
import requests

#Voice Setup (Male)
def command(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

#Voice Setup(Female)
def set_female_voice(rate=180):
    engine = pyttsx3.init()  # Initialize the pyttsx3 engine
    voices = engine.getProperty('voices')  # Get available voices
    
    for voice in voices:
        # Check for "Zira" (female voice)
        if 'zira' in voice.name.lower():
            engine.setProperty('voice', voice.id)  # Set the voice to Microsoft Zira (female)
            break
    else:
        print("Female voice (Zira) not found, using default voice.")
    
    # Set the speech rate (speed)
    engine.setProperty('rate', rate)  
    
    return engine

def say(text, rate=150):
    engine = set_female_voice(rate)  
    engine.say(text)  
    engine.runAndWait()  
    
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = .8
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some error occurred. Sorry, Sir!"
    
if __name__ == "__main__":
    say("Good Morning Sir, I am Enola Holmes")
    command(" And I am Sherlock Holmes, Your Personal Assistant. How can we assist you today?")
    
    while True:
        print("Listening ...")
        query = takecommand()

        # Check if the query is None (i.e., no command was recognized)
        if query is None:
            continue  

        # Normalized Query
        normalized_query = query.strip().lower()
        
        if "good morning" in normalized_query or "morning" in normalized_query:
             say("Good morning Sir! ")
             command("How can we assist you today?")
             continue
        if "good afternoon" in normalized_query or "afternoon" in normalized_query:
             say("Good Afternoon Sir! ")
             command("How can we assist you today?")
             continue
        if "good evening" in normalized_query or "evening" in normalized_query:
             say("Good Evening Sir! ")
             command("What can we do for you?")
             continue
        if " are you" in normalized_query or "how are you" in normalized_query or "How are you" in normalized_query:
             say("I am fine Sir! ")
             command("How can we assist you today?")
             continue
        # Stop listening if the command is "turn off"
        if "turn off" in normalized_query:
            say("Thank You Sir.")
            command("Have a Nice Day. Just call us if you need any help")
            break  # Break the loop to stop the assistant from listening

        # Open websites
        sites = [
            ["youtube", "https://youtube.com"],
            ["google", "https://google.com"],
            ["wikipedia", "https://wikipedia.com"],
            ["messenger", "https://messenger.com"],
            ["facebook", "https://facebook.com"],
            ["instagram", "https://instagram.com"],
            ["whatsapp", "https://whatsapp.com"],
        ]

        for site in sites:
            if f"open {site[0]}" in normalized_query:
                say(f"Sir,Opening {site[0]} ....")
                webbrowser.open(site[1])
        
        # Command for Time
        if "the time" in normalized_query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sir,the time is {strTime}")
            command(f"Sir,the time is {strTime}")
            
        
        # Command for ChatGPT
        if "open chat" in normalized_query or "gpt" in normalized_query :
            say("Sir, opening ChatGPT....")
            webbrowser.open("https://chatgpt.com/")
            
            
        #Command for DeepSeek    
        if "deep seek" in normalized_query or "deep" in normalized_query :
            command("Sir, opening DeepSeek....")
            webbrowser.open("https://chat.deepseek.com/")     
            
            
        #Command for Weather
        if "weather" in normalized_query:
            url = "http://api.weatherapi.com/v1/current.json"
            key = "2d2f7d45680b4fca90170647250902"
            say("Enter your Location")
            location = input("Enter location: ")
            url = f"{url}?key={key}&q={location}"
            response = requests.get(url)                        
            if response.status_code == 200:
                weather_data = response.json()
                print("Location:", weather_data["location"]["name"])   
                say(f"Location: {weather_data['location']['name']}")
                print("Country:", weather_data["location"]["country"])
                command(f"Country: {weather_data['location']['country']}")
                print("Temperature (C):", weather_data["current"]["temp_c"])
                say(f"Temperature : {weather_data['current']['temp_c']} degrees Celsius")
                print("Condition:", weather_data["current"]["condition"]["text"])
                command(f"Condition: {weather_data['current']['condition']['text']}")
            else:
                print("Failed to retrieve weather data:", response.status_code)
                say("Sir, opening Weather....")
                webbrowser.open("https://openweathermap.org/")