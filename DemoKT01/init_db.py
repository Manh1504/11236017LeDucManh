import sqlite3

def init_db():
    with open('init_db.sql', 'r', encoding='utf-8') as f:
        sql_script = f.read()

    conn = sqlite3.connect('ShoppingDB.db')
    cursor = conn.cursor()
    cursor.executescript(sql_script)
    conn.commit()
    conn.close()
    print("✅ Đã tạo lại cơ sở dữ liệu và thêm dữ liệu mẫu.")

if __name__ == "__main__":
    init_db()
