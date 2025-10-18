# Dictionary menyimpan pasangan key dan value
mahasiswa = {"nama": "Miyamura", "umur": 21, "jurusan": "Informatika"}

# Mengakses nilai berdasarkan key
print("Nama:", mahasiswa["nama"])
print("Umur:", mahasiswa["umur"])

# Menambah data baru
mahasiswa["IPK"] = 3.8
print("Data setelah ditambah:", mahasiswa)

# Menggunakan perulangan untuk menampilkan semua pasangan key-value
for kunci, nilai in mahasiswa.items():
    print(f"{kunci}: {nilai}")
