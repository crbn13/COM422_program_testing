import pytest
from car import Car
import inspect

def test_car_constructor():
    obj = Car(3, 44, 10, 100)
    assert obj.speed == 3
    assert obj.max_speed == 44
    assert obj.fuel_level == 10
    assert obj.max_fuel_level == 100
    # print(str(inspect.stack()[0][3]) + "() | ", "Test passed")

def test_car_accelerate():
    obj = Car(3, 44, 10, 100)
    obj.accelerate()
    assert obj.speed == 4

def test_sad_fuel():
    obj = Car(3, 44, 10, 100)
    