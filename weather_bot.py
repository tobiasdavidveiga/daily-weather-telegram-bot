import requests
from datetime import datetime
from telegram import Bot
import asyncio

LAT = "YOUR_LATITUDE"
LON = "YOUR_LONGITUDE"
TELEGRAM_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
TELEGRAM_CHAT_ID = "YOUR_TELEGRAM_CHAT_ID"

def get_weather():
    url = f"https://api.open-meteo.com/v1/forecast?latitude={LAT}&longitude={LON}&current=temperature_2m,relative_humidity_2m,weather_code&daily=temperature_2m_max,temperature_2m_min,precipitation_probability_max&timezone=auto"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        return {
            'temp_current': data['current']['temperature_2m'],
            'temp_min': data['daily']['temperature_2m_min'][0],
            'temp_max': data['daily']['temperature_2m_max'][0],
            'humidity': data['current']['relative_humidity_2m'],
            'rain_prob': data['daily']['precipitation_probability_max'][0] or 0,
            'description': get_weather_description(data['current']['weather_code'])
        }
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather: {e}")
        return None

def get_weather_description(code):
    weather_codes = {
        0: "Clear sky", 1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
        45: "Fog", 48: "Depositing rime fog", 51: "Light drizzle", 53: "Moderate drizzle",
        55: "Dense drizzle", 61: "Slight rain", 63: "Moderate rain", 65: "Heavy rain",
        71: "Slight snow", 73: "Moderate snow", 75: "Heavy snow", 77: "Snow grains",
        80: "Slight rain showers", 81: "Moderate rain showers", 82: "Violent rain showers",
        85: "Slight snow showers", 86: "Heavy snow showers", 95: "Thunderstorm",
        96: "Thunderstorm with slight hail", 99: "Thunderstorm with heavy hail"
    }
    return weather_codes.get(code, "Unknown conditions")

def format_message(weather):
    if not weather:
        return "Unable to fetch weather data"
    
    date = datetime.now().strftime("%Y-%m-%d")
    
    message = f"""Weather Report - {date}

Current: {weather['temp_current']:.1f}°C
Min: {weather['temp_min']:.1f}°C
Max: {weather['temp_max']:.1f}°C

Conditions: {weather['description']}
Humidity: {weather['humidity']}%
Rain probability: {weather['rain_prob']:.0f}%"""
    
    return message

def send_report():
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Fetching weather data...")
    
    weather = get_weather()
    message = format_message(weather)
    
    print(message)
    
    try:
        bot = Bot(token=TELEGRAM_TOKEN)
        asyncio.run(bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message))
        print("Message sent successfully!")
    except Exception as e:
        print(f"Error sending message: {e}")

if __name__ == "__main__":
    send_report()
