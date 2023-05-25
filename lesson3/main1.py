import json
import pyaudio

from vosk import Model, KaldiRecognizer

model = Model('lessons/semester II/lesson3/vosk-model-uk-v3-lgraph')
recognizer = KaldiRecognizer(model, 16000)
worlds = pyaudio.PyAudio()
stream = worlds.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

def listen():
    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if (recognizer.AcceptWaveform(data)) and len(data) > 0:
            answer = json.loads(recognizer.Result())
            if answer['text']:
                yield answer['text']
                

for text in listen():
    if text == 'футбол' or text == 'волейбол' or text == 'баскетбол':
        print(f'PC - Який твій улюблений вид спорту?')
    
        
        
    print(f'User: {text}')




"njdfhgjvbfnnjhkddddddddddddddddddddddddddhgggggggggggggggrjhjdkmxcklebdhjxnfmcdijcxbvnjmfbhjcmvnjkfmcnjvmnf,c"