from gpiozero import Button
import src.webutils.server as Server
from src.sensors.GPIOPINS import pins

rain_sensor = Button(pins['RAIN'])
BUCKET_SIZE = 0.2794
count = 0


def bucket_tipped():
    global count
    count = count + 1
    print(count * BUCKET_SIZE)


def reset_rainfall():
    global count
    count = 0


rain_sensor.when_pressed = bucket_tipped


def measure():
    global count
    Server.uploadData("rain", (count * BUCKET_SIZE))


def debug():
    global count
    print(str(count * BUCKET_SIZE) + "mm/m2")
