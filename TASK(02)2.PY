import requests

# Enter your API key here (get it from openweathermap.org)
API_KEY = "009728215924485167b7a868887f2573"

city = input("Enter city name: ")

# API URL
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

try:
    response = requests.get(url)
    data = response.json()

    # Check if city is valid
    if data["cod"] == 200:
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"]

        print(f"\nWeather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {condition}")
    else:
        print("City not found. Please check the name.")

except Exception as e:
    print("Error: Could not retrieve weather data.")
