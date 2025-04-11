import serial
import pyttsx3

# Replace COM3 with the port shown in Arduino IDE (Tools > Port)
ser = serial.Serial('COM3', 9600, timeout=1)

engine = pyttsx3.init()
print("🔊 Listening to Arduino...")

while True:
    line = ser.readline().decode('utf-8').strip()
    if line:
        print("Arduino:", line)
        engine.say(line)
        engine.runAndWait()