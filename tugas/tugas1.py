students = []

while True:
    print("\n=== MENU ===")
    print("1. Tambah")
    print("2. Lihat")
    print("3. Ubah")
    print("4. Hapus")
    print("5. Keluar")

    pilih = input("Pilih: ")

    
    if pilih == "1":
        name = input("Nama: ")
        umur = input("Umur: ")
        students.append({"name": name, "age": umur})
        print("✅ Ditambahkan!")

    
    elif pilih == "2":
        if not students:
            print("📭 Belum ada data.")
        else:
            for i, s in enumerate(students):
                print(f"{i}. {s['name']} - {s['age']}")

    
    elif pilih == "3":
        idx = input("Index: ")
        if idx.isdigit() and 0 <= int(idx) < len(students):
            idx = int(idx)
            students[idx]["name"] = input("Nama baru: ")
            students[idx]["age"] = input("Umur baru: ")
            print("✏️ Diubah!")
        else:
            print("❌ Index salah!")

    
    elif pilih == "4":
        idx = input("Index: ")
        if idx.isdigit() and 0 <= int(idx) < len(students):
            students.pop(int(idx))
            print("🗑️ Dihapus!")
        else:
            print("❌ Index salah!")

    
    elif pilih == "5":
        print("👋 Keluar.")
        break

    else:
        print("⚠️ Menu tidak ada.")
