from picamera import PiCamera
from time import sleep

cam = PiCamera()
cam.resolution = (1920, 1080)
cam.framerate = 15


cam.start_preview()
cam.start_recording('/media/pi/9401-7CA11/aufnahme.mp4')
sleep(5)
cam.stop_recording()
cam.stop_preview()