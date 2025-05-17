import requests

def get_weather(city):
    API_KEY = "975fb6aeea696719822634f77e86208d"  # Replace this with your real API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        weather = {
            "City": data["name"],
            "Temperature": f"{data['main']['temp']}°C",
            "Weather": data["weather"][0]["description"].capitalize(),
            "Humidity": f"{data['main']['humidity']}%",
            "Wind Speed": f"{data['wind']['speed']} m/s"
        }
        return weather
    else:
        return {"Error": "City not found or API error."}

def main():
    city = input("Enter city name: ")
    weather = get_weather(city)
    for key, value in weather.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()