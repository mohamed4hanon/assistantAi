import os
import time
import speech_recognition as sr
import google.generativeai as genai
from gtts import gTTS

# 1. إعداد ذكاء Gemini الاصطناعي
# استبدل بمفتاحك الخاص المأخوذ من Google AI Studio
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
genai.configure(api_key=GEMINI_API_KEY)

# استخدام نموذج 1.5-flash الأحدث والأسرع والأنسب لموارد الراسبيري باي
model = genai.GenerativeModel('gemini-1.5-flash')

def speak(text):
    """تحويل النص إلى صوت وتشغيله عبر أداة mpg123 الخفيفة لنظام اللينكس"""
    print(f"المساعد: {text}")
    
    filename = "response.mp3"
    
    try:
        # توليد ملف الصوت (يدعم العربية)
        tts = gTTS(text=text, lang='ar', slow=False)
        tts.save(filename)
        
        # تشغيل ملف الصوت عبر أمر النظام mpg123 (الخيار -q للتشغيل الصامت بدون نصوص زائدة)
        os.system(f"mpg123 -q {filename}")
        
    except Exception as e:
        print(f"حدث خطأ أثناء تشغيل الصوت: {e}")
        
    finally:
        # التأكد من حذف الملف المؤقت بعد التشغيل لتحرير المساحة
        if os.path.exists(filename):
            try:
                os.remove(filename)
            except OSError:
                pass

def listen_and_process():
    """الاستماع من المايكروفون (USB) وتحويله إلى نص"""
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("\nجاري ضبط ضوضاء الخلفية... تكلّم بعد سماع كلمة 'ابدأ'")
        # ضبط الحساسية للضوضاء (نصف ثانية لتسريع العملية على الباي)
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print("ابدأ التحدث الآن...")
        
        try:
            # الاستماع مع تحديد وقت أقصى للصمت ووقت التحدث لتووفير موارد المعالج
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)
            print("جاري تحويل الصوت إلى نص...")
            
            # تحويل الصوت لنص عبر محرك جوجل باللكنة المصرية/العربية العامة
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
            # معالجة حالة عدم تحدث المستخدم (Timeout)
            return None

# نقطة انطلاق البرنامج
if __name__ == "__main__":
    speak("مرحباً بك، أنا جاهز لسماع سؤالك.")
    time.sleep(0.5)
    
    while True:
        # 1. الاستماع من المايكروفون
        query = listen_and_process()
        
        if query:
            # شروط إنهاء البرنامج صوتياً
            if "خروج" in query or "إنهاء" in query or "إغلاق" in query:
                speak("إلى اللقاء! يومك سعيد.")
                break
                
            try:
                print("جاري الاتصال بالذكاء الاصطناعي...")
                
                # توجيه الـ prompt ليعطي إجابات قصيرة ومناسبة للمحادثات الصوتية
                prompt = f"أجب باختصار شديد ومناسب للمحادثة الصوتية على السؤال التالي: {query}"
                response = model.generate_content(prompt)
                ai_response = response.text
                
                # 2. نطق الإجابة
                speak(ai_response)
                
            except Exception as e:
                print(f"خطأ في الاتصال بـ API: {e}")
                speak("حدث خطأ أثناء محاولة جلب الإجابة.")
        
        # استراحة قصيرة جداً قبل بدء الدورة القادمة لمنع تداخل الصوت
        time.sleep(1)
