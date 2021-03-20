from gpiozero import Button
import time
import math
import src.webutils.server as Server
from src.sensors.GPIOPINS import pins

radius_cm = 9.0  # Radius of your anemometer
wind_interval = 5  # How often (secs) to report speed
calibration = 1.18


# Calculate the wind speed
def calculate_speed(time_sec, wind_count):
    circumference_cm = (2 * math.pi) * radius_cm
    rotations = wind_count / 2.0

    # Calculate distance travelled by a cup in cm
    dist_km = (circumference_cm * rotations) / 100000  #

    speed = (dist_km / time_sec) * 3600

    return speed * calibration


def justMeasure():
    wind_speed_sensor = Button(pins['WINDSPEED'])
    wind_count = 0
    stopTime = time.time()+5
    while time.time() < stopTime:
        if wind_speed_sensor.is_pressed:
            wind_count += 1
    return wind_count


# Loop to measure wind speed and report at 5-second intervals
def measure():
    wind_count = justMeasure()
    Server.uploadData("wind", calculate_speed(wind_interval, wind_count))


def debug():
    wind_count = justMeasure()
    print("wind", calculate_speed(wind_interval, wind_count))


if __name__ == "__main__":
    while True:
        debug()
