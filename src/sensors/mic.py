import sounddevice as sd
import soundfile as sf


import src.webutils.server as Server

fs = 44100


def record(seconds):
    # TO DO lol
    recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()
    Server.uploadData("TODO", recording)


def debug(seconds):
    recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()
    sf.write("test.wav", recording, fs)
