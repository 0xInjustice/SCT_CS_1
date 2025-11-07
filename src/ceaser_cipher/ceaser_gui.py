import tkinter as tk
from tkinter import ttk

import ttkbootstrap as tb
from cipher_logic import caesar_cipher


def process_text():
    text = input_text.get("1.0", tk.END).rstrip("\n")
    try:
        shift = int(shift_entry.get())
    except ValueError:
        output_text.set("Shift must be an integer.")
        return
    result = caesar_cipher(text, shift)
    output_text.set(result)


root = tb.Window(themename="cyborg")
root.title("Caesar Cipher")

frame = ttk.Frame(root, padding=20)
frame.grid()

# Title
ttk.Label(frame, text="Caesar Cipher", font=("JetBrains Mono", 18, "bold")).grid(
    column=0, row=0, columnspan=2, pady=(0, 15)
)

# Input text
ttk.Label(frame, text="Input Text:", font=("JetBrains Mono", 11)).grid(
    column=0, row=1, sticky="w"
)
input_text = tk.Text(frame, width=60, height=6, font=("JetBrains Mono", 10))
input_text.grid(column=0, row=2, columnspan=2, pady=(0, 10))

# Shift entry
ttk.Label(frame, text="Shift:", font=("JetBrains Mono", 11)).grid(
    column=0, row=3, sticky="w"
)
shift_entry = ttk.Entry(frame, width=10)
shift_entry.grid(column=1, row=3, sticky="w")

# Button
ttk.Button(
    frame,
    text="Encrypt / Decrypt",
    bootstyle="primary-outline",
    command=process_text,
).grid(column=0, row=4, columnspan=2, pady=12)

# Output
ttk.Label(frame, text="Result:", font=("JetBrains Mono", 11, "bold")).grid(
    column=0, row=5, sticky="w"
)
output_text = tk.StringVar()
output_label = ttk.Label(
    frame, textvariable=output_text, wraplength=500, font=("JetBrains Mono", 10)
)
output_label.grid(column=0, row=6, columnspan=2, sticky="w")

root.mainloop()
