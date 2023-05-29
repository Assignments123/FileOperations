
import os
import requests

def weatherbyname(cityname ,countryname):
    city_name = cityname
    country_name = countryname
    print(country_name)
    appid = os.getenv('APPID')

    # resp = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name},{country_name}&appid={appid}&units=metric').json()
    url = 'https://api.openweathermap.org/data/2.5/weather?'
    params = {
        "q":city_name,
        "appid":appid,
        "units":"metric",
    }
    resp = requests.get(url,params=params).json()
    return resp

def weatherbycoords(lattitude,longitude):
    lat = lattitude
    lon = longitude
    appid = os.getenv('APPID')
    url = 'https://api.openweathermap.org/data/2.5/weather?'
    params = { 
        "lat" : lat,
        "lon" : lon,
        "appid": appid,
        "units" : "metric",
    }
    resp = requests.get(url,params=params).json()
    return resp