# Program sederhana untuk mengelola data buku menggunakan OOP dan file handling


class Buku:
    def __init__(self, judul, penulis, tahun):
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun

    def tampilkan_info(self):
        return f"{self.judul} oleh {self.penulis} ({self.tahun})"


# List untuk menampung objek buku
koleksi_buku = []

# Input jumlah buku
total = int(input("Masukkan jumlah buku: "))

for i in range(total):
    print(f"\nData Buku ke-{i+1}")
    judul = input("Judul: ")
    penulis = input("Penulis: ")
    tahun = input("Tahun Terbit: ")

    buku = Buku(judul, penulis, tahun)
    koleksi_buku.append(buku)

# Simpan data buku ke file
with open("koleksi_buku.txt", "w") as file:
    for b in koleksi_buku:
        file.write(b.tampilkan_info() + "\n")

print("\nData buku berhasil disimpan ke file 'koleksi_buku.txt'.")


"""
📘 **Penjelasan:**

* Menggabungkan konsep `class`, `list`, dan `file handling`.
* Program menyimpan data buku ke file agar bisa dibuka nanti.
"""
