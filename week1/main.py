import tkinter as tk 
from car import Car
import time

carobj = Car()
carobj.acceleration=.01

while True:
    print("speed =",carobj.speed)
    print("distance =",carobj.distance)
    print("acceleration =",carobj.acceleration)
    carobj.step_time(1)
    time.sleep(1)