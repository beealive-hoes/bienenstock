import time
import RPi.GPIO as GPIO
from src.sensors.hx711 import HX711
import src.webutils.server as Server

ratio = 10  # BERECHNEN mit weight_test.py

GPIO.setmode(GPIO.BCM)
hx = HX711(5, 6)

err = hx.zero()
# check if successful
if err:
    raise ValueError('Tare is unsuccessful.')

hx.set_scale_ratio(ratio)


def measure():
    value = hx.get_weight_mean()
    Server.uploadData("weight", value)


def debug():
    value = hx.get_weight_mean()
    print(value, "g")

