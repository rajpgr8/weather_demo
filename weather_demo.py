from pyowm import OWM
from prettytable import PrettyTable
import argparse

APIKEY='<YOUR API KEY>'                  #your API Key here as string
def print_weather_data(cities):
    OpenWMap=OWM(APIKEY)                   # Use API key to get data
    mgr=OpenWMap.weather_manager()
    weather_status = PrettyTable(['City Name', 'Status', 'Min Temperature', 'Max Temperature', 'Feel Like'])
    for city in cities:
        data = mgr.weather_at_place(city)
        weather = data.weather
        temp_dict_fahrenheit = weather.temperature('fahrenheit')

        weather_status.add_row([city, weather.status, temp_dict_fahrenheit['temp_min'], temp_dict_fahrenheit['temp_max'],temp_dict_fahrenheit['feels_like']])
    print(weather_status)


if __name__ == "__main__":
    cities = ['London', 'New York', 'Toronto']
    print_weather_data(cities)
    
    
