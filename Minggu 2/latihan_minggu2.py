# Program sederhana untuk menghitung nilai akhir siswa
# Mempraktikkan input, if-else, dan perulangan

jumlah_siswa = int(input("Masukkan jumlah siswa: "))  # input jumlah siswa

for i in range(jumlah_siswa):
    print("\nSiswa ke-", i + 1)
    nama = input("Nama siswa: ")
    nilai = float(input("Masukkan nilai: "))

    # Mengevaluasi nilai
    if nilai >= 90:
        predikat = "A"
    elif nilai >= 75:
        predikat = "B"
    elif nilai >= 60:
        predikat = "C"
    else:
        predikat = "D"

    print(f"Hasil: {nama} mendapatkan nilai {predikat}")
