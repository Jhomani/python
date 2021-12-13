import wave
from threading import Thread, Event
import pyaudio

class Recorder:
  ev: Event
  thr: Thread
  audio: pyaudio.PyAudio
  stream: pyaudio.Stream
  frames = []
  fpath: str

  def __start(self):
    audioAtrr = {
      'format': pyaudio.paInt16,
      'channels': 1,
      'rate': 44100,
      'input':True,
      'frames_per_buffer':1024,
    }

    self.audio = pyaudio.PyAudio()
    self.stream = self.audio.open(**audioAtrr)
    self.frames = []

  def __recordFn(self, _:str):
    while True:
      if not self.ev.isSet():
        data = self.stream.read(1024)
        self.frames.append(data)
      else:
        self.__saveRecord()
        break

  def startRecord(self):
    self.__start()
    self.ev = Event()
    self.thr = Thread(target=self.__recordFn, args=(1,))
    self.thr.start()

  def __saveRecord(self):
    self.stream.stop_stream()
    self.stream.close()
    self.audio.terminate()

    soundFile = wave.open(self.fpath, 'wb')
    soundFile.setnchannels(1)
    soundFile.setsampwidth(self.audio.get_sample_size(pyaudio.paInt16))
    soundFile.setframerate(44100)
    soundFile.writeframes(b''.join(self.frames))
  def stopRecord(self, fpath: str):
    self.fpath = fpath
    self.ev.set()
    self.thr.join()

