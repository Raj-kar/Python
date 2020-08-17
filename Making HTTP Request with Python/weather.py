# API KEY = b**********************f2660

import requests

while True:
    try:
        city_name = input("Enter a city name :: ")

        url = "http://api.openweathermap.org/data/2.5/weather?q=" + \
            city_name + "&appid={enter_your_app_id}&units=metric"

        response = requests.get(url).json()

        print("weather:", response['weather'][0]['main'])
        print(f"current temp: {round(response['main']['temp'])}°c")
        print(f"feels like: {round(response['main']['feels_like'])}°c")
    except KeyError:
        print("\n Opps ! city not found ..! \n")
    except Exception:
        print("\n Opps ! please check your network and try again ..! \n")
    else:
        break
