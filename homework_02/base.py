from abc import ABC
from unicodedata import name
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):

    weight = 900
    started = False
    fuel = 50
    fuel_consumption = 6

    def __init__(self, weight, fuel, fuel_consumption) -> None:

        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
    
    def start(self):

        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError("Low fuel level!")
    
    def move(self, distance):

        if self.fuel >= self.fuel_consumption * distance:
            self.fuel = self.fuel - self.fuel_consumption * distance
        else:
            raise NotEnoughFuel("Not enough fuel!")
                

if __name__ == "__main__":
    vihicle  = Vehicle(1200, 19, 5)
    #print(vihicle.weight)
    # vihicle.move(4)
