import time
from src.sensors.hx711 import HX711
import src.webutils.server as Server
from src.sensors.GPIOPINS import pins

ratio = 10  # BERECHNEN mit weight_test.py

hx = HX711(dout_pin=pins['HX711_DT'], pd_sck_pin=pins['HX711_SCK'])

err = hx.zero()
# check if successful
if err:
    raise ValueError('Tare is unsuccessful.')

hx.set_scale_ratio(ratio)


def measure():
    value = hx.get_weight_mean()
    Server.upload_data("weight", value)


def debug():
    value = hx.get_weight_mean()
    print(value, "g")

