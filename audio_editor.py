from tkinter import *
import os
import threading
from pydub import AudioSegment

class editor():
    def __init__(self):
        self.root = Tk()
        self.root.geometry('920x410')
        self.root.title("Audio Editor")

        self.root.mainloop()


if __name__=="__main__":
    editor()
