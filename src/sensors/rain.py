from gpiozero import Button
import src.webutils.server as Server
from src.sensors.GPIOPINS import pins
import json

rain_sensor = Button(pins['RAIN'])
BUCKET_SIZE = 0.2794
try:
    with open("rain.json") as file:
        countDict = json.load(file)
except (json.decoder.JSONDecodeError, FileNotFoundError):
    countDict = {
        "count": 0
    }


def bucket_tipped():
    countDict["count"] += 1
    with open("rain.json", 'w') as jsonFile:
        json.dump(countDict, jsonFile, indent=1)


def reset_rainfall():
    countDict["count"] = 0
    with open("rain.json", 'w') as jsonFile:
        json.dump(countDict, jsonFile, indent=1)


rain_sensor.when_pressed = bucket_tipped


def measure():
    Server.uploadData("rain", (countDict["count"] * BUCKET_SIZE))


def debug():
    print(str(countDict["count"] * BUCKET_SIZE), "mm/m2")


if __name__ == "__main__":
    while True:
        debug()
