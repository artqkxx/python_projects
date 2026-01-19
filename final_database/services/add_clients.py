from final_database.database.db import conn, cursor

name = input("Ім'я клієнта: ")

balance = int(input("Баланс клієнта: "))

cursor.execute("INSERT INTO clients (name, balance) VALUES (?, ?)",
               (name, balance))

conn.commit()
conn.close()

print("Клієнта додано")