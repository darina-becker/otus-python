"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.exceptions import CargoOverload
from homework_02.base import Vehicle

class Plane(Vehicle):

    cargo = 0
    max_cargo = 100

    def __init__(self, weight, fuel, fuel_consumption, max_cargo) -> None:

        self.weight = weight
        self.max_cargo = max_cargo
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def load_cargo(self, numb):

        if self.cargo + numb > self.max_cargo:
            raise CargoOverload("Maximum cargo weight reached!")
        else:
            self.cargo = self.cargo + numb

    def remove_all_cargo(self):

        save_cargo = self.cargo
        self.cargo = 0
        return save_cargo



# if __name__ == "__main__":
plane = Plane(1200, 50, 6, 100)
print(plane.weight)
# plane.load_cargo(60)
# print(plane.cargo)
# print(plane.remove_all_cargo())
# print(plane.cargo)


# print(plane.weight)
# print(plane.fuel)
# print(plane.fuel_consumption)
# print(plane.max_cargo)