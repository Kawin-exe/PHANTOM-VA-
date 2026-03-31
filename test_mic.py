import speech_recognition as sr

listener = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak now...")
    audio = listener.listen(source)

try:
    text = listener.recognize_google(audio)
    print("You said:", text)
except Exception as e:
    print("Error:", e)