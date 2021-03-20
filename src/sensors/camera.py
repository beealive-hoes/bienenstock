from picamera import PiCamera
import subprocess
import src.webutils.server as Server

cam = PiCamera()
cam.resolution = (1920, 1080)
cam.framerate = 30
directory = "../video/"


def record(recordingTime, pieces, pauseid):
    for filename in cam.record_sequence(directory + 'clip%d.h264' % i for i in range(pieces)):
        cam.wait_recording(recordingTime)

    for i in range(pieces):
        command = f"MP4Box -add {directory}clip{i}.h264 {directory}clip{i}.mp4"
        try:
            output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
            Server.uploadVideo(f"{directory}clip{i}.mp4", f"{pauseid}-{i}")
        except subprocess.CalledProcessError as e:
            print('FAIL:\n cmd:{}\n output:{}'.format(e.cmd, e.output))


def debug():
    for filename in cam.record_sequence(directory + 'clip%d.h264' % i for i in range(5)):
        cam.wait_recording(5)

    for i in range(5):
        command = f"MP4Box -add {directory}clip{i}.h264 {directory}clip{i}.mp4"
        try:
            output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
            print(f"Converted {directory}clip{i}.h264 {directory}clip{i}.mp4")
        except subprocess.CalledProcessError as e:
            print('FAIL:\n cmd:{}\n output:{}'.format(e.cmd, e.output))


if __name__ == "__main__":
    debug()
