from final_database.database.db import conn, cursor

cursor.execute("SELECT * FROM services")
services = cursor.fetchall()

if not services:
    print("Послуг у базі немає.")
else:
    print("Список всіх послуг:")
    for service in services:
        print(f"ID послуги: {service[0]}, Назва: {service[1]}, Ціна: {service[2]}")

conn.close()