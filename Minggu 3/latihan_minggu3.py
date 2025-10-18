# Program untuk menyimpan dan menampilkan data mahasiswa
# Menggunakan list dan dictionary

daftar_mahasiswa = []  # list untuk menampung banyak mahasiswa

jumlah = int(input("Masukkan jumlah mahasiswa: "))

for i in range(jumlah):
    print(f"\nData Mahasiswa ke-{i+1}")
    nama = input("Nama: ")
    umur = int(input("Umur: "))
    jurusan = input("Jurusan: ")

    # Buat dictionary untuk setiap mahasiswa
    data = {"nama": nama, "umur": umur, "jurusan": jurusan}

    # Masukkan ke list utama
    daftar_mahasiswa.append(data)

# Menampilkan semua data mahasiswa
print("\n=== Daftar Mahasiswa ===")
for mhs in daftar_mahasiswa:
    print(f"Nama: {mhs['nama']}, Umur: {mhs['umur']}, Jurusan: {mhs['jurusan']}")
