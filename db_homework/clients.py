from db_manager import get_connection


def add_client(first_name, last_name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO clients (first_name, last_name) VALUES (?, ?)",
        (first_name, last_name)
    )
    conn.commit()
    conn.close()


def get_all_clients():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clients")
    rows = cursor.fetchall()
    conn.close()
    return rows


def update_client(client_id, first_name, last_name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE clients SET first_name=?, last_name=? WHERE id=?",
        (first_name, last_name, client_id)
    )
    conn.commit()
    conn.close()


def delete_client(client_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM clients WHERE id=?", (client_id,))
    conn.commit()
    conn.close()
