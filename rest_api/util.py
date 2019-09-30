import sqlite3
from sqlite3 import Error
from flask import jsonify


def get_prodi_from_nim(nim):
    nim_dict = {
        '101': 'Matematika',
        '102': 'Fisika',
        '103': 'Astronomi',
        '104': 'Mikrobiologi',
        '105': 'Kimia',
        '106': 'Biologi',
        '107': 'Sains dan Teknologi Farmasi',
        '112': 'Rekayasa Hayati',
        '114': 'Rekayasa Pertanian',
        '115': 'Rekayasa Kehutanan',
        '116': 'Farmasi Klinik dan Komunitas',
        '120': 'Teknik Geologi',
        '121': 'Teknik Pertambangan',
        '122': 'Teknik Perminyakan',
        '123': 'Teknik Geofisika',
        '124': 'Geofisika',
        '125': 'Teknik Metalurgi',
        '128': 'Meteorologi',
        '129': 'Oseanografi',
        '130': 'Teknik Kimia',
        '131': 'Teknik Mesin',
        '132': 'Teknik Elektro',
        '133': 'Teknik Fisika',
        '134': 'Teknik Industri',
        '135': 'Teknik Informatika',
        '136': 'Aeronotika dan Astronotika',
        '137': 'Teknik Material',
        '143': 'Teknik Pangan',
        '144': 'Manajemen Rekayasa Industri',
        '145': 'Teknik Bioenergi dan Kemurgi',
        '150': 'Teknik Sipil',
        '151': 'Teknik Geodesi dan Geomatika',
        '152': 'Arsitektur',
        '153': 'Teknik Lingkungan',
        '154': 'Perencanaan Wilayah dan Kota',
        '155': 'Teknik Kelautan',
        '157': 'Rekayasa Infrastruktur Lingkungan',
        '158': 'Teknik dan Pengelolaan Sumber Daya Air',
        '160': 'Tahap Tahun Pertama FMIPA',
        '161': 'Tahap Tahun Pertama SITH',
        '162': 'Tahap Tahun Pertama SF',
        '163': 'Tahap Tahun Pertama FITB',
        '164': 'Tahap Tahun Pertama FTTM',
        '165': 'Tahap Tahun Pertama STEI',
        '166': 'Tahap Tahun Pertama FTSL',
        '167': 'Tahap Tahun Pertama FTI',
        '168': 'Tahap Tahun Pertama FSRD',
        '169': 'Tahap Tahun Pertama FTMD',
        '170': 'Seni Rupa',
        '172': 'Kriya',
        '173': 'Desain Interior',
        '174': 'Desain Komunikasi Visual',
        '175': 'Desain Produk',
        '179': 'MKDU',
        '180': 'Teknik Tenaga Listrik',
        '181': 'Teknik Telekomunikasi',
        '182': 'Sistem dan Teknologi Informasi',
        '183': 'Teknik Biomedis',
        '190': 'Manajemen',
        '192': 'Kewirausahaan',
        '197': 'Tahap Tahun Pertama SBM',
        '199': 'Tahap Tahun Pertama SAPPK'
    }
    substr = nim[0:3]
    prodi = nim_dict.get(substr)
    return prodi


def create_connection():
    # Membuat koneksi ke database
    try:
        return sqlite3.connect('rest_api/database.db')
    except Exception as e:
        print(e)
        print('Error! Gagal membuat koneksi database')
        return None


def create_table():
    try:
        connection = create_connection()
        c = connection.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS nim_nama(
                nim text NOT NULL,
                nama text NOT NULL
            );
        ''')
    except Exception as e:
        print(e)


def import_data():
    try:
        connection = create_connection()
        f = open('nim_nama.sql', 'r')
        sql = f.read()
        connection.execute(sql)
    except Error as e:
        print(e)


def response_api(data):
    return (
        jsonify(**data),
        data['code']
    )
