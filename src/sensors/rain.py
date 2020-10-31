from gpiozero import Button
from webutils.server import Server

rain_sensor = Button(16)
BUCKET_SIZE = 0.2794
count = 0

def bucket_tipped():
    global count
    count = count + 1
    print (count * BUCKET_SIZE)

def reset_rainfall():
    global count
    count = 0

rain_sensor.when_pressed = bucket_tipped

def measure():
    global count
    Server.uploadData("rain",(count*BUCKET_SIZE))

def test():
    global count
    print(count*BUCKET_SIZE + "mm/m2")