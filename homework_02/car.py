from homework_02.base import Vehicle
from homework_02.engine import Engine

class Car(Vehicle):

    engine = None

    def set_engine(self, engine_object):

        self.engine = engine_object


# car = Car(1200, 50, 6)
# engine = Engine
# car.set_engine(engine)
# print(car.engine.pistons)
# print(car.engine.volume)

