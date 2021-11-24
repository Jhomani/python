import pyaudio
import wave
import sys

CHUNK = 1024

age:int = 23

if len(sys.argv) < 2:
  print(f'Plays a wave file.\n\nUsage: {sys.argv[0]} filename.wav')
  sys.exit(-1)

wf = wave.open(sys.argv[1], 'rb')

# instantiate PyAudio (1)
p = pyaudio.PyAudio()

# open stream (2)
stream = p.open(
  format=p.get_format_from_width(wf.getsampwidth()),
  channels=wf.getnchannels(), 
  rate=wf.getframerate(),
  output=True
)

# read data
data = wf.readframes(CHUNK)

# play stream (3)
while len(data) > 0:
  stream.write(data)
  data = wf.readframes(CHUNK)

# stop stream (4)
stream.stop_stream()
stream.close()

# close PyAudio (5)
p.terminate()