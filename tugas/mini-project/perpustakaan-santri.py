

DATA_FILE = "data_perpustakaan.txt"


books = []
loans = []


def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            mode = ""
            for line in f:
                line = line.strip()

                if line == "[BOOKS]":
                    mode = "books"
                    continue
                elif line == "[LOANS]":
                    mode = "loans"
                    continue

                if not line:
                    continue

                if mode == "books":
                    judul, kategori, stok = line.split("|")
                    books.append({
                        "judul": judul,
                        "kategori": kategori,
                        "stok": int(stok)
                    })

                elif mode == "loans":
                    loans.append(line)
    except:
        pass


def save_data():
    with open(DATA_FILE, "w") as f:
        f.write("[BOOKS]\n")
        for b in books:
            f.write(f"{b['judul']}|{b['kategori']}|{b['stok']}\n")

        f.write("[LOANS]\n")
        for l in loans:
            f.write(l + "\n")


def tampilkan_buku():
    print("\n📚 DAFTAR KITAB")
    for b in books:
        print(f"- {b['judul']} | {b['kategori']} | Stok: {b['stok']}")


def cari_buku(judul):
    for b in books:
        if b["judul"].lower() == judul.lower():
            return b
    return None


def pinjam_buku():
    nama = input("Nama santri: ")
    judul = input("Judul kitab: ")
    tanggal = input("Tanggal (YYYY-MM-DD): ")

    buku = cari_buku(judul)

    if not buku:
        print("❌ Kitab tidak ada.")
        return  

    if buku["stok"] > 0:
        buku["stok"] -= 1
        loans.append(f"{nama}|{judul}|{tanggal}")
        print(f"✅ {nama} meminjam '{judul}' pada {tanggal}")
    else:
        print("❌ Stok kitab habis!")


def kembalikan_buku():
    judul = input("Judul kitab: ")
    buku = cari_buku(judul)

    if not buku:
        print("❌ Kitab tidak ditemukan.")
        return

    buku["stok"] += 1
    print("✅ Kitab dikembalikan.")


def riwayat():
    print("\n📄 RIWAYAT PEMINJAMAN")
    if not loans:
        print("Belum ada peminjaman.")
        return

    for l in loans:
        nama, judul, tanggal = l.split("|")
        print(f"- {nama} meminjam '{judul}' pada {tanggal}")


def main():
    load_data()

    if not books:
        books.append({"judul": "Fathul Aly", "kategori": "Fiqh", "stok": 3})
        books.append({"judul": "Tafsir Al-Muyassar", "kategori": "Tafsir", "stok": 3})
        books.append({"judul": "Tamhidussabil", "kategori": "Nahwu", "stok": 3})
        books.append({"judul": "Aqidatuna", "kategori": "Aqidah", "stok": 3})

    while True:
        print("\n=== 📚 MENU PERPUSTAKAAN KITAB ===")
        print("1. Lihat Kitab")
        print("2. Cari Kitab")
        print("3. Pinjam Kitab")
        print("4. Kembalikan Kitab")
        print("5. Riwayat Peminjaman")
        print("6. Simpan & Keluar")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            tampilkan_buku()

        elif pilih == "2":
            judul = input("Judul: ")
            buku = cari_buku(judul)
            if buku:
                print(f"{buku['judul']} | {buku['kategori']} | Stok: {buku['stok']}")
            else:
                print("❌ Kitab tidak ada.")

        elif pilih == "3":
            pinjam_buku()

        elif pilih == "4":
            kembalikan_buku()

        elif pilih == "5":
            riwayat()

        elif pilih == "6":
            save_data()
            print("💾 Data disimpan. Program selesai.")
            break


main()
