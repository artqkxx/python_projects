from final_database.database.db import conn, cursor

name = input("Назва послуги: ")

price = int(input("Ціна послуги: "))

duration = int(input("Час дії послуги(в годинах): "))

cursor.execute("""INSERT INTO services (name, price, duration) VALUES (?, ?, ?)""",
               (name, price, duration))

conn.commit()
conn.close()

print("Послуга додана")