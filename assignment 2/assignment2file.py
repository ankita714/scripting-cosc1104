

# Author : Ankita (100941771)
# Date: 17-11-2024
# Personalized Weather-Based Daily Planner
# Description: This Personalized Weather-Based Daily Planner helps user to plan his/her day 
# by giving activity suggestions based on real-time weather. Whether it’s sunny, rainy, or snowy, 
# it tailors recommendations to suit the conditions and even logs users daily plans for future reference. 
# It’s like having a friendly assistant to keep user prepared for the day ahead!

import requests # https://docs.python-requests.org/
from datetime import datetime # https://docs.python.org/3/library/datetime.html

# Constants
API_KEY = "e2019cfecead5da5fe44d3b1c478b438" # my API
BASE_URL = "http://api.openweathermap.org/data/2.5/weather" # OpenWeatherMap https://openweathermap.org/api
LOG_FILE = "daily_planner_log.txt"

def fetch_weather(city, country=None):  # this function fetch weather information for the city given by the user
    try:
        location = f"{city},{country}" if country else city
        params = {"q": location, "appid": API_KEY, "units": "metric"}
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def suggest_activities(weather): # Function for suggesting activities 
    condition = weather["weather"][0]["main"].lower()
    temp = weather["main"]["temp"]

    if "clear" in condition or "sun" in condition:
        return f"\n It's sunny with {temp}°C. Great for a walk or an outdoor activity!"
    elif "rain" in condition:
        return f"\n It's rainy with {temp}°C. How about an indoor activity like yoga or reading?"
    elif "snow" in condition:
        return f"\n It's snowy with {temp}°C. Perfect for staying cozy indoors!"
    else:
        return f"\n The weather is {condition} with {temp}°C. Plan your day accordingly!"

def personalized_greeting(name, weather):
    city = weather["name"]
    desc = weather["weather"][0]["description"]
    temp = weather["main"]["temp"]
    return f"\n Hello, {name}! Today's weather in {city}: {desc.capitalize()}, {temp}°C."

def log_to_file(log_entry): # function to add new entries to the log txt file 
    """Append the log entry to a log file."""
    with open(LOG_FILE, "a") as file:
        file.write(log_entry + "\n")

def main():
    print("\n *****  Welcome to the Personalized Weather-Based Daily Planner!  ***** ")
    name = input("\nEnter your name: ")
    city = input("\nEnter your city: ")
    country = input("\nEnter your country code (optional, e.g., 'CA' for Canada): ").strip()

    weather = fetch_weather(city, country) # calling fetch weather function
    if weather:
        greeting = personalized_greeting(name, weather)
        suggestion = suggest_activities(weather)

        # Display output to the user
        print("\n" + greeting)
        print("-----Activity Suggested:-----")
        print(suggestion)

        # Log the interaction
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = (
            f"[{timestamp}] User: {name}, City: {city}, "
            f"Weather: {weather['weather'][0]['description'].capitalize()}, {weather['main']['temp']}°C, "
            f"Suggestions: {suggestion}"
        )
        log_to_file(log_entry)

    else:
        print("Could not fetch weather data. Please try again.")

if __name__ == "__main__":
    main()

