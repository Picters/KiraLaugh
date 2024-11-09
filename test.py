import tkinter as tk
from PIL import Image, ImageTk
import time

# Set up main window
root = tk.Tk()
root.attributes('-fullscreen', True)
root.configure(bg="black")

# Close on ESC
root.bind("<Escape>", lambda e: root.destroy())

# Countdown setup
countdown_label = tk.Label(root, text="", font=("Arial", 24), fg="red", bg="black")
countdown_label.pack(pady=10)

# Image display
image_path = "./assets/kira.png"
image = Image.open(image_path).resize((10, 10))
photo = ImageTk.PhotoImage(image)
image_label = tk.Label(root, image=photo, bg="black")
image_label.pack()

# Message
message_label = tk.Label(root, text="Сколько хомячков не жалко для меня?", font=("Arial", 16), fg="white", bg="black")
message_label.pack(pady=10)

# Input field
input_field = tk.Entry(root, font=("Arial", 14), fg="white", bg="gray")
input_field.pack(pady=10)

# Countdown function
def start_countdown(seconds):
    for i in range(seconds, 0, -1):
        countdown_label.config(text=f"Время до запуска: {i} секунд")
        root.update()
        time.sleep(1)
    countdown_label.config(text="")

# Start countdown in a separate thread
root.after(1000, lambda: start_countdown(10))  # 10-second countdown

# Start main event loop
root.mainloop()
