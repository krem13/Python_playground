import requests

class City:
    def __init__(self, name, lat, lon, units):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.units = units
        self.get_data()

    def get_data(self):
        url = "http://api.openweathermap.org/data/2.5/weather"
        response = requests.get(url, params={"units": self.units,"lat": self.lat, "lon": self.lon, "appid": "your_api_key_here"})
        if (response.status_code != 200):
            raise Exception("API request unsuccessful.")
        else:
            response_json = response.json()
            self.temperature = response_json['main']['temp']
            self.temp_min = response_json['main']['temp_min']
            self.temp_max = response_json['main']['temp_max']
            self.humidity = response_json['main']['humidity']

    def display_city_weather(self):
        print(f"City: {self.name}")
        self.display_temp()

    def display_temp(self):
        units_symbol = "C"
        if self.units == "imperial":
            units_symbol = "F"
        print(f"Temperature: {self.temperature}°{units_symbol}")
        print(f"Temperature, low: {self.temp_min}°{units_symbol}")
        print(f"Temperature, high: {self.temp_max}°{units_symbol}")
        print(f"Humidity: {self.humidity}%")

my_city = City("Tokyo", 35.6895, 139.6917, "metric")
my_city.display_city_weather()

vacation_city = City("Portland", 45.5236, -122.6750, "imperial")
vacation_city.display_city_weather()