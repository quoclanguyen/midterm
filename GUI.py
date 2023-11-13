from tkinter import messagebox
from tkinter.font import Font
from tkinter import *
from tkinter import filedialog as fd
from video_analyzer import analyzer
from microphone import microphone
import subprocess
import os
import glob

margin = 0
filename = None

def deleteFrames():
    repo = [
        glob.glob('frames/normal/*'),
        glob.glob('frames/gray/*'),
        glob.glob('frames/reversed/*'),
        glob.glob('audio/*')
    ]
    for file in repo[-1]:
        os.remove(file)
    for folder in repo:
        for file in folder:
            os.remove(file)
    messagebox.showinfo(
            icon = "info", 
            title = 'Notification', 
            message = 'Deleted all frames')
def addThenPlaceBtn(GUI, xx, yy, context, back, fore, cmd, txt_font, varText = None):
    global margin
    retBtn = Button(width = GUI.width // 70, height = GUI.height // 1000, master = GUI.window, text = context, bg = back, fg = fore, font = txt_font, command = cmd)
    if not varText:
        retBtn.configure(textvariable = varText)
    retBtn.place(x = xx, y = yy)
    margin += 80
    return retBtn
def openFile():
    global filename
    accepted_ft = [
        ('Supported video files', '*.mp4 *.wav *.avi'),
        ('MP4 images', '*.mp4'),
        ('WAV images', '*.wav'),
        ('AVI images', '*.avi')
    ]
    filename = fd.askopenfilename(title = 'Open a file', initialdir = './', filetypes = accepted_ft)
    if len(filename) != 0:
        messagebox.showinfo(
            icon = "info", 
            title='Notification', 
            message='Opened {} successfully'.format(filename))
        return
    messagebox.showinfo(
        icon = "error", 
        title='Notification', 
        message='Cannot open selected file!')

def openFramesFolder():
    subprocess.Popen('explorer "frames"')


class GUI:
    def __init__(self, window, width, height, caption):
        self.txt_font = Font(family='EB Garamond', size=18, weight='bold')
        self.window = window
        self.width = width
        self.height = height
        self.caption = caption
        self.option = ""
        self.stop = False
        self.window.bind("<KeyPress-q>", self.quitting)
    def quitting(self, *e):
        self.stop = True
    def drawMainFrame(self):
        SCREEN_WIDTH = self.window.winfo_screenwidth()
        SCREEN_HEIGHT = self.window.winfo_screenheight()
        winx = (SCREEN_WIDTH - self.width)//2
        winy = (SCREEN_HEIGHT - self.height)//2
        self.startx = winx // 8
        self.starty = winy // 10
        self.window.title(self.caption)
        self.window.geometry("{}x{}+{}+{}".format(self.width, self.height, winx, winy))
        self.window.configure(bg = '#262626')
    def drawButtons(self):
        addThenPlaceBtn(
            self, self.startx, self.starty,
            "Open file", "#F48749", "#FDF0E8", openFile, self.txt_font)
        addThenPlaceBtn(
            self, self.startx, self.starty + margin,
            "Cut frame", "#151C47", "#C6CCDA", self.cutFrame, self.txt_font)
        addThenPlaceBtn(
            self, self.startx, self.starty + margin,
            "Voice input", "#E47676", "#F7D9D9", self.voiceInput, self.txt_font)
        addThenPlaceBtn(
            self, self.startx, self.starty + margin,
            "Frames folder", "#A25A30", "#FDF0E8", openFramesFolder, self.txt_font)
        addThenPlaceBtn(
            self, self.startx, self.starty + margin,
            "Delete frames", "#666666", "#E8E8E8", deleteFrames, self.txt_font)
        
    def changeOption(self):
        self.option = self.spbSelectMode.get()
    def voiceInput(self):
        dictCF = ["cắt", "các", "cách"]
        self.voiceInput = microphone()
        self.voiceInput.hear()
        print(self.voiceInput.textHeard)
        if "xóa" in self.voiceInput.textHeard:
            self.voiceInput.speak("tiến hành xóa ảnh")
            deleteFrames()
            return
        if "mở file" in self.voiceInput.textHeard:
            self.voiceInput.speak("mở file thành công")
            openFile()
        if len(filename) == 0:
            self.voiceInput.speak("mở file không thành công")
            return
        for words in dictCF:
            if words in self.voiceInput.textHeard:
                self.voiceInput.speak("tiến hành cắt ảnh")
                if "xám" in self.voiceInput.textHeard:
                    self.varOptions = "Grayscale"
                elif "ngược" in self.voiceInput.textHeard:
                    self.varOptions = "Reversed" 
                else:
                    self.varOptions = "Normal" 
        self.option = self.varOptions
        self.window.update()
        self.cutFrame()
        return
    def cutFrame(self):
        global filename
        if not filename:
            messagebox.showinfo(
                icon = "error", 
                title='Notification', 
                message='You haven\'t selected a file yet!')
            return
        Analyzer = analyzer(filename, self.option)
        self.stop = False
        if self.option == 'Normal':
            Analyzer.normal(self)
        if self.option == 'Grayscale':
            Analyzer.grayscale(self)
        if self.option == 'Reversed':
            Analyzer.reverse(self)
    
    def drawComponent(self):
        options = (
            "Normal",
            "Grayscale",
            "Reversed"
        )
        self.varOptions = StringVar(master = self.window)
        self.spbSelectMode = Spinbox(
            master = self.window, 
            from_ = 0, 
            to = 2, 
            width = self.width // 70, 
            font = self.txt_font,
            values = options,
            command = self.changeOption,
            textvariable = self.varOptions
        )
        self.changeOption()
        self.spbSelectMode.place(
            x = self.startx, 
            y = self.starty + margin
        )
        return
    def mainLoop(self):
        self.drawMainFrame()
        self.drawButtons()
        self.drawComponent()
        self.window.mainloop()