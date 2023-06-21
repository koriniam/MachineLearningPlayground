# weather_forecast_app.py

import requests
import json

class WeatherForecastApp:
    def __init__(self, api_key):
        self.api_key = api_key

    def fetch_weather_forecast(self, city):
        url = f"http://api.weatherapi.com/v1/forecast.json?key={self.api_key}&q={city}&days=3"
        response = requests.get(url)
        data = json.loads(response.text)

        if "error" in data:
            print("An error occurred:", data["error"]["message"])
            return

        print(f"Weather forecast for {data['location']['name']}, {data['location']['country']}:")

        for day in data["forecast"]["forecastday"]:
            date = day["date"]
            avg_temp = day["day"]["avgtemp_c"]
            condition = day["day"]["condition"]["text"]
            print(f"{date}: {condition}, Avg Temp: {avg_temp}°C")

# Usage example
api_key = "YOUR_API_KEY"
app = WeatherForecastApp(api_key)

city = input("Enter a city: ")
app.fetch_weather_forecast(city)
