import soundfile as sf
import numpy as np

data,fs=sf.read('./REC001.WAV')
data2=np.mean(data,axis=1)
sf.write('95-1-mono.wav',data2,fs)


import webrtcvad
!python3 ~/py-webrtcvad/example.py 3 ../95-1-mono.wav

import os
import librosa

for file in os.listdir('./chunks-1/'):
    if file[-3:] == 'wav':
        x, sr = librosa.load('./chunks-1/'+ file, mono=True,sr=None)
        if max(x) < 0.35:
            print(file)
            os.remove('./chunks-1/'+ file) 
        
        