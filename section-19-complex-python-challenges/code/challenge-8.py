import requests, json


api_key = "fb1456186ddbe9e8e8f2a5b8230f5adc"

base_url = " http://api.openweathermap.org/data/2.5/weather?"

cityname = input("Enter the City Name: ")
cityname.lower()
url_api = base_url+f"q={cityname}"+f"&appid={api_key}"

response = requests.get(url_api)

x = response.json()

if x["cod"] != "404":

    y = x["main"]
    current_temperature = y["temp"]
    current_pressure = y["pressure"]
    current_humidiy = y["humidity"]
    z = x["weather"]
    weather_description = z[0]["description"]
    print(" Temperature (in kelvin unit) = " +
          str(current_temperature) +
          "\n atmospheric pressure (in hPa unit) = " +
          str(current_pressure) +
          "\n humidity (in percentage) = " +
          str(current_humidiy) +
          "\n description = " +
          str(weather_description))

else:
    print(" City Not Found ")
