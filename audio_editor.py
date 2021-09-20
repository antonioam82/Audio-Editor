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
        self.audio = ""

        Entry(self.root,textvariable=self.currentDir,width=153).place(x=0,y=0)
        Label(self.root,text="AUDIO TITLE").place(x=10,y=30)
        self.entryName = Entry(self.root,textvariable=self.audioName,width=34,font=('arial 24'))
        self.entryName.place(x=10,y=53)
        #self.durationEntry = Entry(self.root,textvariable=self.duration,width=13,font=('arial 20'),bg="black",fg="red").place(x=690,y=53)
        #Label(self.root,text="DURATION(MINUTES)").place(x=690,y=30)
        Button(self.root,text="SEARCH AUDIO FILE",width=86,height=2,command=self.open_file).place(x=12,y=100)
        Button(self.root,text="EXPORT AS .AU",width=15,height=2).place(x=650,y=177)
        Button(self.root,text="EXPORT AS .AAC",width=15,height=2).place(x=797,y=301)#.place(x=797,y=53)
        Button(self.root,text="EXPORT AS .MP4",width=15,height=2).place(x=650,y=301)#.place(x=650,y=115)
        Button(self.root,text="EXPORT AS .MP2",width=15,height=2).place(x=797,y=239)#.place(x=797,y=115)
        Button(self.root,text="EXPORT AS .OGG",width=15,height=2).place(x=650,y=239)#.place(x=650,y=177)
        Button(self.root,text="EXPORT AS .FLV",width=15,height=2).place(x=797,y=177)#.place(x=797,y=177)
        Button(self.root,text="EXPORT AS .MP3",width=15,height=2).place(x=650,y=115)#.place(x=650,y=239)
        Button(self.root,text="EXPORT AS .WAV",width=15,height=2,command=self.init_task).place(x=797,y=115)#.place(x=797,y=239)
        Button(self.root,text="CHANGE DIRECTORY",width=36,height=2,command=self.change_dir).place(x=650,y=53)#.place(x=650,y=301)
        Button(self.root,text="REVERSE AUDIO",width=35,height=2).place(x=12,y=177)
        Button(self.root,text="METADATA",width=35,height=2).place(x=12,y=239)
        Button(self.root,text="PLAY AUDIO",width=35,height=2).place(x=12,y=301)
        self.slider = Scale(self.root,length=130,bg="light gray",from_=50, to=-50)
        self.slider.set(0)
        self.slider.place(x=300,y=207)
        Label(self.root,text="SPEED UP").place(x=290,y=180)
        self.slider1 = Scale(self.root,length=130,bg="light gray",from_=50, to=1)
        self.slider1.set(1)
        self.slider1.place(x=370,y=207)
        Label(self.root,text="VOLUME").place(x=363,y=180)
        self.slider2 = Scale(self.root,length=130,bg="light gray",from_=50, to=-50)
        self.slider2.place(x=440,y=207)
        Label(self.root,text="GAIN").place(x=443,y=180)
        self.slider3 = Scale(self.root,bg="light gray",length=130, from_=20, to=0)
        self.slider3.place(x=510,y=207)
        Label(self.root,text="FADE IN").place(x=505,y=180)
        self.slider4 = Scale(self.root,bg="light gray",length=130, from_=20, to=0)
        self.slider4.place(x=580,y=207)
        Label(self.root,text="FADE OUT").place(x=570,y=180)

        self.root.mainloop()

    def open_file(self):
        self.audio_file = filedialog.askopenfilename(initialdir = "/",
                     title="Select audio",filetypes = (("mp3 files","*.mp3"),
                     ("wav files","*.wav"),("ogg files","*.ogg"),
                     ("flv files","*.flv"),("mp4 files","*.mp4")))
        if self.audio_file != "":
            audio_f = (self.audio_file.split("/"))[-1]
            name,self.ex = os.path.splitext(audio_f)
            self.audioName.set(audio_f)
            self.import_audio()

    def change_dir(self):
        directory=filedialog.askdirectory()
        if directory != "":
            os.chdir(directory)
            self.currentDir.set(directory)

    def init_task(self):
        t = threading.Thread(target=self.export_audio)
        t.start()

    def export_audio(self):
        self.audio.export("newaudio.wav",format="wav")

    def import_audio(self):
        if self.ex == ".mp3":
            self.audio = AudioSegment.from_mp3(self.audio_file)
        elif self.ex == ".wav":
            self.audio = AudioSegment.from_wav(self.audio_file)
        elif self.ex == ".ogg":
            self.audio = AudioSegment.from_ogg(self.audio_file)
        elif self.ex == ".flv":
            self.audio = AudioSegment.from_flv(self.audio_file)
        else:
            self.audio = AudioSegment.from_file(self.audio_file)
        #self.duration.set(str("{0:.6f}".format(self.audio.duration_seconds/60)))
                                                     
if __name__=="__main__":
    editor()

