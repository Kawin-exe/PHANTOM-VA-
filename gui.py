import tkinter as tk

def launch_gui():
    root = tk.Tk()
    root.title("PHANTOM JARVIS")
    root.geometry("500x300")
    root.configure(bg="black")

    label = tk.Label(root, text="PHANTOM AI", fg="cyan", bg="black", font=("Arial", 24))
    label.pack(pady=50)

    status = tk.Label(root, text="System Ready", fg="white", bg="black")
    status.pack()

    root.mainloop()
