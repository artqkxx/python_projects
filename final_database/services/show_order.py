from final_database.database.db import conn, cursor


cursor.execute("SELECT * FROM orders")
orders = cursor.fetchall()

if not orders:
    print("Замовлень у базі немає.")
else:
    print("Список всіх замовлень:")
    for order in orders:
        print(f"ID замовлення: {order[0]}, Імя клієнта: {order[1]}, Послуга: {order[2]}, Ціна: {order[3]}")

conn.close()