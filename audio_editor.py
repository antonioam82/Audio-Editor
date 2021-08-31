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
        self.audioName = StringVar()
        self.duration = IntVar()

        Entry(self.root,textvariable=self.currentDir,width=153).place(x=0,y=0)
        Label(self.root,text="AUDIO TITLE").place(x=10,y=30)
        self.entryName = Entry(self.root,textvariable=self.audioName,width=40,font=('arial 20'))
        self.entryName.place(x=10,y=53)
        self.durationEntry = Entry(self.root,textvariable=self.duration,width=13,font=('arial 20')).place(x=690,y=53)
        Label(self.root,text="DURATION").place(x=690,y=30)

        self.root.mainloop()


if __name__=="__main__":
    editor()

