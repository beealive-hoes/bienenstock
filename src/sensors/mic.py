import sounddevice as sd
import soundfile as sf
from scipy.io.wavfile import read
import math
import statistics
import src.webutils.server as Server
from src.sensors import DEBUG

SAMPLERATE = 44100  # frames per second
RECORD_TIME = 5  # seconds

#
# Diese Messungen ergeben auf keinen Fall eine sinnvolle Einheit, weil wir keine Referenzmessung oder sowas haben.
# Das sollte aber kein Problem darstellen, weil wir nur den Unterschied betrachten wollen.
#


def analyze(file):
    _, wav_data = read(file)
    db = 20 * math.log10(math.sqrt(statistics.mean(wav_data ** 2)))
    return db


def record(seconds, file):
    recording = sd.rec(int(seconds * SAMPLERATE), samplerate=SAMPLERATE, channels=1)
    sd.wait()
    sf.write(file, recording, SAMPLERATE)


def measure():
    record(RECORD_TIME, "../audio/measure.wav")
    data = analyze("../audio/measure.wav")
    Server.upload_data('volume', data)


def debug_record():
    for i in range(5):
        record(RECORD_TIME, f"../audio/test{i}.wav")
        data = analyze(f"../audio/test{i}.wav")
        print(f"{i}.File: {data}")


def debug_last():
    for i in range(5):
        data = analyze(f"../audio/test{i}.wav")
        print(f"{i}.File: {data}")


def main():
    if DEBUG:
        mode = input("new | last: ")
        if mode == "new":
            debug_record()
        elif mode == "last":
            debug_last()
    else:
        measure()


if __name__ == "__main__":
    main()

