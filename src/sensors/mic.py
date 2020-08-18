import sounddevice as sd
import scipy.io.wavfile as wav
import wave
import struct
from webutils.server import Server

fs = 44100


def record(seconds):
    recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()
    amount = len(recording)
    summ = sum(recording)/amount*fs
    return summ[0]