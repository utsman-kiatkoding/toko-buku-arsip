def cari(kata, daftar):
    return [j for j in daftar if kata.lower() in j.lower()]
