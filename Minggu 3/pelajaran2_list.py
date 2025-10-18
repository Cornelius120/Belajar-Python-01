# List digunakan untuk menyimpan banyak nilai dalam satu variabel
buah = ["apel", "mangga", "jeruk"]

# Mengakses elemen list berdasarkan indeks (dimulai dari 0)
print("Buah pertama:", buah[0])

# Menambahkan item ke dalam list
buah.append("pisang")  # menambah item di akhir
print("Setelah ditambah pisang:", buah)

# Menghapus item
buah.remove("mangga")  # menghapus berdasarkan nama item
print("Setelah dihapus mangga:", buah)

# Menggunakan perulangan untuk menampilkan semua item
for item in buah:
    print("Saya suka", item)
