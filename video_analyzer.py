from tkinter import Label
import cv2 as cvql23
from PIL import Image, ImageTk
import numpy as qlnp


def hex2rgb(hex_value):
    h = hex_value.strip("#") 
    rgb = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    return rgb
def rgb2hsv(r, g, b):
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    
    max_rgb = max(r, g, b)    
    min_rgb = min(r, g, b)   
    difference = max_rgb-min_rgb 
    
    if max_rgb == min_rgb:
        h = 0
    elif max_rgb == r:
        h = (60 * ((g - b) / difference) + 360) % 360
    elif max_rgb == g:
        h = (60 * ((b - r) / difference) + 120) % 360
    elif max_rgb == b:
        h = (60 * ((r - g) / difference) + 240) % 360
    
    if max_rgb == 0:
        s = 0
    else:
        s = (difference / max_rgb) * 100
    v = max_rgb * 100
    return tuple(map(round, (h, s, v)))

class analyzer:
    def __init__(self, filename, option):
        self.filename = filename
        self.option = option
    def normal(self, GUI):
        captureQL = cvql23.VideoCapture(self.filename)
        countQL = 0
        while captureQL.isOpened() and GUI.stop == False:
            _, frame = captureQL.read()
            (h, w, _) = frame.shape 
            r = 400 / w
            dim = (400, int(h*r))
            resizedFrame = cvql23.resize(frame, dim)
            converted = cvql23.cvtColor(resizedFrame, cvql23.COLOR_BGR2RGBA)
            img = Image.fromarray(converted)
            imgTk = ImageTk.PhotoImage(master = GUI.window, image = img)
            lblFrame = Label(master = GUI.window)
            lblFrame.configure(image = imgTk)
            lblFrame.place(x = GUI.width//3, y = GUI.height//6)
            GUI.window.update()
            cvql23.imwrite('frames/normal/nFrame{}.jpg'.format(countQL), resizedFrame)
            countQL += 1
        captureQL.release()
    def grayscale(self, GUI):
        captureQL = cvql23.VideoCapture(self.filename)
        countQL = 0
        while captureQL.isOpened() and GUI.stop == False:
            _, frame = captureQL.read()
            frame = cvql23.cvtColor(frame, cvql23.COLOR_BGR2GRAY)
            (h, w) = frame.shape 
            r = 400 / w
            dim = (400, int(h*r))
            resizedFrame = cvql23.resize(frame, dim)
            converted = cvql23.cvtColor(resizedFrame, cvql23.COLOR_BGR2RGBA)
            img = Image.fromarray(converted)
            imgTk = ImageTk.PhotoImage(master = GUI.window, image = img)
            lblFrame = Label(master = GUI.window)
            lblFrame.configure(image = imgTk)
            lblFrame.place(x = GUI.width//3, y = GUI.height//6)
            GUI.window.update()
            cvql23.imwrite('frames/gray/gFrame{}.jpg'.format(countQL), resizedFrame)
            countQL += 1
            if cvql23.waitKey(10) & 0xFF == ord('q'):
                break
        captureQL.release()
        cvql23.destroyAllWindows()
    def colorfilter(self, GUI):
        captureQL = cvql23.VideoCapture(self.filename)
        countQL = 0
        while captureQL.isOpened() and GUI.stop == False:
            _, frame = captureQL.read()
            lower_color = hex2rgb(GUI.lower_color)
            upper_color = hex2rgb(GUI.upper_color) 
            print(lower_color)
            print(upper_color)
            mask = cvql23.inRange(frame, lower_color, upper_color)
            result = cvql23.bitwise_and(frame, frame, mask = mask) 

            (h, w, _) = result.shape 
            r = 400 / w
            dim = (400, int(h*r))
            resizedFrame = cvql23.resize(result, dim)
            converted = cvql23.cvtColor(resizedFrame, cvql23.COLOR_BGR2RGBA)
            img = Image.fromarray(converted)
            imgTk = ImageTk.PhotoImage(master = GUI.window, image = img)
            lblFrame = Label(master = GUI.window)
            lblFrame.configure(image = imgTk)
            lblFrame.place(x = GUI.width//3, y = GUI.height//6)
            GUI.window.update()
            cvql23.imwrite('frames/filter/fFrame{}.jpg'.format(countQL), resizedFrame)
            countQL += 1
            if cvql23.waitKey(10) & 0xFF == ord('q'):
                break
        captureQL.release()
        cvql23.destroyAllWindows()
    def reverse(self, GUI):
        captureQL = cvql23.VideoCapture(self.filename)
        frameArr = []
        countQL = 0
        checkEnd = True
        while checkEnd == True:
            checkEnd, frame = captureQL.read()
            frameArr.append(frame)
        frameArr.pop()
        frameArr.reverse()
        for frame in frameArr:
            if GUI.stop == True:
                break
            (h, w, _) = frame.shape 
            r = 400 / w
            dim = (400, int(h*r))
            resizedFrame = cvql23.resize(frame, dim)
            converted = cvql23.cvtColor(resizedFrame, cvql23.COLOR_BGR2RGBA)
            img = Image.fromarray(converted)
            imgTk = ImageTk.PhotoImage(master = GUI.window, image = img)
            lblFrame = Label(master = GUI.window)
            lblFrame.configure(image = imgTk)
            lblFrame.place(x = GUI.width//3, y = GUI.height//6)
            GUI.window.update()
            cvql23.imwrite('frames/reversed/rFrame{}.jpg'.format(countQL), resizedFrame)
            countQL += 1
            if cvql23.waitKey(10) & 0xFF == ord('q'):
                break
            frameArr.pop(0)
        captureQL.release()
        cvql23.destroyAllWindows()