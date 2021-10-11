from tkinter import *
from tkinter import filedialog, messagebox
import tkinter.scrolledtext as sct
import os
from pygame import mixer
import threading
from pydub import AudioSegment

class editor():
    def __init__(self):
        self.root = Tk()
        self.root.geometry('923x375')
        self.root.title("Audio Editor")
        self.root.configure(bg="gray28")

        self.currentDir = StringVar()
        self.currentDir.set(os.getcwd())
        self.audioName = StringVar()
        self.audio = ""
        self.history = ""
        self.playing = False
        mixer.init()

        Entry(self.root,textvariable=self.currentDir,width=153).place(x=0,y=0)
        Label(self.root,text="AUDIO TITLE",fg="white",bg="gray28").place(x=10,y=30)
        self.entryName = Entry(self.root,textvariable=self.audioName,bg="black",fg="green",width=34,font=('arial 24'))
        self.entryName.place(x=10,y=53)
        #self.durationEntry = Entry(self.root,textvariable=self.duration,width=13,font=('arial 20'),bg="black",fg="red").place(x=690,y=53)
        #Label(self.root,text="DURATION(MINUTES)").place(x=690,y=30)
        Button(self.root,text="SEARCH AUDIO FILE",width=86,height=2,bg="gray70",command=self.open_file).place(x=12,y=100)
        Button(self.root,text="EXPORT AS .AU",width=15,height=2,bg="red",fg="white",command=lambda:self.init_task("au")).place(x=650,y=177)
        Button(self.root,text="EXPORT AS .AAC",width=15,height=2,bg="red",fg="white",command=lambda:self.init_task("aac")).place(x=797,y=301)#.place(x=797,y=53)
        Button(self.root,text="EXPORT AS .MP4",width=15,height=2,bg="red",fg="white",command=lambda:self.init_task("mp4")).place(x=650,y=301)#.place(x=650,y=115)
        Button(self.root,text="EXPORT AS .MP2",width=15,height=2,bg="red",fg="white",command=lambda:self.init_task("mp2")).place(x=797,y=239)#.place(x=797,y=115)
        Button(self.root,text="EXPORT AS .OGG",width=15,height=2,bg="red",fg="white",command=lambda:self.init_task("ogg")).place(x=650,y=239)#.place(x=650,y=177)
        Button(self.root,text="EXPORT AS .FLV",width=15,height=2,bg="red",fg="white",command=lambda:self.init_task("flv")).place(x=797,y=177)#.place(x=797,y=177)
        Button(self.root,text="EXPORT AS .MP3",width=15,height=2,bg="red",fg="white",command=lambda:self.init_task("mp3")).place(x=650,y=115)#.place(x=650,y=239)
        Button(self.root,text="EXPORT AS .WAV",width=15,height=2,bg="red",fg="white",command=lambda:self.init_task("wav")).place(x=797,y=115)#.place(x=797,y=239)
        self.btnPlay = Button(self.root,text="PLAY AUDIO",width=36,height=2,bg="gray70",command=self.init_task2)
        self.btnPlay.place(x=650,y=53)#.place(x=650,y=301)
        Button(self.root,text="REVERSE AUDIO",width=35,height=2,bg="light green",command=self.reverse_audio).place(x=12,y=177)
        Button(self.root,text="CLEAR CHANGES",width=35,height=2,bg="light green",command=self.clear_changes).place(x=12,y=239)
        Button(self.root,text="HISTORY",width=35,height=2,bg="light green",command=self.show_history).place(x=12,y=301)
        self.stateLabel = Label(self.root,text="",width=86,bg="gray28",fg="light blue")
        self.stateLabel.place(x=14,y=148)
        self.slider = Scale(self.root,length=130,bg="gray25",fg="white",from_=2.00, to=0.01, digits = 3, resolution = 0.01)
        self.slider.set(1.00)
        self.slider.place(x=290,y=207)
        Label(self.root,text="SPEED",fg="white",bg="gray28").place(x=295,y=180)
        self.slider1 = Scale(self.root,length=130,bg="gray25",fg="white",from_=50, to=-50)
        self.slider1.set(1)
        self.slider1.place(x=360,y=207)
        Label(self.root,text="VOLUME",fg="white",bg="gray28").place(x=357,y=180)
        self.slider2 = Scale(self.root,length=130,bg="gray25",fg="white",from_=50, to=1)
        self.slider2.place(x=437,y=207)
        Label(self.root,text="GAIN",fg="white",bg="gray28").place(x=438,y=180)
        self.slider3 = Scale(self.root,bg="gray25",fg="white",length=130, from_=500, to=1)
        self.slider3.place(x=510,y=207)
        Label(self.root,text="FADE IN",fg="white",bg="gray28").place(x=505,y=180)
        self.slider4 = Scale(self.root,bg="gray25",fg="white",length=130, from_=500, to=1)
        self.slider4.place(x=580,y=207)
        Label(self.root,text="FADE OUT",fg="white",bg="gray28").place(x=570,y=180)

        self.root.mainloop()

    def open_file(self):
        self.audio_file = filedialog.askopenfilename(initialdir = "/",
                     title="Select audio",filetypes = (("mp3 files","*.mp3"),
                     ("wav files","*.wav"),("ogg files","*.ogg"),
                     ("flv files","*.flv"),("mp4 files","*.mp4")))
        if self.audio_file != "":
            self.audio_f = (self.audio_file.split("/"))[-1]
            self.name,self.ex = os.path.splitext(self.audio_f)
            self.audioName.set(self.audio_f)
            self.import_audio()

    def change_audio_characts(self):
        speed = self.slider.get()
        self.audio = (self.audio._spawn(self.audio.raw_data, overrides={"frame_rate": int(self.audio.frame_rate * speed)})).fade_out(self.slider4.get()).fade_in(self.slider3.get()
                        ).apply_gain(self.slider2.get())+self.slider1.get()
        
        return (self.audio.set_frame_rate(self.audio.frame_rate))
            
    def play_audio(self):
        if self.audio != "":
            if "preview.wav" in os.listdir():
                mixer.music.unload()
                os.remove("preview.wav")
            self.change_audio_characts()
            self.audio.export("preview.wav",format="wav")
            pos_time = mixer.music.get_pos()
            mixer.music.load("preview.wav")
            mixer.music.play()
            self.update_state()

    def update_state(self):
        pos_time = mixer.music.get_pos()
        if pos_time != -1:
            self.btnPlay.configure(text="STOP AUDIO")
            self.btnPlay.configure(command=self.stop_audio)
            print("PLAYING")
            self.root.after(500, self.update_state)
        else:
            print("NOT PLAYING")
            self.btnPlay.configure(text="PLAY AUDIO")
            self.btnPlay.configure(command=self.play_audio)
            self.root.after_cancel(self.update_state)
            #mixer.quit()

    def stop_audio(self):
         mixer.music.stop()
         self.btnPlay.configure(text="PLAY AUDIO")
         self.btnPlay.configure(command=self.play_audio)


    def init_task2(self):
        t = threading.Thread(target=self.play_audio)
        t.start()

    def show_history(self):
        if self.history != "":
            top = Toplevel()
            top.title("EDITION HISTORY")
            self.display = sct.ScrolledText(master=top,width=90,height=30,bg="gray91")
            self.display.pack(padx=0,pady=0)
            self.display.insert(END,self.history)
            Button(top,text="CLEAR HISTORY",bg="gray70",command=self.clear_history).pack(side=BOTTOM)

    def clear_history(self):
        self.display.delete('1.0',END)
        
    def clear_changes(self):
        if self.audio != "":
            self.audio = self.original_audio
            self.slider.set(1.00)
            self.slider2.set(1)
            self.slider4.set(1)
            self.slider3.set(1)
            self.slider1.set(1)
            self.stateLabel.configure(text="RESTORED ORIGINAL AUDIO")
            self.history = self.history+("---->RESTORED ORIGINAL AUDIO.\n")

    def init_task(self,ex):
        if self.audio != "":
            self.extension = ex
            t = threading.Thread(target=self.export_audio)
            t.start()

    def reverse_audio(self):
        if self.audio != "":
            try:
                self.audio = self.audio.reverse()
                self.history=self.history+"---->AUDIO REVERSED.\n"
                self.stateLabel.configure(text="REVERSED")
            except Exception as e:
                messagebox.showwarning("UNEXPECTED ERROR",str(e))
                self.history = self.history+("---->UNEXPECTED ERROR: {}.".format(str(e)))+"\n"

    def export_audio(self):
        self.stateLabel.configure(text="SAVING FILE")
        try:
            self.change_audio_characts()
            self.history = self.history+"---->APPLIED AUDIO CHARACTS.\n"
            file = filedialog.asksaveasfilename(initialdir="/",initialfile=self.name,
                    title="SAVE AS",defaultextension="."+self.extension)
            if file != "":
                self.audio.export(file,format=self.extension)
                messagebox.showinfo("SAVED FILE","Saved file in: {}.".format(file))
                self.history = self.history+("---->SAVED FILE IN: {}.".format(file))+"\n"
        except Exception as e:
            messagebox.showwarning("UNEXPECTED ERROR",str(e))
            self.history=self.history+"---->UNEXPECTED ERROR: {}.\n".format(str(e))
            
        self.stateLabel.configure(text="")

    def import_audio(self):
        try:
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
            self.history = self.history+("\n-->LOADED: {}.".format(self.audio_f))+"\n"
            self.original_audio = self.audio
        except Exception as e:
            messagebox.showwarning("UNEXPECTED ERROR",str(e))
            self.history = self.history+("---->UNEXPECTED ERROR: {}.".format(str(e)))+"\n"
            self.audio = ""
                                                     
if __name__=="__main__":
    editor()


    

