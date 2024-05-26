import random 

class World:
    def __init__(self):
        self.weather = 'sunny'

    def modify_weather(self, value):
        self.weather = value
        print(f"The weather is now {self.weather}.")
    def random_weather(self):
        weather_list = ['sunny', 'rainy', 'cloudy', 'foggy', 'stormy']
        self.modify_weather(random.choice(weather_list))