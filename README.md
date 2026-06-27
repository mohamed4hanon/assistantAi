# 🤖 assistantAi

Welcome to **assistantAi**, a dedicated control panel and management system designed to turn your Raspberry Pi into an intelligent, always-on AI assistant. This page helps you monitor system resources, manage background AI models, and configure assistant behaviors.

## 🛠️ Key Features
- **Pi Management:** Real-time tracking of CPU, memory, and temperature metrics.
- **AI Core Control:** Start, stop, and configure locally hosted or API-driven AI models.
- **Task Automation:** Schedule recurring routines and manage script workflows on your Pi.
- **Interactive Console:** Built-in dashboard to communicate with your AI assistant directly.

## 📦 Getting Started

### Prerequisites
Before running this project, ensure your Raspberry Pi has the following installed:
- Raspberry Pi lite OS (64-bit recommended)
- Python 3.10+ or Node.js (v18+)
- Git
- Update and Upgrade system and install required librarries :
   - تحديث النظام أولاً

  ```bash
    sudo apt update && sudo apt upgrade -y
  ```


- تثبيت الحزم اللازمة للتعامل مع الصوت والمايكروفون (ALSA و PulseAudio)

   ```bash
       sudo apt install alsa-utils pulseaudio portaudio19-dev libasound2-dev -y
   ```

- تثبيت الحزم اللازمة لتشغيل ملفات MP3 ومكتبة Pygame في بيئة بدون واجهة رسومية
  ```bash
      sudo apt install libsdl2-mixer-2.0-0 ffmpeg -y
  ```


- تثبيت مكتبات بايثون
تأكد من تثبيت المكتبات داخل النظام (يفضل استخدام بيئة افتراضية لـ Python 3):

  ```bash
    pip3 install google-generativeai speechRecognition gTTS pygame pyaudio
  ```
    ```bash
    sudo apt install python3-pip python3-pyaudio portaudio19-dev libasound2-dev flac -y

  ```

 -   تشغيل خادم الصوت (في حال واجهت مشكلة في خروج الصوت):
  ```bash
   pulseaudio --start
  ```


  
- to edit config txt :
  ```bash
    sudo nano /boot/firmware/config.txt
  ```


- To check mic :
  ```bash
    arecord -l
  ```

- TO chech Speakers :
  ```bash
   aplay -l
  ```

- TO test headphone :
  ```bash
   speaker-test -t sine -f 440 -c 2
  ```
- You should get AI Key :
  GEMINI_API_KEY = "ضع_مفتاح_جوجل_هنا"
  
- Option A: Download a WAV file (Recommended because it works instantly without extra software):
  ```bash
     wget -O test.wav https://github.com2
  ```
- If playing the WAV file:Run the native aplay command:
  ```bash
     aplay test.wav
  ```
 - Option B: Download an MP3 file:
  ```bash
     wget -O test.mp3 https://github.com/rafaelreis-hotmart/Audio-Sample-files/raw/master/sample.mp3
  ```   
- If playing the MP3 file:You will need to install a command-line player first. Use mpg123:
  ```bash
    sudo apt update && sudo apt install mpg123 -y
    mpg123 test.mp3
  ```





### Installation
1. Clone this repository to your Raspberry Pi:
   ```bash
   git clone https://github.com/mohamed4hanon/assistantAi.git
   ```
2. Navigate into the project directory:
   ```bash
   cd assistantAi
   ```
3. Run the setup script to install dependencies and configure local environment variables:
   ```bash
   bash setup.sh
   ```

## 💻 Usage
To launch the assistant management server, run:
```bash
npm start
```
*Or if using Python:*
```bash
python assistant.py
```
Open your browser and navigate to `http://localhost:3000` (or your Pi's local IP address) to access the dashboard.

## 🤝 Contributing
Contributions are what make the open-source community an amazing place to learn, inspire, and create. Feel free to fork this project, open an issue, or submit a pull request!
