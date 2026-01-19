from final_database.database.db import conn, cursor

client_name = input("Ім'я замовника: ")

service_name = input("Назва послуги: ")

price = int(input("Ціна послуги: "))

cursor.execute("""INSERT INTO orders (client_name, service_name, price) VALUES (?, ?, ?)""",
               (client_name, service_name, price))

conn.commit()
conn.close()

print("Замовлення додано!")