import time

import numpy as np
from scipy.io.wavfile import write
from playsound import playsound

DURATION_BEEP = 0.070
SPS = 44100
FREQ_HZ = 600

def create_wave(sps, freq_hz, duration_s, filename):
    each_sample_number = np.arange(duration_s * sps)
    waveform = np.sin(2 * np.pi * each_sample_number * freq_hz / sps)
    waveform_quiet = waveform * 0.3
    waveform_integers = np.int16(waveform_quiet * 32767)
    write(filename+".wav", sps, waveform_integers)

duration_s_short = DURATION_BEEP
duration_s_long = 3*DURATION_BEEP

create_wave(SPS, FREQ_HZ, duration_s_short, "short_beep")
create_wave(SPS, FREQ_HZ, duration_s_long, "long_beep")

def short_beep():
    playsound("short_beep.wav")

def long_beep():
    playsound("long_beep.wav")

