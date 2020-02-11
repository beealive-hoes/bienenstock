from picamera import PiCamera
import subprocess

cam = PiCamera()
cam.resolution = (1920, 1080)
cam.framerate = 30

def record(recordingTime):
    cam.start_recording('/media/pi/9401-7CA11/recording.h264') #9401-7CA11 ersetzen durch den Ordner der SSD
    cam.wait_recording(recordingTime)
    cam.stop_recording()

    from subprocess import CalledProcessError
    command = "MP4Box -add /media/pi/9401-7CA11/recording.h264 /media/pi/9401-7CA11/recording.mp4"
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError as e:
        print('FAIL:\n cmd:{}\n output:{}'.format(e.cmd, e.output))
