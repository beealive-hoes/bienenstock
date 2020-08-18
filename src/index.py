import sensors.camera as camera
import sensors.multisensor as multi
import sensors.rain as rain
import sensors.mic as mic
import sensors.windspeed as wind
import schedule
import time

def main():
  camera.record(5, 2)

if __name__ == '__main__':
  main()
