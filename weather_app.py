import requests

API_KEY = "YOUR_API_KEY_HERE"

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"]

        print(f"\n🌍 Weather in {city}")
        print(f"🌡️ Temperature: {temperature}°C")
        print(f"💧 Humidity: {humidity}%")
        print(f"☁️ Condition: {condition}")
    else:
        print("❌ City not found or API error")

def main():
    print("🌦️ Weather App")
    city = input("Enter city name: ")
    get_weather(city)

if __name__ == "__main__":
    main()