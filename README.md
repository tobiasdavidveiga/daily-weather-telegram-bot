# Daily Weather Bot

Automated Python script that sends daily weather reports via Telegram.

## Requirements

- Python 3.x
- Libraries listed in `requirements.txt`
- Telegram bot token
- Telegram chat ID

## Installation

```bash
pip install -r requirements.txt
```

## Configuration

### 1. Get Telegram Bot Token

- Open Telegram and search for `@BotFather`
- Send `/newbot` command
- Choose a name for your bot (e.g., "My Weather Bot")
- Choose a username ending in "bot" (e.g., "myweather_bot")
- Copy the token provided (format: `123456789:ABCdefGHIjklMNOpqrsTUVwxyz`)
- Start a conversation with your new bot by searching for it and sending `/start`

### 2. Get Your Chat ID

- Search for `@userinfobot` in Telegram
- Send `/start` command
- Copy the ID number shown (e.g., `123456789`)

### 3. Get Location Coordinates

Find your city's latitude and longitude:
- Go to https://www.latlong.net/
- Search for your city
- Copy the coordinates

Example coordinates:
- New York: `40.7128, -74.0060`
- London: `51.5074, -0.1278`
- Tokyo: `35.6762, 139.6503`
- Buenos Aires: `-34.6037, -58.3816`

### 4. Update the Script

Open `weather_bot.py` and replace the following values:

```python
LAT = "YOUR_LATITUDE"           # Replace with your latitude (e.g., 40.7128)
LON = "YOUR_LONGITUDE"          # Replace with your longitude (e.g., -74.0060)
TELEGRAM_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"    # Replace with your bot token
TELEGRAM_CHAT_ID = "YOUR_TELEGRAM_CHAT_ID"    # Replace with your chat ID
```

**Example:**
```python
LAT = "40.7128"
LON = "-74.0060"
TELEGRAM_TOKEN = "123456789:ABCdefGHIjklMNOpqrsTUVwxyz"
TELEGRAM_CHAT_ID = "987654321"
```

## Usage

### Manual Execution

```bash
python weather_bot.py
```

### Automated Daily Reports

**Deploy on PythonAnywhere (free):**

1. Create account at https://www.pythonanywhere.com
2. Go to **Files** tab and upload `weather_bot.py`
3. Open a **Bash console** and install dependencies:
   ```bash
   pip3 install requests python-telegram-bot --user
   ```
4. Go to **Tasks** tab
5. Create a new scheduled task:
   - **Time**: Set your preferred time in UTC format
     - For 6:00 AM in Argentina (UTC-3): use `09:00`
     - For 7:00 AM in New York (UTC-5): use `12:00`
     - For 8:00 AM in London (UTC+0): use `08:00`
   - **Command**: `python3 /home/YOUR_USERNAME/weather_bot.py`
     - Replace `YOUR_USERNAME` with your PythonAnywhere username

## Features

- Fetches current weather conditions
- Reports daily minimum and maximum temperatures
- Includes humidity and rain probability
- No API key required (uses Open-Meteo)
- Sends formatted reports via Telegram

## Example Output

```
Weather Report - 2025-10-28

Current: 18.5°C
Min: 14.2°C
Max: 22.8°C

Conditions: Partly cloudy
Humidity: 65%
Rain probability: 20%
```

## Troubleshooting

**401 Unauthorized error:**
- Verify your Telegram bot token is correct
- Make sure you started a conversation with your bot

**No weather data:**
- Check that latitude and longitude are in decimal format
- Verify coordinates are correct (latitude: -90 to 90, longitude: -180 to 180)

**Message not received:**
- Confirm you have the correct chat ID
- Ensure you started a conversation with the bot first
