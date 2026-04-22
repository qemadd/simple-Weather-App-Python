import requests

API_key ="YOUR_API_KEY_HERE"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

print("=== Welcome to Weather App (type 'exit' to quit) ===")

while True:
    city= input("\nEnter the city name: ")

    if city.strip().lower()=="exit":
        print("Goodbye! :(")
        break


    url=f"{BASE_URL}?q={city}&appid={API_key}&lang=en&units=metric"
    response = requests.get(url)


    if response.status_code==200:
        data=response.json()


        temp= data["main"]["temp"]
        humidity=data["main"]["humidity"]
        description=data["weather"][0]["description"]

        print("==== Weather details ====")
        print(f"City:{city}")
        print(f"temperature: {temp} °C")
        print(f"humidity: {humidity}%")
        print(f"description: {description}")
        print("=========================")

    else:
        print("Sorry, city not found!,try again")