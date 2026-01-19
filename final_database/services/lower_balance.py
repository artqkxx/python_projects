from final_database.database.db import conn, cursor

id = int(input("Введіть ID: "))

cursor.execute("SELECT * FROM clients WHERE id = ?", (id,))
clients = cursor.fetchone()

if clients is None:
    print("Клієнта не знайдено")
else:
    amount = float(input("Введіть суму для зменшення балансу: "))

    if amount > clients[2]:
        print(f"Недостатньо коштів. Поточний баланс: {clients[2]}")
    else:
        new_balance = clients[2] - amount
        cursor.execute(
            "UPDATE clients SET balance = ? WHERE id = ?",
            (new_balance, id)
        )
        conn.commit()
        print(f"Баланс знижено. Новий баланс: {new_balance}")

conn.close()
