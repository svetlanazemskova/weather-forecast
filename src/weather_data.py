import requests

def fetch_weather(api_key, cities_list):
    message = ""
    for city in cities_list:
        weather_data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}")

        # print(weather_data.status_code)
        # print(weather_data.json())

        if weather_data.status_code // 100 == 4:
            message += f"City <{city}> was not found\n"
        else:
            country = weather_data.json()['sys']['country']
            weather = weather_data.json()['weather'][0]['main']
            temp = round((weather_data.json()['main']['temp'] - 32) * 5 / 9)
            temp2 = round((weather_data.json()['main']['feels_like'] - 32) * 5 / 9)
            wind_speed = weather_data.json()['wind']['speed']

            message += f"The weather in {city} ({country}) is: {weather}\n"
            message += f"The temperature in {city} is: {temp}ºC feels like: {temp2}ºC\n"
            message += f"The wind speed is: {wind_speed} m/s\n"
            message += "*" * 10 + "\n"
    return message



