    from final_database.database.db import conn, cursor

id = int(input("Айді клієнта: "))

cursor.execute(
    "SELECT * FROM clients WHERE id = ?",
    (id,)
)
clients = cursor.fetchone()

if clients is None:
    raise Exception("Клієнта не знайдено")

print("Інформація про клієнта:")
print(f"ID: {clients[0]}")
print(f"Ім'я: {clients[1]}")
print(f"Баланс: {clients[2]}")

conn.commit()
conn.close()