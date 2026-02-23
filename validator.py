from datetime import datetime

def validasi_input(nama, tanggal):
    errors = []

    if not nama.strip():
        errors.append("Nama tugas tidak boleh kosong!")
    elif len(nama.strip()) < 3:
        errors.append("Nama tugas terlalu pendek!")

    try:
        datetime.strptime(tanggal, "%Y-%m-%d")
    except ValueError:
        errors.append("Format tanggal salah (Gunakan YYYY-MM-DD)!")

    return errors