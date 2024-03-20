import requests


api_key = 'enteryourapikeyhere'

city_name = input("Enter city: ")
state_code = input("Enter your abbreviated State value(Max 2 characters): ")
country_code = input("Enter your country of origin: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={city_name},{state_code},{country_code}&units=imperial&APPID={api_key}")

if weather_data.json()['cod'] == '404':
    print("Location not found")
else: 
    weather = weather_data.json()['weather'][0]['main']
temp = weather_data.json()['main']['temp']
feels_like = weather_data.json()['main']['feels_like']

print(f"The weather in {city_name},{state_code} is: {weather}.")
print(f"The temperature in {city_name},{state_code} is: {temp}°F.")
print(f"The weather feels like: {feels_like}°F.")