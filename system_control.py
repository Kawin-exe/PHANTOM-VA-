import os
import pyautogui

def control(command):
    if "open chrome" in command:
        os.system("start chrome")

    elif "open vscode" in command:
        os.system("code")

    elif "screenshot" in command:
        img = pyautogui.screenshot()
        img.save("screenshot.png")

    elif "volume up" in command:
        pyautogui.press("volumeup")

    elif "volume down" in command:
        pyautogui.press("volumedown")
