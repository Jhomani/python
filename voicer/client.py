import sys
import json
import tkinter as tk
from threading import Thread
from pynput.keyboard import Listener

from pyspeach.Pyspeach import Pyspeach


def showUI(model:str):
  root = tk.Tk()

  inst = tk.Label(
    root,
    anchor='nw',
    justify='left', 
    text=json.dumps(model, indent=4),
    fg="white",
    bg="black",
    width=60,
    height=30)
  inst.pack()
  root.mainloop()

test = Pyspeach()

def onRelease(key):
  try:
    if key.char ==  'r':
      print("\n\nRecording...\n\n")
      test.startSpeech()

    elif key.char ==  's':
      print("\n\nRecording stopped\n\n")
      model = test.stopSpeech()
      if model and not isinstance(model, bool):
        thr = Thread(target=showUI, args=(model,))
        thr.start()

    elif key.char ==  'q':
      model = test.runCommand('/home/jhomani/python/voicer/test.wav')
      if model and not isinstance(model, bool):
        thr = Thread(target=showUI, args=(model,))
        thr.start()

    elif key.char in  ('x', 'd'):
      print(' Bay...')
      sys.exit(-1)

    else:
      raise AttributeError
  except(AttributeError, NameError):
    # print(" Invalid key")
    pass

with Listener(on_release=onRelease) as listener:
  listener.join()
