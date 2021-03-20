import sounddevice as sd
import soundfile as sf
from scipy.io.wavfile import read
import math
import statistics
import src.webutils.server as Server

SAMPLERATE = 44100  # frames per second
RECORD_TIME = 5  # seconds

#
# Diese Messungen ergeben auf keinen Fall eine sinnvolle Einheit, weil wir keine Referenzmessung oder sowas haben.
# Das sollte aber kein Problem darstellen, weil wir nur den Unterschied betrachten wollen.
#


def analyze(file):
    samprate, wavdata = read(file)
    db = 20 * math.log10(math.sqrt(statistics.mean(wavdata ** 2)))
    return db


def record(seconds, file):
    recording = sd.rec(int(seconds * SAMPLERATE), samplerate=SAMPLERATE, channels=1)
    sd.wait()
    sf.write(file, recording, SAMPLERATE)


def measure():
    record(RECORD_TIME, "../audio/measure.wav")
    data = analyze("../audio/measure.wav")
    Server.uploadData('volume', data)


def debugRecord():
    for i in range(5):
        record(RECORD_TIME, f"../audio/test{i}.wav")
        data = analyze(f"../audio/test{i}.wav")
        print(f"{i}.File: {data}")


def debugLast():
    for i in range(5):
        data = analyze(f"../audio/test{i}.wav")
        print(f"{i}.File: {data}")


if __name__ == "__main__":
    mode = input("new | last: ")
    if mode == "new":
        debugRecord()
    elif mode == "last":
        debugLast()
