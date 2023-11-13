from tkinter import Label
import cv2 as cvql23
from PIL import Image, ImageTk
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
        cvql23.destroyAllWindows()
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