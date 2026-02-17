DATA_FILE = "data_perpustakaan.txt"


# ==========================
# USER (PARENT CLASS)
# ==========================
class User:
    def __init__(self, nama):
        self.__nama = nama  # private variable (encapsulation)

    def get_nama(self):
        return self.__nama


class Admin(User):
    pass


class Santri(User):
    pass


# ==========================
# BOOK CLASS
# ==========================
class Book:
    def __init__(self, judul, kategori, stok):
        self.__judul = judul
        self.__kategori = kategori
        self.__stok = stok

    # Getter
    def get_judul(self):
        return self.__judul

    def get_kategori(self):
        return self.__kategori

    def get_stok(self):
        return self.__stok

    # Setter / aksi
    def tambah_stok(self, jumlah):
        self.__stok += jumlah

    def kurangi_stok(self):
        # Pastikan stok tidak minus
        if self.__stok > 0:
            self.__stok -= 1
            return True
        return False

    def info(self):
        return f"{self.__judul} | {self.__kategori} | Stok: {self.__stok}"


# ==========================
# LOAN CLASS
# ==========================
class Loan:
    def __init__(self, peminjam, judul_buku, tanggal):
        self.__peminjam = peminjam
        self.__judul_buku = judul_buku
        self.__tanggal = tanggal

    def serialize(self):
        # Ubah ke teks agar bisa disimpan
        return (
            self.__peminjam.get_nama()
            + "|"
            + self.__judul_buku
            + "|"
            + self.__tanggal
        )

    @staticmethod
    def deserialize(text):
        bagian = text.split("|")
        santri = Santri(bagian[0])
        return Loan(santri, bagian[1], bagian[2])

    def info(self):
        return (
            self.__peminjam.get_nama()
            + " meminjam '"
            + self.__judul_buku
            + "' pada "
            + self.__tanggal
        )


# ==========================
# LIBRARY CLASS
# ==========================
class Library:
    def __init__(self):
        self.__books = []
        self.__loans = []

    # ---------- BOOK ----------
    def tambah_buku(self, book):
        self.__books.append(book)

    def tampilkan_buku(self):
        print("\n📚 DAFTAR KITAB")
        for book in self.__books:
            print("-", book.info())

    def cari_judul(self, judul):
        for book in self.__books:
            if book.get_judul().lower() == judul.lower():
                return book
        return None

    def cari_kategori(self, kategori):
        hasil = []
        for book in self.__books:
            if book.get_kategori().lower() == kategori.lower():
                hasil.append(book)
        return hasil

    # ---------- PINJAM ----------
    def pinjam_buku(self, santri, judul, tanggal):
        buku = self.cari_judul(judul)

        if not buku:
            print("❌ Buku tidak ditemukan.")
            return

        if buku.kurangi_stok():
            loan = Loan(santri, judul, tanggal)
            self.__loans.append(loan)
            print("✅", loan.info())
        else:
            print("❌ Stok habis!")

    # ---------- KEMBALI ----------
    def kembalikan_buku(self, judul):
        buku = self.cari_judul(judul)

        if not buku:
            print("❌ Buku tidak ditemukan.")
            return

        buku.tambah_stok(1)
        print("✅ Buku dikembalikan.")

    # ---------- RIWAYAT ----------
    def tampilkan_peminjaman(self):
        print("\n📄 RIWAYAT PEMINJAMAN")
        if not self.__loans:
            print("Belum ada peminjaman.")
            return

        for loan in self.__loans:
            print("-", loan.info())

    # ---------- SAVE / LOAD ----------
    def save_data(self):
        with open(DATA_FILE, "w") as file:
            # Simpan buku
            file.write("[BOOKS]\n")
            for b in self.__books:
                file.write(
                    b.get_judul()
                    + "|"
                    + b.get_kategori()
                    + "|"
                    + str(b.get_stok())
                    + "\n"
                )

            # Simpan peminjaman
            file.write("[LOANS]\n")
            for l in self.__loans:
                file.write(l.serialize() + "\n")

    def load_data(self):
        try:
            with open(DATA_FILE, "r") as file:
                mode = ""
                for line in file:
                    line = line.strip()

                    if line == "[BOOKS]":
                        mode = "BOOKS"
                        continue
                    elif line == "[LOANS]":
                        mode = "LOANS"
                        continue

                    if not line:
                        continue

                    if mode == "BOOKS":
                        data = line.split("|")
                        self.__books.append(
                            Book(data[0], data[1], int(data[2]))
                        )

                    elif mode == "LOANS":
                        self.__loans.append(Loan.deserialize(line))

        except:
            # Jika file belum ada, abaikan
            pass


