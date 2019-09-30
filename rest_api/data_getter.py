import sqlite3
from sqlite3 import Error
from rest_api.util import get_prodi_from_nim


def create_connection():
    # Membuat koneksi ke database
    try:
        return sqlite3.connect('nim_finder_api.db')
    except:
        print('Error! Gagal membuat koneksi database')
        return None

def create_table():
    try:
        with create_connection() as connection:
            c = connection.cursor()
            c.execute('''
                CREATE TABLE IF NOT EXISTS nim_nama(
                    nim text NOT NULL,
                    nama text NOT NULL
                );
            ''')
    except Error as e:
        print(e)

def get_by_id(id_nim):
    with create_connection() as conn:
        c = conn.cursor()

        c.execute(
            '''
                SELECT *
                FROM nama
                WHERE nim = ?;
            ''',
            (id_nim,)
        )

        row = c.fetchall()

        if row:
            for i in range(0, len(row)):
                row = row[i]
                payload = []
                prodi = get_prodi_from_nim(row[1])
                data = {
                    'name': row[0],
                    'nim_tpb': row[1],
                    'nim_jur': row[1],
                    'prodi' : prodi
                }
                payload.append(data);
        else:
            payload = []