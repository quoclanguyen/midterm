from tkinter import messagebox
from tkinter.font import Font
from tkinter import *
from tkinter import filedialog as fd
from video_analyzer import analyzer
import subprocess
import os
import glob

margin = 0
filename = None

def deleteFrames():
    repo = [
        glob.glob('frames/normal/*'),
        glob.glob('frames/gray/*'),
        glob.glob('frames/reversed/*')
    ]
    
    for folder in repo:
        for file in folder:
            os.remove(file)
    messagebox.showinfo(
            icon = "info", 
            title='Notification', 
            message='Deleted all frames')
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

def voiceInput():
    print("test")
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
            "Start cut frame", "#151C47", "#C6CCDA", self.cutFrame, self.txt_font)
        addThenPlaceBtn(
            self, self.startx, self.starty + margin,
            "Voice input", "#E47676", "#F7D9D9", voiceInput, self.txt_font)
        addThenPlaceBtn(
            self, self.startx, self.starty + margin,
            "Frames folder", "#A25A30", "#FDF0E8", openFramesFolder, self.txt_font)
        addThenPlaceBtn(
            self, self.startx, self.starty + margin,
            "Delete frames", "#666666", "#E8E8E8", deleteFrames, self.txt_font)
        
    def changeOption(self):
        self.option = self.spbSelectMode.get()
    def cutFrame(self):
        global filename
        if not filename:
            messagebox.showinfo(
                icon = "error", 
                title='Notification', 
                message='You haven\'t selected a file yet!')
            return
        Analyzer = analyzer(filename, self.option)
        if self.option == 'Normal':
            Analyzer.normal()
        if self.option == 'Grayscale':
            Analyzer.grayscale()
        if self.option == 'Reversed':
            Analyzer.reverse()
    
    def drawComponent(self):
        options = (
            "Normal",
            "Grayscale",
            "Reversed"
        )
        self.spbSelectMode = Spinbox(
            master = self.window, 
            from_ = 0, 
            to = 2, 
            width = self.width // 70, 
            font = self.txt_font,
            values = options,
            command = self.changeOption
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