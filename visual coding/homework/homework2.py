import tkinter as tk
import re


def check_text():
    text = entry.get()
    pattern = r"^[A-Za-zА-Яа-яІіЇїЄє]+$"

    if re.fullmatch(pattern, text):
        result_label.config(text="Тільки букви", fg="green")
    else:
        result_label.config(text="Містить сторонні символи", fg="red")


# Вікно
root = tk.Tk()
root.title("Перевірка тексту")
root.geometry("300x150")

# Entry
entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=10)

# Button
check_button = tk.Button(root, text="Перевірити", command=check_text)
check_button.pack(pady=5)

# Label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
