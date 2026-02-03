print("hello world!")
#cara membuat fungsi
#struktur: def namaFungsi(prameternya)
def hello(nama):
    print(f"hello {nama}")
#panggil dibawah, gk blh nyatu dgn web
hello("ujang")
hello("nyoman")
hello("Azmie")
hello("doelll")

#minta 3 parameter
def nilai(nama , uts , uas):
    rumus = (uts + uas) / 2
    print(f"nilai akhir {nama}: {rumus}")

nilai("ahmad",99.9,99.9 )
nilai("banyu",80,90 )
nilai("azka",70 ,80 )
nilai("zain",75 ,85 )


# students = []

# while True:
#     print("\n=== MENU ===")
#     print("1. Tambah data")
#     print("2. Lihat data")
#     print("3. Ubah data")
#     print("4. Hapus data")
#     print("5. Keluar")

#     pilihan = input("Pilih menu: ")

#     if pilihan == "1":
#         name = input("Nama: ")
#         age = input("Umur: ")
#         students.append({"name": name, "age": age})
#         print("Data ditambah!")

#     elif pilihan == "2":
#         if not students:
#             print("Belum ada data.")
#         else:
#             for i, s in enumerate(students):
#                 print(i, s["name"], "-", s["age"])

#     elif pilihan == "3":
#         index = int(input("Index yang mau diubah: "))
#         if 0 <= index < len(students):
#             name = input("Nama baru: ")
#             age = input("Umur baru: ")
#             students[index]["name"] = name
#             students[index]["age"] = age
#             print("Data diubah!")
#         else:
#             print("Index salah!")

#     elif pilihan == "4":
#         index = int(input("Index yang mau dihapus: "))
#         if 0 <= index < len(students):
#             students.pop(index)
#             print("Data dihapus!")
#         else:
#             print("Index salah!")

#     elif pilihan == "5":
#         print("Keluar program.")
#         break

#     else:
#         print("Pilihan tidak ada!")
