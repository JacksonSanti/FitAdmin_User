import sqlite3

def add_fake_data(conn):
    try:
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                group INTEGER NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        """)

        cursor.execute("INSERT OR IGNORE INTO Users (name, group, email, password) VALUES (?, ?, ?, ?)", 
                       ("Admin", 1, "admin@fitadmin.com", "12345678"))

        conn.commit()

    except Exception as e:
        print(f"Erro ao criar tabela: {e}")

def authenticate_user(conn, email, password):

    cursor = conn.cursor()

    cursor.execute("SELECT id FROM Users WHERE email = ? AND password = ?", (email, password))

    user_status = cursor.fetchone()

    return user_status

def get_all_student(conn):

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Students")

    data = cursor.fetchall()

    return data

def get_all_gender(conn):

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Genders")

    data = cursor.fetchall()

    return data

def get_gender_by_id(conn, gender_id):

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Genders WHERE id = ?", (gender_id,))

    data = cursor.fetchone()

    return data

def get_all_state(conn):

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM States")

    data = cursor.fetchall()

    return data

def get_state_by_id(conn, state_id):

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM States WHERE id = ?", (state_id,))

    data = cursor.fetchone()
    return data

def update_student_by_id(conn,id,name,gender_id,birthday,email,phone,state_id,city,neighborhood,address,number,cep,payment_id):

    cursor = conn.cursor()

    cursor.execute("""
    UPDATE students 
    SET name = ?, 
        gender_id = ?, 
        birthday = ?, 
        email = ?, 
        phone = ?, 
        state_id = ?, 
        city = ?, 
        neighborhood = ?, 
        address = ?, 
        number = ?, 
        cep = ?,
        payment_id = ? 
    WHERE id = ?;
    """, (name, gender_id, birthday, email, phone, state_id, city, neighborhood, address, number,cep, payment_id, id))

    conn.commit()

    return True

def create_student(conn, name, gender_id, birthday, email, phone, state_id, city, neighborhood, address, number, cep, payment_id):

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO students (
        name, 
        gender_id, 
        birthday, 
        email, 
        phone, 
        state_id, 
        city, 
        neighborhood, 
        address, 
        number, 
        cep,
        payment_id
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    """, (name, gender_id, birthday, email, phone, state_id, city, neighborhood, address, number, cep, payment_id))

    conn.commit()

    return cursor.lastrowid

def update_payment_id_by_student_id(conn, student_id, financial_id):

    cursor = conn.cursor()

    cursor.execute("""
        UPDATE students 
        SET payment_id = ? 
        WHERE id = ?;
    """, (financial_id, student_id))

    conn.commit()

    return True

def delete_student_by_id(conn, student_id):
    cursor = conn.cursor()
    
    cursor.execute("""
        DELETE FROM students
        WHERE id = ?;
    """, (student_id,))
    
    conn.commit()

    return True

def get_student_by_name(conn, name):

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students WHERE name LIKE ?", (f"%{name}%",))

    data = cursor.fetchall() 

    return data





