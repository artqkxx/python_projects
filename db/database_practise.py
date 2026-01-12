import sqlite3


conn = sqlite3.connect("subjects.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    lectures INTEGER,
    practices INTEGER,
    exams INTEGER
)
""")


subjects_data = [
    ("Python", 20, 15, 2),
    ("Математика", 18, 8, 3),
    ("Бази даних", 16, 12, 1),
    ("Алгоритми", 14, 10, 2)
]

cursor.executemany("""
INSERT INTO subjects (name, lectures, practices, exams)
VALUES (?, ?, ?, ?)
""", subjects_data)

conn.commit()


cursor.execute("""
UPDATE subjects
SET practices = 18
WHERE name = 'Python'
""")
conn.commit()


print("Всі предмети:")
cursor.execute("SELECT * FROM subjects")
for row in cursor.fetchall():
    print(row)


print("\nПредмети з лекціями > 15:")
cursor.execute("""
SELECT name, lectures FROM subjects
WHERE lectures > 15
""")
for row in cursor.fetchall():
    print(row)


print("\nПредмети з практичними > 10:")
cursor.execute("""
SELECT name, practices FROM subjects
WHERE practices > 10
""")
for row in cursor.fetchall():
    print(row)


print("\nПредмет з найбільшою кількістю екзаменів:")
cursor.execute("""
SELECT name, exams FROM subjects
ORDER BY exams DESC
LIMIT 1
""")
print(cursor.fetchone())


conn.close()
