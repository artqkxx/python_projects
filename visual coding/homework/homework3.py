import tkinter as tk
import re

def check_number():
    number = entry.get()
    pattern = r"^\+380\d{9}$"

    if re.fullmatch(pattern, number):
        result_label.config(text="Номер правильний", fg="green")
    else:
        result_label.config(text="Номер неправильний", fg="red")


root = tk.Tk()
root.title("Перевірка номеру")
root.geometry("300x300")

# Entry
entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=10)

# Button
check_button = tk.Button(root, text="Перевірити", command=check_number)
check_button.pack(pady=5)

# Label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()