STOK = {
    "Laskar Pelangi": 10,
    "Bumi Manusia": 5,
    "Pulang": 8,
}


def cek_stok(judul):
    return STOK.get(judul, 0)
