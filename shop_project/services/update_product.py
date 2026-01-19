from shop_project.database.db import conn, cursor

product_id = int(input("ID товару: "))
new_price = int(input("Нова ціна: "))


cursor.execute("UPDATE products SET price = ? WHERE id = ?",(new_price,product_id))

conn.commit()
conn.close()
print("Ціну оновлено")