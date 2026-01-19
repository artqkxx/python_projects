from final_database.database.db import conn, cursor

# Ввід ID клієнта
id = int(input("Введіть ID клієнта: "))

# Знайти клієнта
cursor.execute("SELECT * FROM clients WHERE id = ?", (id,))
clients = cursor.fetchone()

if clients is None:
    print("Клієнта не знайдено")
else:
    print(f"Баланс клієнта {clients[1]} (ID: {clients[0]}): {clients[2]}")

conn.close()