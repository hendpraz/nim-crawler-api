import unittest

from rest_api.util import get_prodi_from_nim

def test_nim_informatika():
    nim = '13517105'
    prodi = get_prodi_from_nim(nim)
    assert prodi == 'Teknik Informatika'

def test_nim_tpb_stei():
    nim = '16517358'
    prodi = get_prodi_from_nim(nim)
    assert prodi == 'Tahap Tahun Pertama STEI'