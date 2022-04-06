import requests


class WeatherParams:
    def __init__(self, city, country, units="metric"):
        self.city = city 
        self.country = country
        self.units = units
        self.mode = "json"


def get_weather(appid, weather_params):
    endpoint  = "http://api.openweathermap.org/data/2.5/weather"
    query_params = {
        'q': weather_params.city,
        'q': weather_params.country,
        'mode': weather_params.mode,
        'units': weather_params.units,
        'appid': appid, 
    }
    
    
    response = requests.get(endpoint, params=query_params)
    #print (response.status_code) 
    # the print statement returns 200 HTTP status code to confirm code works
    return response.json()


if __name__ == "__main__":
    appid = "a37bce417d85324e3a8633ab887393eb" 
    city_name = input("Enter city name : ")
    country_name = input("Enter country name : ")
    params = WeatherParams(city_name, country_name)
    print (f"Current temperature in {city_name} is {get_weather(appid, params) ['main']['temp']}")