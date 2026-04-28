import sqlite3

DB_NAME = "penjadwal.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    # Membuat tabel jika belum ada
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS aktivitas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            judul TEXT NOT NULL,
            tanggal TEXT NOT NULL,
            waktu TEXT NOT NULL,
            kategori TEXT NOT NULL,
            prioritas TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_activity(judul, tanggal, waktu, kategori, prioritas):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO aktivitas (judul, tanggal, waktu, kategori, prioritas)
        VALUES (?, ?, ?, ?, ?)
    ''', (judul, tanggal, waktu, kategori, prioritas))
    conn.commit()
    conn.close()

def get_all_activities():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM aktivitas ORDER BY tanggal, waktu')
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_activity(activity_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM aktivitas WHERE id = ?', (activity_id,))
    conn.commit()
    conn.close()