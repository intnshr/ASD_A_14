# =======================================================
# ANTRIAN TIKET BIOSKOP
# KELAS : TPL A
# KELOMPOK : THREECUTE
# ANGGOTA :
# 1. INTAN SAHARA NURAFNI (J0403251008)
# 2. NAYLATUL FADHILAH (J0403251033)
# 3. FAIZA AGHNAITA (J0403251122)
# =======================================================

with open("data_antrian.txt","r",encoding="utf-8") as file:
    antrian = []

import os

def load_data():
    global antrian
    antrian = []

    base_dir = os.path.dirname(os.path.abspath(__file__))
    path_file = os.path.join(base_dir, "data_antrian.txt")


    try:
        with open(path_file, "r", encoding="utf-8") as file:
            for baris in file:
                nama = baris.strip()
                if nama != "":
                    antrian.append(nama)


    except FileNotFoundError:
        print("File tidak ditemukan")



def save_data():
    """Menyimpan isi list antrian ke file TXT."""
    with open(NAMA_FILE, "w", encoding="utf-8") as file:
        for nama in antrian:
            file.write(nama + "\n")


def tambah_antrian():
    """Create: menambahkan pembeli ke antrian."""
    nama = input("Masukkan nama pembeli: ").strip()

    if nama == "":
        print("Nama tidak boleh kosong.")
        return

    antrian.append(nama)
    save_data()
    print(f"{nama} berhasil ditambahkan ke antrian.")


def tampilkan_antrian():
    """Read: menampilkan seluruh isi antrian."""
    if len(antrian) == 0:
        print("Antrian masih kosong.")
        return

    print("\n=== DAFTAR ANTRIAN ===")
    for i, nama in enumerate(antrian, start=1):
        print(f"{i}. {nama}")


def update_antrian():
    """Update: mengubah nama pembeli berdasarkan nomor antrian."""
    if len(antrian) == 0:
        print("Antrian kosong, tidak ada yang bisa diubah.")
        return

    tampilkan_antrian()

    try:
        nomor = int(input("Masukkan nomor antrian yang ingin diubah: "))
    except ValueError:
        print("Input harus berupa angka.")
        return

    if nomor < 1 or nomor > len(antrian):
        print("Nomor antrian tidak valid.")
        return

    nama_baru = input("Masukkan nama baru: ").strip()
    if nama_baru == "":
        print("Nama baru tidak boleh kosong.")
        return

    nama_lama = antrian[nomor - 1]
    antrian[nomor - 1] = nama_baru
    save_data()
    print(f"Data berhasil diubah: {nama_lama} -> {nama_baru}")


def layani_antrian():
    """Delete: melayani dan menghapus pembeli paling depan."""
    if len(antrian) == 0:
        print("Antrian kosong.")
        return

    nama = antrian.pop(0)
    save_data()
    print(f"Pembeli yang dilayani: {nama}")


def lihat_depan():
    """Menampilkan pembeli paling depan tanpa menghapus."""
    if len(antrian) == 0:
        print("Antrian kosong.")
        return

    print(f"Antrian paling depan: {antrian[0]}")


def jumlah_antrian():
    """Menampilkan jumlah pembeli dalam antrian."""
    print(f"Jumlah antrian saat ini: {len(antrian)}")


def menu():
    while True:
        print("\n=== SISTEM ANTRIAN TIKET BIOSKOP ===")
        print("1. Tambah Antrian")
        print("2. Tampilkan Antrian")
        print("3. Update Data Antrian")
        print("4. Layani Antrian")
        print("5. Lihat Antrian Paling Depan")
        print("6. Jumlah Antrian")
        print("7. Keluar")

        pilih = input("Pilih menu (1-7): ").strip()

        if pilih == "1":
            tambah_antrian()
        elif pilih == "2":
            tampilkan_antrian()
        elif pilih == "3":
            update_antrian()
        elif pilih == "4":
            layani_antrian()
        elif pilih == "5":
            lihat_depan()
        elif pilih == "6":
            jumlah_antrian()
        elif pilih == "7":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih 1-7.")


load_data()
menu()