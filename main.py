import random
import http.client
from datetime import datetime
from kivy.app import App
from kivy.uix.gridlayout import GridLayout



class Container(GridLayout):
    def outputTime(self) -> str:
        data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.label.text = data


    def outputRandomCar(self) -> str:
        cars = ['Audi', 'Lada', 'BMW', 'Mercedes-Benz', 'Aston Martin', 'Ferrari', 'Porshe', 'УАЗ', 'GEEP']
        car = random.choice(cars)
        self.label.text = car
    
    
    def outputHeadsOrTails(self) -> str:
        coin_sides = ['Орёл', 'Решка']
        side = random.choice(coin_sides)
        self.label.text = side

    
    def outputCurlInternetProtocol(self) -> None:
        conn = http.client.HTTPConnection("ifconfig.me")
        conn.request("GET", "/ip")
        ip = conn.getresponse().read().decode('utf-8')
        self.label.text = ip


class RandomFunctionsApp(App):
    def build(self) -> None:
        return Container()



if __name__ == "__main__":
    RandomFunctionsApp().run()