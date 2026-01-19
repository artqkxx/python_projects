from final_database.database.db import conn, cursor

cursor.execute("SELECT * FROM clients")
clients = cursor.fetchall()

if not clients:
    print("Клієнтів у базі немає")
else:
    print("Список всіх клієнтів:")
    for client in clients:
        print(f"ID: {client[0]}, Ім'я: {client[1]}, Баланс: {client[2]}")

conn.close()