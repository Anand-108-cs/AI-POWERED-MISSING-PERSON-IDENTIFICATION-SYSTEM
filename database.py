import sqlite3
import pickle
import os
DB_FOLDER = "known_faces"
DB_NAME = "missing_persons.db"

def init_db():
    """
    Creates Database (DDL Operation)

    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Creating table of missing persons
    # Save Embedding in BLOB(binary large object)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS missing_persons (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            gender TEXT,
            email TEXT,
            age INTEGER,
            address TEXT,
            embedding BLOB 
        )
    ''')
    
    conn.commit()
    conn.close()
    print("Database initialized successfully.")

def insert_person(full_name, gender, email, age, address, embedding_array):
    """
    Insert data of new missing person
    
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # To save numpy array(embedding) in database , convert into bytes/pickle
    embedding_bytes = pickle.dumps(embedding_array)
    
    cursor.execute('''
        INSERT INTO missing_persons (full_name, gender, email, age, address, embedding)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (full_name, gender, email, age, address, embedding_bytes))
    
    conn.commit()
    conn.close()

def get_all_embeddings():
    """
    Takes embeddings from database for Face Recognition(comparison)

    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("SELECT full_name, embedding FROM missing_persons")
    rows = cursor.fetchall()
    conn.close()
    
    # Store into dictionary format as recognizer expects
    saved_embeddings = {}
    for row in rows:
        name = row[0]
        embedding_bytes = row[1]
        if embedding_bytes:
            embedding_array = pickle.loads(embedding_bytes)

            if name not in saved_embeddings:
                saved_embeddings[name] = []
            saved_embeddings[name].append(embedding_array)
            
    return saved_embeddings

# Table will be created when it run
if __name__ == "__main__":
    init_db()

# to get email

def get_email_by_name(name):
    """
    Reads email from the database on the basis of Name

    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("SELECT email FROM missing_persons WHERE full_name=?", (name,))
    result = cursor.fetchone()
    
    conn.close()
    
    if result and result[0]:
        return result[0]
    return None