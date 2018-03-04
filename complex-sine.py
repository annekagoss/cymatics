import pyaudio
import numpy as np
import os
import sys

p = pyaudio.PyAudio()

VOLUME = 0.1     # range [0.0, 1.0]
FS = 44100       # sampling rate, Hz, must be integer
DURATION = 10.0   # in seconds, may be float

def sinewave(frequency):
    return (np.sin(2*np.pi*np.arange(FS*DURATION)*frequency/FS)).astype(np.float32)

def complexTone(frequency):
    return sinewave(frequency) + sinewave(frequency*2) + sinewave(frequency*1.5)

inputFreq = float(sys.argv[1])

# generate samples, note conversion to float32 array
samples = complexTone(inputFreq)

# for paFloat32 sample values must be in range [-1.0, 1.0]
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=FS,
                output=True)

loop = True
# play. May repeat with different volume values (if done interactively)
while loop :
    stream.write(VOLUME*samples)
print stream.read()

stream.stop_stream()
stream.close()

p.terminate()