# ==========================
# INPUT VALIDATION
# ==========================
def input_menu(prompt):
    while True:
        nilai = input(prompt)
        if nilai.isdigit():
            return nilai
        print("⚠️ Masukkan angka yang benar.")


# ==========================
# MAIN PROGRAM
# ==========================
def main():
    library = Library()
    library.load_data()

    # Data awal jika kosong
    if not library.cari_judul("Fathul Qarib"):
        library.tambah_buku(Book("Fathul Qarib", "Fiqh", 3))
        library.tambah_buku(Book("Tafsir Jalalain", "Tafsir", 2))
        library.tambah_buku(Book("Alfiyah Ibnu Malik", "Nahwu", 1))

    while True:
        print("\n=== 📚 MENU PERPUSTAKAAN KITAB ===")
        print("1. Lihat Semua Kitab")
        print("2. Cari Judul")
        print("3. Cari Kategori")
        print("4. Pinjam Kitab")
        print("5. Kembalikan Kitab")
        print("6. Riwayat Peminjaman")
        print("7. Simpan & Keluar")

        pilih = input_menu("Pilih menu: ")

        if pilih == "1":
            library.tampilkan_buku()

        elif pilih == "2":
            judul = input("Judul: ")
            buku = library.cari_judul(judul)
            print(buku.info() if buku else "❌ Tidak ditemukan.")

        elif pilih == "3":
            kategori = input("Kategori: ")
            hasil = library.cari_kategori(kategori)

            if hasil:
                for b in hasil:
                    print("-", b.info())
            else:
                print("❌ Tidak ada kitab.")

        elif pilih == "4":
            nama = input("Nama santri: ")
            judul = input("Judul kitab: ")
            tanggal = input("Tanggal pinjam (YYYY-MM-DD): ")

            santri = Santri(nama)
            library.pinjam_buku(santri, judul, tanggal)

        elif pilih == "5":
            judul = input("Judul kitab: ")
            library.kembalikan_buku(judul)

        elif pilih == "6":
            library.tampilkan_peminjaman()

        elif pilih == "7":
            library.save_data()
            print("💾 Data disimpan. Program selesai.")
            break


if __name__ == "__main__":
    main()

# DATA_FILE = "data_perpustakaan.txt"



# class User:
#     def __init__(self, nama):
#         self.__nama = nama 

#     def get_nama(self):
#         return self.__nama


# class Admin(User):
#     pass


# class Santri(User):
#     pass



# class Book:
#     def __init__(self, judul, kategori, stok):
#         self.__judul = judul
#         self.__kategori = kategori
#         self.__stok = stok

#     def get_judul(self):
#         return self.__judul

#     def get_kategori(self):
#         return self.__kategori

#     def get_stok(self):
#         return self.__stok

#     def tambah_stok(self, jumlah):
#         self.__stok += jumlah

#     def kurangi_stok(self):
#         if self.__stok > 0:
#             self.__stok -= 1
#             return True
#         return False

#     def info(self):
#         return f"{self.__judul} | {self.__kategori} | Stok: {self.__stok}"



# class Loan:
#     def __init__(self, peminjam, judul_buku, tanggal):
#         self.__peminjam = peminjam
#         self.__judul_buku = judul_buku
#         self.__tanggal = tanggal

#     def serialize(self):
#         return (
#             self.__peminjam.get_nama()
#             + "|"
#             + self.__judul_buku
#             + "|"
#             + self.__tanggal
#         )

#     @staticmethod
#     def deserialize(text):
#         bagian = text.split("|")
#         santri = Santri(bagian[0])
#         return Loan(santri, bagian[1], bagian[2])

#     def info(self):
#         return (
#             self.__peminjam.get_nama()
#             + " meminjam '"
#             + self.__judul_buku
#             + "' pada "
#             + self.__tanggal
#         )



# class Library:
#     def __init__(self):
#         self.__books = []
#         self.__loans = []


#     def tambah_buku(self, book):
#         self.__books.append(book)

#     def tampilkan_buku(self):
#         print("\n📚 DAFTAR KITAB")
#         for book in self.__books:
#             print("-", book.info())

#     def cari_judul(self, judul):
#         for book in self.__books:
#             if book.get_judul().lower() == judul.lower():
#                 return book
#         return None

