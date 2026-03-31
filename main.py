from voice_engine import speak, listen
from brain_ai import ask_ai
from system_control import control
from gui import launch_gui
import threading
import webbrowser

print("Login skipped. Starting Phantom...")

# Start GUI
threading.Thread(target=launch_gui).start()

speak("Welcome back. Phantom system is online.")

while True:
    command = listen()

    if not command:
        continue

    print("User:", command)

    # YOUTUBE
    if "youtube" in command:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")

    # SYSTEM CONTROL
    elif "open" in command or "volume" in command or "screenshot" in command:
        speak("Executing your command")
        control(command)

    # EXIT
    elif "exit" in command or "stop" in command:
        speak("Shutting down")
        break

    # AI RESPONSE
    else:
        response = ask_ai(command)
        speak(response)