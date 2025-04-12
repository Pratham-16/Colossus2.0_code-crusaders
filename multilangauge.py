from gtts import gTTS
from googletrans import Translator
from playsound import playsound
import serial
import time
import os
import uuid

# === Serial Port ===
ser = serial.Serial('COM3', 9600, timeout=1)  # Replace COM4 with your actual port
time.sleep(2)

# === Translator Setup ===
translator = Translator()
target_lang = 'ta'  # 'ta' = Tamil, use 'hi' for Hindi, etc.

print("🎧 Listening to Arduino...")

last_spoken = ""

try:
    while True:
        if ser.in_waiting:
            line = ser.readline().decode('utf-8').strip()

            if line.startswith("Obstacle at:") and line != last_spoken:
                last_spoken = line
                print("📏 ", line)

                # Translate full line
                translated = translator.translate(line, dest=target_lang).text
                print("🌐 Translated:", translated)

                # Convert to speech
                filename = f"tts_{uuid.uuid4().hex[:6]}.mp3"
                tts = gTTS(text=translated, lang=target_lang)
                tts.save(filename)

                playsound(filename)
                os.remove(filename)

except KeyboardInterrupt:
    print("\n🛑 Program stopped.")
finally:
    ser.close()
