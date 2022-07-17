import sounddevice as sd
from scipy.io import wavfile

print(sd.query_devices())

sd.default.device[0] = 2

fs = 44100 # Hz
length = 120 # s
recording = sd.rec(frames=fs * length, samplerate=fs, blocking=True, channels=1)
sd.wait()

wavfile.write('Audio.wav', fs, recording)
