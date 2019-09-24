import io
import os

# Imports the Google Cloud client library
from google.cloud import speech_v1p1beta1 as speech
from google.cloud.speech_v1p1beta1 import enums
from google.cloud.speech_v1p1beta1 import types

# Instantiates a client
client = speech.SpeechClient()

audio = types.RecognitionAudio(uri="gs://wgils-speech/61-1-mono.wav")
config = types.RecognitionConfig(
    encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=48000,
    language_code='en-US',
    enable_speaker_diarization = True,
    enable_automatic_punctuation=True,
    #use_enhanced = True,
    #model='phone_call',
    enable_word_time_offsets=True,
    diarization_speaker_count = 2)

operation = client.long_running_recognize(config, audio)
response = operation.result(timeout=10000)

result = response.results[-1]
words_info = result.alternatives[0].words
len(words_info)

transcript = ""
punct = [".","?"]
for word_info in words_info:
		timestamp  = word_info.start_time.seconds + word_info.start_time.nanos * 1e-9 
	if len(transcript)==0 or transcript[-2] in punct:
		transcript += "\n"
		if(word_info.speaker_tag==0): 
			transcript+= str(timestamp) + " " + "0: " + word_info.word + " "
		if(word_info.speaker_tag==1): 
			transcript+= str(timestamp) + " " + "1: " + word_info.word + " "
		if(word_info.speaker_tag==2):  
			transcript+= str(timestamp) + " " + "2: "+word_info.word+" "
		if(word_info.speaker_tag==3): 
			transcript+= str(timestamp) + " " + "3: "+word_info.word+" "
	else:
		transcript += word_info.word+" "
		print(word_info.word)

f= open("./transcriptions/ingrid-61/transcript_complete","w+")
f.write(transcript)
f.close()

results = response.results
transcript2 = ""
punt = [".","?"]
for result in results:
	words_info = result.alternatives[0].words
	for word_info in words_info:
		timestamp  = word_info.start_time.seconds + word_info.start_time.nanos * 1e-9 
		if len(transcript2)==0 or transcript2[-2] in punct:
			transcript2 += "\n"
			if(word_info.speaker_tag==0): 
				transcript2+=str(timestamp) + " " + "0: "+word_info.word+" "
			if(word_info.speaker_tag==1): 
				transcript2+=str(timestamp) + " " + "1: "+word_info.word+" "
			if(word_info.speaker_tag==2): 
				transcript2+=str(timestamp) + " " + "2: "+word_info.word+" "
			if(word_info.speaker_tag==3): 
				transcript2+=str(timestamp) + " " + "3: "+word_info.word+" "
		else:
			transcript2 += word_info.word+" "
			print(word_info.word)
f= open("./transcriptions/ingrid-61/justincase.txt","w+")
f.write(transcript2)
f.close()
