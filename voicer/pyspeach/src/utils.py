import re
import wave
import os
import pyaudio

def formatResDict(attr, val: tuple) -> dict:
  res = {}
  size = len(attr)

  for i in range(size):
    res[attr[i]] = val[i]

  return res

def formatResList(attr: tuple, val):
  res = []

  for i in val:
    res.append(formatResDict(attr, i))

  return res

def parser(token: str, dic: tuple) -> tuple:
  res = None

  actions = f"({dic['delete']}|{dic['update']}|{dic['get']})"
  regex = f"({actions}).*[0-9]+.*({dic['source']}|de) ([a-z]+)$"

  matched = re.search(regex, token)

  if matched:
    [action] = re.findall(actions, token)
    [key] = re.findall('[0-9]+', token)
    [table] = re.findall(r'\s([a-zA-Z]+)$', token)

    res = (action,int(key), table.capitalize() )

  return res

def playAudio(mode: str) -> None:
  chunk = 1024

  pwd = os.path.dirname(__file__)
  path = os.path.join(pwd, f'../assets/{mode}.wav')

  aud = wave.open(os.path.normpath(path), 'rb')
  pydio = pyaudio.PyAudio()

  audioAtrr = {
    'format': pydio.get_format_from_width(aud.getsampwidth()),
    'channels': aud.getnchannels(),
    'rate': aud.getframerate(),
    'output':True,
  }

  stream = pydio.open(**audioAtrr)

  data = aud.readframes(chunk)

  while len(data) > 0:
    stream.write(data)
    data = aud.readframes(chunk)

  stream.stop_stream()
  stream.close()

  pydio.terminate()
