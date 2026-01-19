from final_database.database.db import conn, cursor

id = int(input("Введіть ID клієнта: "))

cursor.execute("SELECT * FROM clients WHERE id = ?", (id,))
clients = cursor.fetchone()

if clients is None:
    print("Клієнта не знайдено")
else:
    amount = float(input("Введіть суму для збільшення балансу: "))

    new_balance = clients[2] + amount
    cursor.execute(
        "UPDATE clients SET balance = ? WHERE id = ?",
        (new_balance, id)
    )
    conn.commit()
    print(f"Баланс успішно збільшено. Новий баланс: {new_balance}")

conn.close()