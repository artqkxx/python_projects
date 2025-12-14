import tkinter as tk

root = tk.Tk()

font_size_value = 25

def font_size():
    global font_size_value
    if font_size_value == 25:
        font_size_value = 50
    else:
        font_size_value = 25
    lable.config(font=("Times New Roman", font_size_value, "bold"))

root.title("Мій текст")
root.geometry("400x300")
root.resizable(False, False)

lable = tk.Label(root, text="Text",
                 font=("Times New Roman", 25, "bold"),
                 fg="white", bg="black", padx=30, pady=10)

button = tk.Button(root, text="Change size",
                   font=("Arial", 15, "bold"),
                   fg="white", bg="green",
                   width=10, height=2,
                   command=font_size)

button.pack()
lable.pack()

root.mainloop()
