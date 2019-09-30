import sqlite3
from sqlite3 import Error
from rest_api.util import get_prodi_from_nim, create_connection, create_table


def get_data(query, type, page):
    conn = create_connection()
    c = conn.cursor()

    if(type == "nim"):
        c.execute(
            '''
                SELECT *
                FROM nim_nama
                WHERE nim LIKE ? ORDER BY nim;
            ''',
            ("%" + query + "%",)
        )
    elif(type == "nama"):
        c.execute(
            '''
                SELECT *
                FROM nim_nama
                WHERE nama LIKE ? ORDER BY nim;
            ''',
            ("%" + query + "%",)
        )

    pageNow = 0
    payload = []
    i = 0
    for row in c.fetchall():
        if(pageNow == page):
            prodi = get_prodi_from_nim(row[0])
            data = {
                'name': row[1],
                'nim_tpb': row[0],
                'nim_jur': row[0],
                'prodi' : prodi
            }
            payload.append(data)

        i = i + 1
        if((i % 10) == 0):
            pageNow = pageNow + 1

    ret_data = {
        'code': 200,
        'status' : 'OK',
        'query' : query,
        'message': 'Data berhasil ditemukan.',
        'payload': payload
    }

    return ret_data