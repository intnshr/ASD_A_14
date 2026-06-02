# =======================================================
# ANTRIAN TIKET BIOSKOP
# KELAS : TPL A
# KELOMPOK : THREECUTE
# ANGGOTA :
# 1. INTAN SAHARA NURAFNI (J0403251008)
# 2. NAYLATUL FADHILAH (J0403251033)
# 3. FAIZA AGHNAITA (J0403251122)
# =======================================================

import os

# =======================================================
# CLASS NODE (LINKED LIST)
# =======================================================

class Node:

    def __init__(self, nama, kursi):

        self.nama = nama
        self.kursi = kursi
        self.next = None

# =======================================================
# CLASS QUEUE BIOSKOP
# =======================================================

class QueueBioskop:

    def validasi_kursi(self, kursi):

        if len(kursi) < 2:
            return False

        huruf = kursi[0]
        angka = kursi[1:]

        if huruf not in "ABCDEFGHIJ":
            return False

        if not angka.isdigit():
            return False

        angka = int(angka)

        if angka < 1 or angka > 10:
            return False

        return True

    def __init__(self):

        # Pointer queue
        self.front = None
        self.rear = None

        # Jumlah antrian
        self.jumlah = 0

        # Total kursi studio
        self.total_kursi = 100

        # Lokasi file
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))

        self.file_antrian = os.path.join(
            BASE_DIR,
            "data_antrian.txt"
        )

        self.file_kursi = os.path.join(
            BASE_DIR,
            "data_kursi.txt"
        )

        # Load data dari txt
        self.load_data()
        self.load_kursi()

    # ===================================================
    # LOAD DATA ANTRIAN
    # ===================================================

    def load_data(self):

        try:

            with open(
                self.file_antrian,
                "r",
                encoding="utf-8"
            ) as file:

                for baris in file:

                    data = baris.strip().split("|")

                    if len(data) == 2:

                        nama = data[0]
                        kursi = data[1]

                        self.tambah_node(nama, kursi)

        except FileNotFoundError:

            print("File antrian tidak ditemukan.")


    # ===================================================
    # LOAD DATA KURSI
    # ===================================================

    def load_kursi(self):

        try:

            with open(self.file_kursi, "r") as file:

                self.kursi_tersedia = int(
                    file.read()
                )

        except:

            self.kursi_tersedia = self.total_kursi




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
