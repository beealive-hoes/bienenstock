from picamera import PiCamera
import subprocess
import src.webutils.server as Server
from src.sensors import DEBUG
from sys import argv

directory = "../video/"


def record(recording_time, pieces, pause_id):
    record_and_convert(recording_time, pieces)
    upload(pieces, pause_id)


def record_and_convert(recording_time, pieces):
    with PiCamera(resolution=(1920, 1080), framerate=30) as cam:
        for i in range(pieces):
            file_name = f'{directory}clip{i}.h264'
            print("Start Recording", file_name)
            cam.start_recording(file_name)
            cam.wait_recording(recording_time)
            cam.stop_recording()
            command = f"MP4Box -add {directory}clip{i}.h264 {directory}clip{i}.mp4"
            print(f"Converted {directory}clip{i}.h264 {directory}clip{i}.mp4")
            try:
                output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
            except subprocess.CalledProcessError as e:
                print(f'FAIL:\n cmd:{e.cmd}\n output:{e.output}')


def upload(pieces, pause_id):
    for i in range(pieces):
        Server.upload_video(f"{directory}clip{i}.mp4", f"{pause_id}-{i}")


def debug():
    record_and_convert(10, 3)


def main():
    if DEBUG:
        debug()
    else:
        pause_id = argv[1]
        if pause_id == 1:
            record(60, 15, 1)
        elif pause_id == 2:
            record(60, 15, 2)
        elif pause_id == 3:
            record(60, 45, 2)
        else:
            print("Wrong pause_id.")


if __name__ == "__main__":
    main()
