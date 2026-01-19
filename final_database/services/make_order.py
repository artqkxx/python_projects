from final_database.database.db import conn, cursor

current_user = input("Введіть ваш ID користувача (0 якщо не увійшли): ")

if current_user == "0":
    print("Ви не авторизовані. Покупка заборонена")

else:
    product_id = int(input("ID товару: "))
    quantity = int(input("Кількість: "))

    cursor.execute("SELECT quanity FROM products WHERE id = ?",(product_id,))

    product = cursor.fetchall()

    if product and product[0] >= quantity:
        cursor.execute("UPDATE products SET quantity = quantity - ? WHERE id = ?",(quantity, product_id))

        conn.commit()
        print("Покупка успішна")

    else:
        print("Недостатня кількість товару")


conn.close()