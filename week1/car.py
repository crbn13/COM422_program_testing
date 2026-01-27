class Car:
    def __init__(self):
        self.speed: float=0
        self.acceleration: float=0
        self.fuel_level: float=0
        self.distance: float=0

    def step_time(self, mstime:float=100):
        if self.fuel_level < 0:
            self.fuel_level = 0
        else:
            self.speed += self.acceleration * mstime
            self.distance += self.speed * mstime
            if self.acceleration > 0:
                self.fuel_level -= self.fuel_level - mstime*self.acceleration

    def set_accel(self, acceleration:float=0):
        self.acceleration = acceleration

    def brake(self):
        self.set_accel()
        speed = speed -1

    def refuel(self):
        self.fuel_level += 1


