import requests
import pandas as pd

def fetch_weather(city="Warsaw"):
    API_KEY = "MYAPIKEY" # !!!!!!!
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    df = pd.DataFrame([{
        "city": city,
        "temp": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "weather": data["weather"][0]["main"],
        "timestamp": pd.Timestamp.now()
    }])

    df.to_csv("data/weather.csv", index=False)
    return df