import tkinter as tk

def hide_text():
    if lable["text"] == "":
        lable.config(text="Hello ITStep")
    else:
        lable.config(text="")





root = tk.Tk()

# назва проги
root.title("Моя перша віконна програма")

# розмір вікна
# 1 умова-розмір, 2 умова - спавн
root.geometry("500x400+700+300")

# заблокувати змінну розміра
root.resizable(False,False)


lable =  tk.Label(root,text = "Hello ITStep",
                  font = ("Times New Roman",25,'bold'), # шрифт, розмір, стиль
                  fg="white", # розмір тексту
                  bg="black",# колір фону текста
                  padx=30,pady=10 # відступ від країв

                  )

# створення кнопки
button = tk.Button(root, text = "Click me",
                   font=("Arial", 15,'bold'),
                   fg="white",
                   bg="green",
                   width=10,
                   height=2,
                   relief="raised",
                   command=hide_text
                   ) # стиль рамки: flat raised sunken groove ridge
button.pack()
lable.pack()





# показати вікно
root.mainloop()