from tkinter import *
from tkinter import filedialog
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
        Button(self.root,text="SEARCH AUDIO FILE",width=85,height=2,command=self.open_file).place(x=10,y=100)

        self.root.mainloop()

    def open_file(self):
        audio_file = filedialog.askopenfilename(initialdir = "/",
                     title="Select audio",filetypes = (("mp3 files","*.mp3"),
                     ("wav files","*.wav")))
        if audio_file != "":
            audio_f = (audio_file.split("/"))[-1]
            self.audioName.set(audio_f)
        


if __name__=="__main__":
    editor()

