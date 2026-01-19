from shop_project.database.db import conn, cursor


name = input("Назва товару: ")
price = float(input("Ціна: "))
quantity = int(input("Кількість: "))

cursor.execute("INSERT INTO products (name,price,quantity) VALUES (?, ?, ?)",(name, price, quantity))

conn.commit()
conn.close()

print("Товар додано")