import unittest

from rest_api.data_getter import get_data

def test_get_by_id():
    valid_data = {
            "name": "Dewita Sonya Tarabunga",
            "nim_jur": "13515021",
            "nim_tpb": "13515021",
            "prodi": "Teknik Informatika"
        }
    response = get_data('13515021', 'nim', 0)
    assert response.get("payload")[0] == valid_data

def test_data_per_page():
    # Data setiap page ada 10
    response = get_data('135', 'nim', 0)
    assert len(response.get("payload")) == 10

def test_data_page_1():
    # Data setiap page ada 10
    response = get_data('135', 'nim', 1)
    assert len(response.get("payload")) == 10

def test_get_by_nama_sama_persis():
    valid_data = {
            "name": "Dewita Sonya Tarabunga",
            "nim_jur": "13515021",
            "nim_tpb": "13515021",
            "prodi": "Teknik Informatika"
        }
    response = get_data('Dewita Sonya Tarabunga', 'nama', 0)
    assert response.get("payload")[0] == valid_data

def test_get_by_nama_lowercase():
    valid_data = {
            "name": "Dewita Sonya Tarabunga",
            "nim_jur": "13515021",
            "nim_tpb": "13515021",
            "prodi": "Teknik Informatika"
        }
    response = get_data('dewita sonya tarabunga', 'nama', 0)
    assert response.get("payload")[0] == valid_data

def test_get_by_nama_uppercase():
    valid_data = {
            "name": "Dewita Sonya Tarabunga",
            "nim_jur": "13515021",
            "nim_tpb": "13515021",
            "prodi": "Teknik Informatika"
        }
    response = get_data('DEWITA SONYA TARABUNGA', 'nama', 0)
    assert response.get("payload")[0] == valid_data

def test_get_by_nama_tidak_lengkap():
    valid_data = {
            "name": "Dewita Sonya Tarabunga",
            "nim_jur": "13515021",
            "nim_tpb": "13515021",
            "prodi": "Teknik Informatika"
        }
    response = get_data('ewita sonya tarabung', 'nama', 0)
    assert response.get("payload")[0] == valid_data