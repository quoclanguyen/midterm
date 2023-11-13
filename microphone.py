import playsound
from gtts import gTTS as qlgtts
import speech_recognition as sr
from datetime import datetime

class microphone:
    def __init__(self):
        self.lang = "vi"
        self.regconizer = sr.Recognizer()
    def speak(self, saywhat):
        myObj = qlgtts(text = saywhat, lang = self.lang, slow = False)
        filename = "audio/voice_" + datetime.now().strftime("%d-%m-%Y_%H%M%S") + ".mp3"
        myObj.save(filename)
        playsound.playsound(filename)
    def hear(self):
        with sr.Microphone() as source:
            wait_time = 5
            audio_data = self.regconizer.record(source, duration = wait_time)
            try:
                textHeard = self.regconizer.recognize_google(audio_data, language = self.lang)
            except:
                textHeard = "Không thể nghe được bạn nói gì"
            self.textHeard = textHeard.lower()