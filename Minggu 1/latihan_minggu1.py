# =================================================================
#               LATIHAN AKHIR MINGGU 1
# Tujuan: Menggabungkan semua konsep dari pelajaran 1-5.
# Konsep: Variabel, Tipe Data, Operator, Komentar, dan Print.
# =================================================================

# --- 1. DEKLARASI VARIABEL ---
# Kita akan membuat beberapa variabel untuk menyimpan biodata sederhana.
# Perhatikan penggunaan tipe data yang berbeda (string, integer, float).

nama_lengkap = "Miyamura Izumi"
tahun_lahir = 2003
tahun_sekarang = 2024
tinggi_badan = 172.5  # Menggunakan float untuk angka desimal
sudah_sarapan = True  # Menggunakan boolean

# --- 2. MENGGUNAKAN OPERATOR ARITMATIKA ---
# Kita akan menghitung umur berdasarkan tahun lahir dan tahun sekarang.
# Ini mempraktikkan operator pengurangan (-).

umur = tahun_sekarang - tahun_lahir

# --- 3. MENAMPILKAN HASIL DENGAN PRINT & F-STRING ---
# f-string (string yang diawali huruf 'f') adalah cara modern dan
# paling mudah untuk menggabungkan teks dengan nilai variabel.

print("--- BIODATA SEDERHANA ---")
print(f"Nama Lengkap   : {nama_lengkap}")
print(f"Tahun Lahir    : {tahun_lahir}")
print(f"Tinggi Badan   : {tinggi_badan} cm")
print(f"Sudah Sarapan? : {sudah_sarapan}")
print("=" * 25)  # Mencetak garis pemisah dengan operator perkalian (*)

print(
    f"Halo {nama_lengkap}! Berdasarkan perhitungan, umur Anda sekarang adalah {umur} tahun."
)

# --- 4. PREDIKSI SEDERHANA ---
# Mari kita gunakan operator penjumlahan (+) untuk memprediksi umur di masa depan.
tahun_prediksi = 10
umur_di_masa_depan = umur + tahun_prediksi

print(
    f"Dalam {tahun_prediksi} tahun lagi, umur Anda akan menjadi {umur_di_masa_depan} tahun."
)

"""
📘 **Rangkuman Latihan:**

Dalam file ini, kita berhasil:
1. Membuat variabel dengan tipe data String, Integer, Float, dan Boolean.
2. Menggunakan operator matematika (-) dan (+) untuk kalkulasi sederhana.
3. Menggunakan operator (*) pada string untuk membuat garis pemisah.
4. Menampilkan semua informasi secara rapi menggunakan f-string.

Ini adalah fondasi yang kuat untuk melanjutkan ke Minggu 2!
"""
