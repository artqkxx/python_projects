import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import re

def loging():
    login = login_entry.get()
    password = password_entry.get()

    login_1 = bool(login_pattern.search(login))
    password_1 = bool(password_pattern.search(password))


    login_entry.config(bg="green" if login_1 else "red")
    password_entry.config(bg="green" if password_1 else "red")


    if login_1 and password_1:
        messagebox.showinfo(
            "Yakivchykgram",
            "Вітаю Ти зареєструвався в новому месенджері Yakivchykgram, чекай релізу"
        )
    if login_1 and not password_1:
        messagebox.showerror("Yakivchykgram", "Неправильно введений пароль, передивись підсказку")

    if password_1 and not login_1:
          messagebox.showerror("Yakivchykgram","Формат номера телефону повинен бути +380XXXXXXXXX")

    if not login_1 and not password_1:
        messagebox.showerror("Yakivchykgram","Не правильно введено номер телефону та пароль")

login_pattern = re.compile(r"^\+380\d{9}$")
password_pattern = re.compile(r"^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#%^&*?]).{6,20}$")

root = tk.Tk()
root.iconbitmap("img/1.ico")
root.geometry("600x400")
root.resizable(False, False)


image = Image.open("img/image.png")
image = image.resize((600, 400))
bg = ImageTk.PhotoImage(image)

bg_label = tk.Label(root, image=bg)
bg_label.place(x=0, y=0)


tip_label = tk.Label(root, text="Підсказка:1 велика літера, 1 мала, 1 цифра, 1 спецсимвол", font=("Arial", 14), bg="violet")
tip_label.place(x=50, y=185)

login_label = tk.Label(root, text="Number:", font=("Arial", 14), bg="white")
login_label.place(x=100, y=100)

login_entry = tk.Entry(root, font=("Arial", 12), width=20)
login_entry.place(x=200, y=105)

password_label = tk.Label(root, text="Password:", font=("Arial", 14), bg="white")
password_label.place(x=100, y=150)

password_entry = tk.Entry(root, font=("Arial", 12), width=20, show="*")
password_entry.place(x=200, y=155)

login_button = tk.Button(root, text="LOGIN", font=("Arial", 16), width=12, command=loging)
login_button.place(x=220, y=220)

root.mainloop()
