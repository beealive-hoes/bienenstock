from gpiozero import Button
import src.webutils.server as Server
from src.sensors.GPIOPINS import pins
from src.sensors import DEBUG
import pickle

rain_sensor = Button(pins['RAIN'])
BUCKET_SIZE = 0.2794
try:
    with open("rain.pickle", 'rb') as file:
        count_dict = pickle.load(file)
except (pickle.UnpicklingError, FileNotFoundError):
    count_dict = {
        "count": 0
    }


def bucket_tipped():
    count_dict["count"] += 1
    with open("rain.pickle", 'wb') as pickleFile:
        pickle.dump(count_dict, pickleFile)


def reset_rainfall():
    count_dict["count"] = 0
    with open("rain.pickle", 'wb') as pickleFile:
        pickle.dump(count_dict, pickleFile)


def measure():
    Server.upload_data("rain", (count_dict["count"] * BUCKET_SIZE))


def debug():
    print(str(count_dict["count"] * BUCKET_SIZE), "mm/m2")


def main():
    while True:
        rain_sensor.wait_for_press()
        bucket_tipped()
        if DEBUG:
            debug()


if __name__ == "__main__":
    main()
    # TODO reset rainfall zum funktionieren bringen
