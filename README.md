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
- Update and Upgrade system :
  ```bash
    sudo apt update && sudo apt upgrade -y
  ```
- to edit config txt :
  ```bash
    sudo nano /boot/firmware/config.txt
  ```
  ```bash
    sudo apt install python3-pip python3-pyaudio portaudio19-dev libasound2-dev flac -y

    pip3 install speechrecognition google-generativeai gTTS pygame --break-system-packages
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
`

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
