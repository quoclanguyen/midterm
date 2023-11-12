import playsound
from gtts import gTTS as qlan23
import speech_recognition as sr
from datetime import datetime
reg = sr.Recognizer()
src_lng = "vi"
des_lng = "en"
translated_text = ""


# yeu cau 3, 4 chọn tên ngôn ngữ in-out
# yeu cau 5: chọn tên file lưu, kiểm tra tên có sẵn không, nếu có hỏi ý nếu cần overwrite? 
# =============================================================================
# Sử dụng module os
# # th1: Đổi tên file cũ tự động
# # th2: đặt tên file mới tự động
# # th3: đặt tên file cũ mới khác nhau
# =============================================================================

def speak(textHeard, lng):
    myObj = qlan23(text=textHeard, lang=lng, slow=False)
    filename = "voice_" + datetime.now().strftime("%d-%m-%Y_%H%M%S") + ".mp3"
    myObj.save(filename)
    
    playsound.playsound(filename)

with sr.Microphone() as source:
    print("Hiệu chỉnh trước khi nói... Nhập vào thời gian (s):", end='')
    wait_time = int(input())
    reg.adjust_for_ambient_noise(source, duration=wait_time)
    
    print("Chọn ngôn ngữ đầu vào:", end='')
    src_lng = input()
    
    print("Hãy nói vào mic:... Nhập vào thời gian nghe giọng nói (s):", end='')
    wait_time = int(input())
    audio_data = reg.record(source, duration=wait_time)
    
    print("Chọn ngôn ngữ đầu ra:", end='')
    des_lng = input()
     
    print("Kết quả:")
    textHeard = ""
    try:
        textHeard = reg.recognize_google(audio_data, language=src_lng)
    except:
        textHeard = "Không thể nghe được bạn nói gì"
    
    print("Văn bản nghe được: {}".format(textHeard))
    speak(textHeard, src_lng)
