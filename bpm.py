import wave
import math
import time
import sys
import array
import numpy
import argparse
from scipy import signal
import matplotlib.pyplot as plt


def read_wav(filename):
    song = wave.open(filename,'r')
    frames = song.getnframes()
    fps = song.getframerate()
    samps = list(array.array('i',song.readframes(frames)))
    print samps
    #return samps, fps


print read_wav("song.wav")