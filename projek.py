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

    # ===================================================
    # SAVE DATA ANTRIAN
    # ===================================================

    def save_data(self):

        with open(
            self.file_antrian,
            "w",
            encoding="utf-8"
        ) as file:

            temp = self.front

            while temp:

                file.write(
                    f"{temp.nama}|{temp.kursi}\n"
                )

                temp = temp.next

    # ===================================================
    # SAVE DATA KURSI
    # ===================================================

    def save_kursi(self):

        with open(self.file_kursi, "w") as file:

            file.write(
                str(self.kursi_tersedia)
            )

    # ===================================================
    # CEK KURSI
    # ===================================================

    def cek_kursi(self, kursi):

        temp = self.front

        while temp:

            if temp.kursi == kursi:

                return True

            temp = temp.next

        return False

    # ===================================================
    # ENQUEUE
    # ===================================================

    def enqueue(self):

        # Jika kursi habis
        if self.kursi_tersedia == 0:

            print("\n================================")
            print("KURSI BIOSKOP SUDAH HABIS")
            print("ANTRIAN DITUTUP")
            print("================================")

            return

        nama = input(
            "Masukkan nama pembeli : "
        ).strip()

        # Validasi nama
        if nama == "":

            print("Nama tidak boleh kosong.")
            return

        if nama.isdigit():

            print("Nama tidak boleh angka.")
            return

        kursi = input(
            "Masukkan nomor kursi : "
        ).upper().strip()
        
        if not self.validasi_kursi(kursi):

            print(
                    "Nomor kursi tidak valid.\n"
                    "Gunakan format A1 sampai J10."
            )

            return


        # Validasi kursi
        if kursi == "":

            print("Nomor kursi tidak boleh kosong.")
            return

        # Cek kursi sudah dipakai
        if self.cek_kursi(kursi):

            print("Nomor kursi sudah digunakan.")
            return

        # Tambah node
        self.tambah_node(nama, kursi)

        # Kursi berkurang
        self.kursi_tersedia -= 1

        # Save file
        self.save_data()
        self.save_kursi()

        print(f"{nama} berhasil masuk antrian.")
    
    # ===================================================
    # DEQUEUE
    # ===================================================

    def dequeue(self):

        if self.front is None:

            print("Antrian kosong.")
            return

        nama = self.front.nama
        kursi = self.front.kursi

        # Geser front
        self.front = self.front.next

        # Jika kosong
        if self.front is None:

            self.rear = None

        self.jumlah -= 1

        # Save data
        self.save_data()

        print("\n=== PEMBELI DILAYANI ===")
        print(f"Nama   : {nama}")
        print(f"Kursi  : {kursi}")


    # ===================================================
    # TAMPILKAN ANTRIAN
    # ===================================================

    def tampilkan_antrian(self):

        if self.front is None:

            print("Antrian kosong.")
            return

        print("\n=== DAFTAR ANTRIAN BIOSKOP ===")

        temp = self.front
        nomor = 1

        while temp:

            print(
                f"{nomor}. "
                f"{temp.nama} - Kursi {temp.kursi}"
            )

            temp = temp.next
            nomor += 1

    # ===================================================
    # UPDATE NOMOR KURSI
    # ===================================================

    def update_kursi(self):

        if self.front is None:

            print("Antrian kosong.")
            return

        self.tampilkan_antrian()

        try:

            nomor = int(
                input("Pilih nomor antrian : ")
            )

        except ValueError:

            print("Input harus angka.")
            return

        if nomor < 1 or nomor > self.jumlah:

            print("Nomor tidak valid.")
            return

        kursi_baru = input(
            "Masukkan kursi baru : "
        ).upper().strip()

        if not self.validasi_kursi(kursi_baru):

            print(
                "Nomor kursi tidak valid.\n"
                "Gunakan format A1 sampai J10."
            )

            return

        # Validasi
        if kursi_baru == "":

            print("Nomor kursi tidak boleh kosong.")
            return

        # Cek kursi
        if self.cek_kursi(kursi_baru):

            print("Nomor kursi sudah digunakan.")
            return

        # Traversal linked list
        temp = self.front

        for i in range(1, nomor):

            temp = temp.next

        kursi_lama = temp.kursi

        temp.kursi = kursi_baru

        # Save data
        self.save_data()

        print(
            f"Kursi berhasil diubah "
            f"{kursi_lama} -> {kursi_baru}"
        )

    # ===================================================
    # SEARCHING
    # ===================================================

    def cari_data(self):

        if self.front is None:

            print("Antrian kosong.")
            return

        keyword = input(
            "Masukkan nama / kursi : "
        ).lower()

        temp = self.front
        nomor = 1
        ditemukan = False

        print("\n=== HASIL PENCARIAN ===")

        while temp:

            if (
                keyword in temp.nama.lower()
                or keyword in temp.kursi.lower()
            ):

                print(
                    f"{nomor}. "
                    f"{temp.nama} - Kursi {temp.kursi}"
                )

                ditemukan = True

            temp = temp.next
            nomor += 1

        if not ditemukan:

            print("Data tidak ditemukan.")

    # ===================================================
    # SORTING KURSI
    # ===================================================
    def merge_sort(self, data):

        if len(data) <= 1:
            return data

        tengah = len(data) // 2

        kiri = self.merge_sort(data[:tengah])
        kanan = self.merge_sort(data[tengah:])

        hasil = []

        i = 0
        j = 0

        while i < len(kiri) and j < len(kanan):

            if kiri[i][1] <= kanan[j][1]:

                hasil.append(kiri[i])
                i += 1

            else:

                hasil.append(kanan[j])
                j += 1

        while i < len (kiri):

                hasil.append(kiri[i])
                i += 1

        while j < len(kanan):

                hasil.append(kanan[j])
                j += 1

        return hasil

    def sorting_kursi(self):

        if self.front is None:

            print("Antrian kosong.")
            return

        data = []

        temp = self.front

        while temp:

            data.append(
                (temp.nama, temp.kursi)
            )

            temp = temp.next

        # Merge Sort
        data = self.merge_sort(data)

        print("\n=== SORTING NOMOR KURSI ===")

        for i, item in enumerate(data, start=1):

            print(
                f"{i}. "
                f"{item[0]} - Kursi {item[1]}"
            )







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
