# Fungsi adalah blok kode yang bisa digunakan berulang kali
# Fungsi dibuat menggunakan kata kunci 'def'


# Contoh fungsi sederhana
def sapa(nama):
    # Fungsi ini menampilkan sapaan
    print(f"Halo, {nama}! Selamat belajar Python.")


# Memanggil fungsi
sapa("Miyamura")


# Fungsi dengan nilai kembalian (return)
def tambah(a, b):
    # Mengembalikan hasil penjumlahan dua angka
    return a + b


hasil = tambah(5, 3)
print("Hasil penjumlahan:", hasil)
