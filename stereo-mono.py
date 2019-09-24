import soundfile as sf
import numpy as np
data,fs=sf.read('./REC001.WAV')
data2=np.mean(data,axis=1)


filename = '74-3-mono.wav'
sf.write(filename, data2, fs)


from google.cloud import storage

filename = '95-2-mono.wav'
storage_client = storage.Client()
bucket = storage_client.get_bucket('wgils-speech')
blob = bucket.blob(filename)
blob.upload_from_filename('/voicedata/Recorders/95/RECORD/'+filename)

