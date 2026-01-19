from final_database.database.db import conn, cursor

id = int(input("Айді послуги: "))

cursor.execute(
    "SELECT * FROM services WHERE id = ?",
    (id,)
)
service = cursor.fetchone()

if service is None:
    raise Exception("Послугу не знайдено")


print("Інформація про послугу:")
print(f"ID: {service[0]}")
print(f"Назва: {service[1]}")
print(f"Ціна: {service[2]}")

conn.commit()
cursor.close()