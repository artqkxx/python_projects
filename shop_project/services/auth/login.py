from shop_project.database.db import conn, cursor


username = input("Логін: ")
password = input("Пароль: ")

cursor.execute("SELECT * FROM users where username = ? AND password = ?",
               (username,password))

# дістаю результат запиту
user=cursor.fetchall()
conn.close()

if user:
    print("Вхід успішний")
    current_user = user[0]

else:
    print("Невірний логін або пароль")
    current_user = None
