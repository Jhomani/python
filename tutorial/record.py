import pyaudio;
import wave;
from threading import Timer, Thread, Event;
from multiprocessing import Process; 
import time

audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
frames = []

def recordFn(e: Event):
  while(True):
    if not e.isSet():
      data = stream.read(1024)
      frames.append(data)
      # time.sleep(1)
    else:
      stream.stop_stream()
      stream.close()
      audio.terminate()

      sound_file = wave.open('myrecord.wav', 'wb')
      sound_file.setnchannels(1)
      sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
      sound_file.setframerate(44100)
      sound_file.writeframes(b''.join(frames))
      break 

e = Event()
t = Thread(target=recordFn, args=(e,))
t.start()

# wait 5 seconds for the thread to finish its work
t.join(5)
e.set()
print("thread is not done, setting event to kill thread.")

# proc = Process(target=recordFn, args=(e,))
# proc.start()

# def finishRecord(n: int): 
#   print('Finished this task')
#   proc.terminate()

# Timer(2.0, finishRecord, (1,)).start()