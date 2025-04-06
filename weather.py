import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()

def get_current_weather():
    print('\n*** Get Current Weather Conditions ***\n')

    city = input("\nPlease enter a city name: ")

    requests_url = f'https://api.openweathermap.org/data/2.5/weather?&appid={os.getenv("API_KEY")}&q={city}&units=metric'

    print(requests_url)
    weather_data = requests.get(requests_url).json()

    pprint(weather_data)

    print(f'\nCurrent weather for {weather_data["name"]}: ')
    print(f'\nThe temperature is {weather_data["main"]["temp"]:.1f}°')

get_current_weather()