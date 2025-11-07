import string
import tkinter as tk
from tkinter import ttk


def caesar_cipher(text, shift):
    alphabet = string.ascii_letters + string.digits + string.punctuation + " "
    result = ""
    for char in text:
        if char in alphabet:
            idx = alphabet.index(char)
            result += alphabet[(idx + shift) % len(alphabet)]
        else:
            result += char
    return result


def process_text():
    text = input_text.get("1.0", tk.END).rstrip("\n")
    try:
        shift = int(shift_entry.get())
    except ValueError:
        output_text.set("Shift must be an integer.")
        return
    result = caesar_cipher(text, shift)
    output_text.set(result)


root = tk.Tk()
root.title("Caesar Cipher")

frame = ttk.Frame(root, padding=12)
frame.grid()

ttk.Label(frame, text="Enter text:").grid(column=0, row=0, sticky="w")
input_text = tk.Text(frame, width=50, height=5)
input_text.grid(column=0, row=1, columnspan=2)

ttk.Label(frame, text="Shift:").grid(column=0, row=2, sticky="w")
shift_entry = ttk.Entry(frame, width=10)
shift_entry.grid(column=1, row=2, sticky="w")

ttk.Button(frame, text="Encrypt / Decrypt", command=process_text).grid(
    column=0, row=3, columnspan=2, pady=8
)

output_text = tk.StringVar()
ttk.Label(frame, text="Result:").grid(column=0, row=4, sticky="w")
ttk.Label(frame, textvariable=output_text, wraplength=400).grid(
    column=0, row=5, columnspan=2, sticky="w"
)

root.mainloop()
