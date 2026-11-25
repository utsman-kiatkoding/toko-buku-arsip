def harga_akhir(harga, diskon_persen=0):
    """Hitung harga setelah diskon."""
    return harga - (harga * diskon_persen / 100)


if __name__ == "__main__":
    print(harga_akhir(80000, 10))
    print(harga_akhir(50000))
