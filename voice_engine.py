import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()

def speak(text):
    print("Phantom:", text)

    engine = pyttsx3.init()   # 🔥 reinitialize every time
    engine.setProperty('rate', 170)
    engine.setProperty('volume', 1.0)

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    engine.say(text)
    engine.runAndWait()
    engine.stop()   # 🔥 prevents freeze


def listen():
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source, duration=1)
            print("Listening...")

            audio = listener.listen(source, timeout=5, phrase_time_limit=5)
            command = listener.recognize_google(audio)

            print("You said:", command)
            return command.lower()

    except Exception as e:
        print("Voice Error:", e)
        return ""