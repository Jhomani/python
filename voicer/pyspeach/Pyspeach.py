import speech_recognition as sr
from pyspeach.src import Recorder, ConnectSQL, playAudio, parser

class Pyspeach:
  __FILENAME: str
  _recorder: Recorder
  _sql: ConnectSQL
  _dicionary = {}

  def __init__(self) -> None:
    self.__FILENAME = '/tmp/recorded.wav'
    self._recorder = Recorder()

    self._sql = ConnectSQL('root', 'Test1235', 'Metodos')

    self._dicionary =  {
      'delete': 'eliminar',
      'update': 'actualizar',
      'get': 'obtener',
      'source': 'tabla',
    }


  def startSpeech(self):
    self._recorder.startRecord()

  def stopSpeech(self):
    self._recorder.stopRecord(self.__FILENAME)

    rec = sr.Recognizer()

    with sr.AudioFile(self.__FILENAME) as source:
      rec.adjust_for_ambient_noise(source=source)
      audioData = rec.record(source)

      text = rec.recognize_google(audioData, language="es-ES")
      print(text)

      return self.handleText(text)

  def handleText(self, txt: str):
    result = False
    parsed = parser(txt, self._dicionary)

    if parsed:

      if parsed[0] == self._dicionary['delete']:
        result = self._sql.deleteById(parsed[1], parsed[2])
      elif parsed[0] == self._dicionary['get']:
        result = self._sql.getById(parsed[1], parsed[2])
      elif parsed[0] == self._dicionary['update']:
        result = self._sql.updateById(1, 'Producto', 'nombre', 'Windows 10')

      if result:
        playAudio('success')
      else:
        playAudio('failed')

      print(parsed)
    else:
      playAudio('failed')

    return result

  def runCommand(self, audiopath: str):
    rec = sr.Recognizer()

    with sr.AudioFile(audiopath) as source:
      rec.adjust_for_ambient_noise(source=source)
      audioData = rec.record(source)

      text = rec.recognize_google(audioData, language="es-ES")
      print(text)

      return self.handleText(text)

  def setDeleteAct(self, cmd: str):
    self._dicionary['delete'] = cmd

  def setUpdateAct(self, cmd: str):
    self._dicionary['update'] = cmd

  def setGetAct(self, cmd: str):
    self._dicionary['get'] = cmd
