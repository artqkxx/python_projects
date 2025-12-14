import tkinter as tk
import re

def filter_text():
    text = entry.get()
    result = re.sub(r"\d+", "", text)
    result_label.config(text=result)


root = tk.Tk()
root.title("Фільтр слів")


entry = tk.Entry(root, width=40)
entry.pack(pady=10)


button = tk.Button(root, text="Видалити цифри", command=filter_text)
button.pack(pady=5)


result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
