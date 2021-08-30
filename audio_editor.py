from tkinter import *
import os
import threading
from pydub import AudioSegment

class editor():
    def __init__(self):
        self.root = Tk()
        self.root.geometry('923x410')
        self.root.title("Audio Editor")

        self.currentDir = StringVar()
        self.currentDir.set(os.getcwd())

        Entry(self.root,textvariable=self.currentDir,width=153).place(x=0,y=0)

        self.root.mainloop()


if __name__=="__main__":
    editor()
