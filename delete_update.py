def docum_menu_edit(data):
    """
    Menghapus tugas berdasarkan ID
    atau mengubah status tugas menjadi 'Selesai'.
    Parameter:
        data (list): daftar tugas
    Return:
        list: data yang telah diperbarui
    """

def menu_edit(data):
    id_target = int(input("Masukkan ID tugas: "))
    for t in data:
        if t['id'] == id_target:
            print("1. Hapus | 2. Tandai Selesai")
            opsi = input("Pilih: ")
            if opsi == "1":
                data.remove(t)
                print("🗑️ Berhasil dihapus")
            elif opsi == "2":
                t['status'] = "Selesai"
                print("✔️ Status diperbarui")
            return data
    print("⚠️ ID tidak ditemukan")
    return data