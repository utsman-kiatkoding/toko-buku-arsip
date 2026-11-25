KATEGORI = {
    "Laskar Pelangi": "Novel",
    "Bumi Manusia": "Sejarah",
    "Pulang": "Novel",
}


def kategori_buku(judul):
    return KATEGORI.get(judul, "Umum")
