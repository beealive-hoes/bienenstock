from picamera import PiCamera
import subprocess
from webutils.server import Server
cam = PiCamera()
cam.resolution = (1920, 1080)
cam.framerate = 30


def record(recordingTime, pieces):
    directory = "./video/"
    for filename in cam.record_sequence(directory + 'clip%d.h264' % i for i in range(pieces)):
        cam.wait_recording(recordingTime)
    
    for i in range(pieces):
        from subprocess import CalledProcessError
        command = "MP4Box -add " + directory + "clip%d.h264 " % i + directory + "clip%d.mp4" % i
        try:
            output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
            Server.uploadVideo(directory + "clip%d.mp4" % i)
        except subprocess.CalledProcessError as e:
            print('FAIL:\n cmd:{}\n output:{}'.format(e.cmd, e.output))