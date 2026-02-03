class Car:
    def __init__(self, speed:int = 0, max_speed:int=0, initial_fuel:int=0, max_fuel:int=100):
        self.speed= speed
        self.max_speed= max_speed
        self.fuel_level= initial_fuel
        self.max_fuel_level = max_fuel

    def accelerate(self, change_val:int=1):
        if self.fuel_level > 0:
            self.speed += change_val
            self.fuel_level += -1
            if self.speed > self.max_speed:
                self.speed = self.max_speed
        else:
            self.speed = 0

    def brake(self, change_val:int=-1):
        self.speed += change_val
        if self.speed <= 0:
            self.speed = 0

    def refuel(self, change_val: int=1):
        self.fuel_level += change_val
        if self.fuel_level > self.max_fuel_level:
            self.fuel_level= self.max_fuel_level


