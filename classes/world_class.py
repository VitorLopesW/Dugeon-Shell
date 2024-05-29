import random 

class World:
    def __init__(self):
        self.weather = 'sunny'
        self.name = 'Pythonia'

    def modify_weather(self, value):
        self.weather = value
        print(f"The weather is now {self.weather}.")
    def random_weather(self):
        weather_list = ['sunny', 'rainy']
        self.modify_weather(random.choice(weather_list))
    def weather_world_building(self):
        if self.weather == 'sunny':
            return "The sun is shining"
        elif self.weather == 'rainy':
            return "It's raining"