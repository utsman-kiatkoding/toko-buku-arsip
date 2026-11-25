import unittest

from harga import harga_akhir


class TestHarga(unittest.TestCase):
    def test_tanpa_diskon(self):
        self.assertEqual(harga_akhir(50000), 50000)

    def test_diskon_sepuluh_persen(self):
        self.assertEqual(harga_akhir(80000, 10), 72000)


if __name__ == "__main__":
    unittest.main()
