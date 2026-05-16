import tkinter as tk
from time import strftime

# Create window
root = tk.Tk()
root.title("Modern Digital Clock")
root.geometry("700x300")
root.configure(bg="#0f172a")  # Dark background

# Function to update time
def update_time():
    # 12-hour format with AM/PM
    current_time = strftime('%I:%M:%S %p')
    current_date = strftime('%A, %d %B %Y')

    time_label.config(text=current_time)
    date_label.config(text=current_date)

    # Update every second
    time_label.after(1000, update_time)

# Title Label
title_label = tk.Label(
    root,
    text="DIGITAL CLOCK",
    font=("Helvetica", 24, "bold"),
    bg="#0f172a",
    fg="#38bdf8"
)
title_label.pack(pady=10)

# Time Label
time_label = tk.Label(
    root,
    font=("Courier", 50, "bold"),
    bg="#1e293b",
    fg="#00ffcc",
    padx=20,
    pady=20,
    relief="ridge",
    bd=8
)
time_label.pack(pady=20)

# Date Label
date_label = tk.Label(
    root,
    font=("Helvetica", 18),
    bg="#0f172a",
    fg="white"
)
date_label.pack()

# Start clock
update_time()

# Run window
root.mainloop()