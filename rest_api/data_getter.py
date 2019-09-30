from rest_api.util import get_prodi_from_nim, create_connection


def get_data(query, tipe, page):
    conn = create_connection()
    c = conn.cursor()

    if tipe == "nim":
        c.execute(
            '''
                SELECT *
                FROM nim_nama
                WHERE nim LIKE ? ORDER BY nim;
            ''',
            ("%" + query + "%",)
        )
    elif tipe == "nama":
        c.execute(
            '''
                SELECT *
                FROM nim_nama
                WHERE nama LIKE ? ORDER BY nim;
            ''',
            ("%" + query + "%",)
        )

    page_now = 0
    payload = []
    i = 0
    for row in c.fetchall():
        if page_now == page:
            prodi = get_prodi_from_nim(row[0])
            data = {
                'name': row[1],
                'nim_tpb': row[0],
                'nim_jur': row[0],
                'prodi': prodi
            }
            payload.append(data)

        i = i + 1
        if (i % 10) == 0:
            page_now = page_now + 1

    ret_data = {
        'code': 200,
        'status': 'OK',
        'query': query,
        'message': 'Data berhasil ditemukan.',
        'payload': payload
    }

    return ret_data
