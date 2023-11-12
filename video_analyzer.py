import cv2 as cvql23
class analyzer:
    def __init__(self, filename, option):
        self.filename = filename
        self.option = option
    def normal(self):
        captureQL = cvql23.VideoCapture(self.filename)
        countQL = 0
        while captureQL.isOpened():
            _, frame = captureQL.read()
            (h, w, _) = frame.shape 
            r = 1000 / w
            dim = (1000, int(h*r))
            resizedFrame = cvql23.resize(frame, dim)
            cvql23.imshow('Normal Frame', resizedFrame)
            cvql23.imwrite('frames/normal/nFrame{}.jpg'.format(countQL), resizedFrame)
            countQL += 1
            if cvql23.waitKey(10) & 0xFF == ord('q'):
                break
        captureQL.release()
        cvql23.destroyAllWindows()
    def grayscale(self):
        captureQL = cvql23.VideoCapture(self.filename)
        countQL = 0
        while captureQL.isOpened():
            _, frame = captureQL.read()
            frame = cvql23.cvtColor(frame, cvql23.COLOR_BGR2GRAY)
            (h, w) = frame.shape 
            r = 1000 / w
            dim = (1000, int(h*r))
            resizedFrame = cvql23.resize(frame, dim)
            cvql23.imshow('Grayscale Frame', resizedFrame)
            cvql23.imwrite('frames/gray/gFrame{}.jpg'.format(countQL), resizedFrame)
            countQL += 1
            if cvql23.waitKey(10) & 0xFF == ord('q'):
                break
        captureQL.release()
        cvql23.destroyAllWindows()
    def reverse(self):
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
            cvql23.imshow("Reversed Frame", frame)
            cvql23.imwrite('frames/reversed/rFrame{}.jpg'.format(countQL), frame)
            countQL += 1
            if cvql23.waitKey(10) & 0xFF == ord('q'):
                break
        captureQL.release()
        cvql23.destroyAllWindows()



def analyze(filename):
    captureQL = cvql23.VideoCapture(filename)
    frameArr = []
    countQL = 0
    while captureQL.isOpened():
        ret, frame = captureQL.read()
        (h, w, d) = frame.shape 
        r = 1000 / w
        dim = (1000, int(h*r))
        resizedFrame = cvql23.resize(frame, dim)
        cvql23.imshow('Frame', resizedFrame)
        cvql23.imwrite('frames/aFrame{}.jpg'.format(countQL), resizedFrame)
        countQL += 1
        if cvql23.waitKey(10) & 0xFF == ord('q'):
            break
    captureQL.release()
    cvql23.destroyAllWindows()