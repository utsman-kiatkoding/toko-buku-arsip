STOK = {
    "Laskar Pelangi": 10,
    "Bumi Manusia": 5,
    "Pulang": 8,
}


def cek_stok(judul):
    return STOK.get(judul, 0)


def tambah_stok(judul, jumlah):
    STOK[judul] = STOK.get(judul, 0) + jumlah
    return STOK[judul]
