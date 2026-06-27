import os
import time
import speech_recognition as sr
import google.generativeai as genai
from gtts import gTTS
import pygame

# 1. إعداد ذكاء Gemini الاصطناعي
# استبدل YOUR_GEMINI_API_KEY بمفتاحك الخاص
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro')

def speak(text):
    """تحويل النص إلى صوت وتشغيله عبر السماعة"""
    print(f"المساعد: {text}")
    # توليد ملف الصوت (يدعم العربية)
    tts = gTTS(text=text, lang='ar', slow=False)
    tts.save("response.mp3")
    
    # تشغيل ملف الصوت باستخدام pygame
    pygame.mixer.init()
    pygame.mixer.music.load("response.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
    pygame.mixer.quit()
    
    # حذف الملف المؤقت بعد التشغيل
    if os.path.exists("response.mp3"):
        os.remove("response.mp3")

def listen_and_process():
    """الاستماع من المايكروفون وتحويله إلى نص"""
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("\nجاري ضبط ضوضاء الخلفية... تكلّم بعد سماع كلمة 'ابدأ'")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("ابدأ التحدث الآن...")
        
        try:
            # الاستماع للصوت
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            print("جاري تحويل الصوت إلى نص...")
            
            # تحويل الصوت لنص باستخدام محرك جوجل (يدعم العربية)
            user_text = recognizer.recognize_google(audio, language='ar-EG')
            print(f"أنت قلت: {user_text}")
            return user_text
            
        except sr.UnknownValueError:
            speak("عذراً، لم أفهم ما قلته بشكل واضح.")
            return None
        except sr.RequestError:
            speak("عذراً، هناك مشكلة في الاتصال بالإنترنت.")
            return None
        except Exception as e:
            print(f"حدث خطأ: {e}")
            return None

# التشغيل المستمر للمساعد الذكي
if __name__ == "__main__":
    speak("مرحباً بك، أنا جاهز لسماع سؤالك.")
    
    while True:
        # 1. أخذ السؤال من المايكروفون
        query = listen_and_process()
        
        if query:
            if "خروج" in query or "إنهاء" in query:
                speak("إلى اللقاء!")
                break
                
            try:
                print("جاري الاتصال بالذكاء الاصطناعي...")
                # 2 & 3. إرسال النص إلى Gemini واستقبال الإجابة
                response = model.generate_content(query)
                ai_response = response.text
                
                # 4. إخراج الإجابة عبر السماعة
                speak(ai_response)
                
            except Exception as e:
                print(f"خطأ في الاتصال بـ API: {e}")
                speak("حدث خطأ أثناء محاولة جلب الإجابة.")
        
        # استراحة قصيرة قبل الاستماع مجدداً
        time.sleep(1)
