import requests

api_key = '45c53b58dee89aa6f6f5abdb7e56db4e'

MY_LATITUDE = -34.003502
MY_LONGITUDE = 18.735451

parameters = {
    "lat": MY_LATITUDE,
    "lon": MY_LONGITUDE,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)

if response.status_code == 200:

    weather_data = response.json()
    condition = weather_data["hourly"][1]["weather"][0]["main"]
    temperature = int(weather_data["hourly"][0]["temp"] - 273.15)
    weather_id = weather_data["hourly"][:12]
    print(weather_id)

    




