def format_rupiah(angka):
    return "Rp" + format(int(angka), ",").replace(",", ".")
