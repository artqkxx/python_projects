from shop_project.database.db import conn, cursor

username = input("Введіть ваш логін: ")


while True:

    password = input("Введіть пароль: ")
    password_repeat = input("Повторіть пароль: ")

    if password == password_repeat:
        break

    else:
        print("Паролі не співпадають. Спробуйте ще раз")


cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)",(username, password))

conn.commit()
conn.close()
print("Реєстрація успішна")