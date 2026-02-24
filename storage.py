import json
import os

FILE_NAME = "data.json" # Bikin variabel untuk nama filenya biar gampang kalau mau diganti

def load_data():
    """Fungsi untuk membaca data dari file JSON"""
    # Pengecekan pertama, file data.json-nya udah ada belum di folder?
    if not os.path.exists(FILE_NAME):
        # Kalau belum ada, balikin list kosong. Nanti otomatis kebuat pas disave.
        return []
    
    # Kalau filenya ada, kita buka dan baca
    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)
            return data
    except json.JSONDecodeError:
        return [] # Jaga-jaga kalau filenya ada tapi isinya kosong atau error (corrupt)

def save_data(data):
    """Fungsi untuk menyimpan data baru ke file JSON"""
    with open(FILE_NAME, "w") as file: # Dapat ngebuka filenya dengan mode "w" (write/menulis ulang)
        # indent=4 itu biar tulisan di JSON-nya rapi ke bawah, gak mpet-mpetan sejajar
        json.dump(data, file, indent=4)


# === BAGIAN TESTING === (CUMA BUAT TESTING APAKAH KODE/SYNTAKS DIATAS JALAN/TIDAK)

# if __name__ == "__main__":
    # print("Testing ambil data...")
    # data_sekarang = load_data()
    # print("Isi data awal:", data_sekarang)

    # print("\nTesting nambahin data baru...")
    # data_baru = {"id": 1, "tugas": "Bikin Storage", "pic": "Iqbal"}
    # data_sekarang.append(data_baru)
    
    # save_data(data_sekarang)
    # print("Data berhasil disave! Cek file data.json di folder kalian.")