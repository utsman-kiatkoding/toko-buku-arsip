def cari(kata, daftar):
    return [j for j in daftar if kata.lower() in j.lower()]


def cari_pertama(kata, daftar):
    hasil = cari(kata, daftar)
    return hasil[0] if hasil else None
