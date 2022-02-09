import threading
import pyttsx3
from PyQt5.QtGui import *
from PyQt5.QtCore import *
#################Voice setting
engine = pyttsx3.init()
rate = engine.getProperty('rate')   # getting details of current speaking rate                    #printing current voice rate
engine.setProperty('rate', 200)     # setting up new voice rate

##################Volume 
"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)                     #printing current volume level
engine.setProperty('volume',1)    # setting up volume level  between 0 and 1

#####################################Voice 
"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice

#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[0].id)   #changing index, changes voices. 1 for female
###################Finish


class SpeechRunnable(QRunnable):
    def __init__(self):
        QRunnable.__init__(self)
    def run(self):
        try:
            
            engine.say(self.chat_speech)
            engine.runAndWait()
        except:
            pass

    def say(self, text):
        self.chat_speech = text
        QThreadPool.globalInstance().start(self)

    def stop(self):
        engine.stop()

def threadedsay(_str):
    runnable = SpeechRunnable()
    runnable.say(_str)

engine.runAndWait()