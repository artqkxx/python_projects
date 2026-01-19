from shop_project.database.db import conn, cursor

cursor.execute("SELECT * FROM products")
products = cursor.fetchall()

print("\nСписок товарів:")
for products in products:
    print(products)

conn.close()
