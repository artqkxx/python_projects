from db_manager import get_connection


def add_membership(m_type, price, duration):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO memberships (type, price, duration) VALUES (?, ?, ?)",
        (m_type, price, duration)
    )
    conn.commit()
    conn.close()


def get_all_memberships():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM memberships")
    rows = cursor.fetchall()
    conn.close()
    return rows


def update_membership(m_id, m_type, price, duration):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE memberships SET type=?, price=?, duration=? WHERE id=?",
        (m_type, price, duration, m_id)
    )
    conn.commit()
    conn.close()


def delete_membership(m_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM memberships WHERE id=?", (m_id,))
    conn.commit()
    conn.close()
