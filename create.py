import validator

def tambah_tugas(data):
    nama = input("Nama Tugas: ")
    deadline = input("Deadline (YYYY-MM-DD): ")
    
    errors = validator.validasi_input(nama, deadline)
    if not errors:
        new_id = max([t['id'] for t in data], default=0) + 1
        data.append({"id": new_id, "nama": nama, "deadline": deadline, "status": "Belum"})
        print("✅ Tugas berhasil ditambah!")
    else:
        for err in errors: print(f"❌ {err}")
    return data