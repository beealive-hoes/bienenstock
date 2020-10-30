from gpiozero import Button
import time
import math
from webutils.server import Server

wind_count = 0       # Counts how many half-rotations
radius_cm = 9.0 # Radius of your anemometer
wind_interval = 5    # How often (secs) to report speed
calibration = 1.18


# Every half-rotation, add 1 to count
def spin():
	global wind_count
	wind_count = wind_count + 1
	# print("spin" + str(wind_count))

# Calculate the wind speed
def calculate_speed(time_sec):
        global wind_count
        global calibration
        circumference_cm = (2 * math.pi) * radius_cm
        rotations = wind_count / 2.0

        # Calculate distance travelled by a cup in cm
        dist_km = (circumference_cm * rotations) / 100000 #

        speed = (dist_km / time_sec) * 3600

        return speed * calibration


wind_speed_sensor = Button(26)
wind_speed_sensor.when_pressed = spin

# Loop to measure wind speed and report at 5-second intervals
def measure():
        wind_count = 0
        time.sleep(wind_interval)
        Server.uploadData("windspeed",calculate_speed(wind_interval))
