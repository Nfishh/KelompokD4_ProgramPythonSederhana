import storage
import create
import delete_update
import timeline_ui

def main():
    data = storage.load_data()
    while True:
        print("\n=== SMART TASK MANAGER ===")
        print("1. Lihat Task")
        print("2. Tambah Task")
        print("3. Hapus/Update")
        print("0. Keluar")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            timeline_ui.tampilkan_tabel(data)
        elif pilih == "2":
            data = create.tambah_tugas(data)
            storage.save_data(data)
        elif pilih == "3":
            data = delete_update.menu_edit(data)
            storage.save_data(data)
        elif pilih == "0":
            break

if __name__ == "__main__":
    main()