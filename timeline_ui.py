from datetime import datetime

# Kode warna untuk terminal agar UI terlihat profesional
HIJAU = '\033[92m'
KUNING = '\033[93m'
MERAH = '\033[91m'
BIRU = '\033[94m'
BOLD = '\033[1m'
RESET = '\033[0m'

def tampilkan_tabel(data_tugas):
    """
    Fungsi ini menerima list of dictionary dari modul lain
    dan menampilkannya dalam bentuk tabel yang rapi.
    """
    if not data_tugas:
        print(f"\n{KUNING} [!] Belum ada data tugas untuk ditampilkan. {RESET}")
        return

    # Sorting berdasarkan deadline agar yang paling dekat muncul di atas
    try:
        sorted_data = sorted(data_tugas, key=lambda x: datetime.strptime(x['deadline'], "%Y-%m-%d"))
    except Exception as e:
        print(f"{MERAH}Format tanggal salah! Pastikan formatnya YYYY-MM-DD.{RESET}")
        sorted_data = data_tugas

    print(f"\n{BOLD}{BIRU}=== DAFTAR DEADLINE TUGAS ==={RESET}")
    header = f"{'ID':<4} | {'Nama Tugas':<20} | {'Deadline':<15} | {'Status'}"
    print(f"{BOLD}{header}{RESET}")
    print("-" * 60)
    
    for t in sorted_data:
        # Penentuan warna berdasarkan status
        status = t['status'].lower()
        if status == 'siap' or status == 'selesai':
            warna = HIJAU
        elif status == 'proses':
            warna = KUNING
        else:
            warna = MERAH
            
        print(f"{t['id']:<4} | {t['nama']:<20} | {t['deadline']:<15} | {warna}{t['status']:<10}{RESET}")
    
    print("-" * 60)
    print(f"Total: {len(data_tugas)} Tugas Terdaftar\n")

# Bagian ini dikosongkan dari sampel agar tidak muncul saat di-import
if __name__ == "__main__":
    print("Modul UI siap digunakan. Silakan panggil fungsi 'tampilkan_tabel(data)' dari modul utama.")