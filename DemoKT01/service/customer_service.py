from database.connection import get_connection
from model.customer_model import Customer

def get_all_customers():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Customers")
    rows = cursor.fetchall()
    conn.close()
    return [Customer(*row).to_dict() for row in rows]

def delete_customer(customer_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Customers WHERE customer_id = ?", (customer_id,))
    conn.commit()
    conn.close()
    return cursor.rowcount > 0

def add_customer(data):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Customers (first_name, last_name, company, address, email)
        VALUES (?, ?, ?, ?, ?)
    """, (data["first_name"], data["last_name"], data["company"], data["address"], data["email"]))
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return new_id

def update_customer(customer_id, data):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE Customers SET first_name=?, last_name=?, company=?, address=?, email=?
        WHERE customer_id=?
    """, (data["first_name"], data["last_name"], data["company"], data["address"], data["email"], customer_id))
    conn.commit()
    conn.close()
    return cursor.rowcount > 0
