from modules.Observer import Subject
import sqlite3, os
import numpy as np
from scipy.io.wavfile import write
import matplotlib.pyplot as plt


class Model(Subject):

    def __init__(self):
        Subject.__init__(self)

    def create_note(self, octa, note, is_pure_note, is_harmonic, duration=1):
        connect = sqlite3.connect("frequencies.db")
        cursor  = connect.cursor()
        freqs   = cursor.execute("SELECT * FROM frequencies")
        notes   = ["oct", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
        index   = notes.index(note)

        file_path   = 'Sounds/{}{}.wav'.format(note, int(octa))

        for f in freqs:
            freq = f[index]*(2**(int(octa)-3))
            print(freq)

        fs          = 44100     # sampling rate, Hz, must be integer
        duration    = 1.0       # in seconds, may be float

        if(is_pure_note):
            left_audio  = (np.sin(2*np.pi*np.arange(fs*duration)*freq/fs)).astype(np.float32)
            righ_audio  = (np.sin(2*np.pi*np.arange(fs*duration)*freq/fs)).astype(np.float32)
            audio       = np.stack((left_audio, righ_audio), axis=1)

            write(file_path, fs, audio)

        if(is_harmonic):
            pass

        self.notify()