#     def cari_kategori(self, kategori):
#         hasil = []
#         for book in self.__books:
#             if book.get_kategori().lower() == kategori.lower():
#                 hasil.append(book)
#         return hasil

   
#     def pinjam_buku(self, santri, judul, tanggal):
#         buku = self.cari_judul(judul)

#         if not buku:
#             print("❌ ga ada bukunya kocak.")
#             return

#         if buku.kurangi_stok():
#             loan = Loan(santri, judul, tanggal)
#             self.__loans.append(loan)
#             print("✅", loan.info())
#         else:
#             print("❌ gua bilang Stok sdh habis!, ngeyel banget")

#     def kembalikan_buku(self, judul):
#         buku = self.cari_judul(judul)

#         if not buku:
#             print("❌ dibilangin ga ada bukunya.")
#             return

#         buku.tambah_stok(1)
#         print("✅ Buku dikembalikan.")

#     def tampilkan_peminjaman(self):
#         print("\n📄 RIWAYAT PEMINJAMAN")
#         if not self.__loans:
#             print("Belum ada peminjaman.")
#             return

#         for loan in self.__loans:
#             print("-", loan.info())

#     def save_data(self):
#         with open(DATA_FILE, "w") as file:
#             file.write("[BOOKS]\n")
#             for b in self.__books:
#                 file.write(
#                     b.get_judul()
#                     + "|"
#                     + b.get_kategori()
#                     + "|"
#                     + str(b.get_stok())
#                     + "\n"
#                 )

     
#             file.write("[LOANS]\n")
#             for l in self.__loans:
#                 file.write(l.serialize() + "\n")

#     def load_data(self):
#         try:
#             with open(DATA_FILE, "r") as file:
#                 mode = ""
#                 for line in file:
#                     line = line.strip()

#                     if line == "[BOOKS]":
#                         mode = "BOOKS"
#                         continue
#                     elif line == "[LOANS]":
#                         mode = "LOANS"
#                         continue

#                     if not line:
#                         continue

#                     if mode == "BOOKS":
#                         data = line.split("|")
#                         self.__books.append(
#                             Book(data[0], data[1], int(data[2]))
#                         )

#                     elif mode == "LOANS":
#                         self.__loans.append(Loan.deserialize(line))

#         except:
#             pass



# def input_menu(prompt):
#     while True:
#         nilai = input(prompt)
#         if nilai.isdigit():
#             return nilai
#         print("⚠️ lu bisa ketik angka yg bener ga sih?.")



# def main():
#     library = Library()
#     library.load_data()

#     if not library.cari_judul("Fathul Qarib"):
#         library.tambah_buku(Book("Fathul Aly", "Fiqh", 3))
#         library.tambah_buku(Book("Tafsir Al-muyassar", "Tafsir", 3))
#         library.tambah_buku(Book("Tamhidussabil", "Nahwu", 3))
#         library.tambah_buku(Book("Aqidatuna", "Aqidah", 3))

#     while True:
#         print("\n=== 📚 MENU PERPUSTAKAAN KITAB ===")
#         print("1. Lihat Semua Kitab")
#         print("2. Cari Judul")
#         print("3. Cari Kategori")
#         print("4. Pinjam Kitab")
#         print("5. Kembalikan Kitab")
#         print("6. Riwayat Peminjaman")
#         print("7. Simpan & Keluar")

#         pilih = input_menu("Pilih menu: ")

#         if pilih == "1":
#             library.tampilkan_buku()

#         elif pilih == "2":
#             judul = input("Judul: ")
#             buku = library.cari_judul(judul)
#             print(buku.info() if buku else "❌ ga ada kocak, batu bet lu.")

#         elif pilih == "3":
#             kategori = input("Kategori: ")
#             hasil = library.cari_kategori(kategori)

#             if hasil:
#                 for b in hasil:
#                     print("-", b.info())
#             else:
#                 print("❌ dibilangin ga ada kitabnya.")

#         elif pilih == "4":
#             nama = input("Nama santri: ")
#             judul = input("Judul kitab: ")
#             tanggal = input("Tanggal pinjam (YYYY-MM-DD): ")

#             santri = Santri(nama)
#             library.pinjam_buku(santri, judul, tanggal)

#         elif pilih == "5":
#             judul = input("Judul kitab: ")
#             library.kembalikan_buku(judul)

#         elif pilih == "6":
#             library.tampilkan_peminjaman()

#         elif pilih == "7":
#             library.save_data()
#             print("💾 Data disimpan. Program selesai, jangan kau paksa lagi!!!...")
#             break


# if __name__ == "__main__":
#     main()
