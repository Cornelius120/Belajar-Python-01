"""
MINGGU 6 — PROYEK AKHIR PYTHON DASAR (VERSI PERBAIKAN)
=====================================================
Kumpulan proyek mini untuk mempraktikkan semua yang telah dipelajari
dari Minggu 1 sampai 5.

Perbaikan dalam file ini:
- Adanya menu utama interaktif untuk memilih program.
- Penggunaan fungsi bantuan (helper function) untuk validasi input pengguna
  agar program tidak mudah error (crash).
- Setiap mini proyek dibuat dalam fungsi sendiri agar kode lebih rapi.
- Komentar yang lebih detail untuk menjelaskan setiap bagian.
"""

# Modul bawaan Python, tidak perlu install apa-apa.
import random
from datetime import datetime

# -----------------------------------------------------------
# Fungsi Bantuan (Helper Functions)
# -----------------------------------------------------------


def input_angka(prompt):
    """
    Fungsi ini secara aman meminta input angka dari pengguna.
    Akan terus meminta sampai pengguna memasukkan angka yang valid.
    Mengembalikan angka dalam bentuk integer.
    """
    while True:
        try:
            # Mencoba mengubah input menjadi integer
            angka = int(input(prompt))
            return angka
        except ValueError:
            # Jika terjadi error (misal, pengguna mengetik huruf),
            # beri pesan dan ulangi loop.
            print("Input tidak valid! Harap masukkan angka.")


# -----------------------------------------------------------
# 1. Mini Proyek: Game Tebak Angka
# -----------------------------------------------------------


def game_tebak_angka():
    """Menggabungkan modul 'random', loop 'while', dan logika 'if-elif-else'."""
    print("\n--- Selamat Datang di Game Tebak Angka! ---")
    angka_rahasia = random.randint(1, 20)
    kesempatan = 5

    print(
        f"Saya telah memilih sebuah angka antara 1 dan 20. Kamu punya {kesempatan} kesempatan."
    )

    while kesempatan > 0:
        print(f"\nKesempatan tersisa: {kesempatan}")
        tebakan = input_angka("Masukkan tebakanmu: ")

        kesempatan -= 1  # Kurangi kesempatan setiap kali menebak

        if tebakan < angka_rahasia:
            print("Terlalu kecil! Coba lagi.")
        elif tebakan > angka_rahasia:
            print("Terlalu besar! Coba lagi.")
        else:
            print(
                f"🎉 Selamat, {nama_pengguna}! Kamu berhasil menebak angkanya, yaitu {angka_rahasia}!"
            )
            return  # Keluar dari fungsi jika berhasil

    # Kode ini hanya akan berjalan jika loop selesai (kesempatan habis)
    print(
        f"\nSayang sekali, kesempatanmu habis. Angka rahasianya adalah {angka_rahasia}."
    )


# -----------------------------------------------------------
# 2. Mini Proyek: Kalkulator Sederhana
# -----------------------------------------------------------


def kalkulator():
    """Mempraktikkan fungsi, input, dan operasi matematika."""
    print("\n--- Kalkulator Sederhana ---")

    angka1 = input_angka("Masukkan angka pertama: ")
    angka2 = input_angka("Masukkan angka kedua: ")

    print("\nPilih Operasi:")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")

    pilihan = input("Masukkan pilihan (1/2/3/4): ")

    if pilihan == "1":
        hasil = angka1 + angka2
        print(f"Hasil: {angka1} + {angka2} = {hasil}")
    elif pilihan == "2":
        hasil = angka1 - angka2
        print(f"Hasil: {angka1} - {angka2} = {hasil}")
    elif pilihan == "3":
        hasil = angka1 * angka2
        print(f"Hasil: {angka1} * {angka2} = {hasil}")
    elif pilihan == "4":
        # Menangani pembagian dengan nol
        if angka2 == 0:
            print("Error! Tidak bisa membagi dengan nol.")
        else:
            hasil = angka1 / angka2
            print(f"Hasil: {angka1} / {angka2} = {hasil:.2f}")  # Format 2 angka desimal
    else:
        print("Pilihan tidak valid.")


# -----------------------------------------------------------
# 3. Mini Proyek: Pengelola Catatan (Simpan ke File)
# -----------------------------------------------------------


def pengelola_catatan():
    """Mempraktikkan File Handling (menulis ke file)."""
    print("\n--- Pengelola Catatan Harian ---")
    catatan = input("Tuliskan catatan untuk hari ini: ")

    # Mengambil waktu saat ini untuk dijadikan timestamp
    waktu_sekarang = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Menggunakan 'with open' agar file otomatis ditutup
    # Mode 'a' (append) untuk menambahkan catatan baru tanpa menghapus yang lama
    try:
        with open("catatan_harian.txt", "a") as file:
            file.write(f"[{waktu_sekarang}] {catatan}\n")
        print("Catatan berhasil disimpan ke file 'catatan_harian.txt'.")
    except Exception as e:
        print(f"Terjadi error saat menyimpan file: {e}")


# -----------------------------------------------------------
# Menu Utama Program
# -----------------------------------------------------------

# Baris 'if __name__ == "__main__":' adalah praktik standar di Python.
# Artinya, kode di dalam blok ini hanya akan berjalan jika file ini
# dieksekusi secara langsung (bukan di-import oleh file lain).
if __name__ == "__main__":
    nama_pengguna = input("Selamat datang! Siapa nama Anda? ")

    while True:
        print(f"\n=== Halo, {nama_pengguna}! Pilih Proyek yang Ingin Dijalankan ===")
        print("1. Game Tebak Angka")
        print("2. Kalkulator Sederhana")
        print("3. Tulis Catatan Harian")
        print("4. Keluar")

        pilihan_menu = input("Masukkan pilihan Anda (1-4): ")

        if pilihan_menu == "1":
            game_tebak_angka()
        elif pilihan_menu == "2":
            kalkulator()
        elif pilihan_menu == "3":
            pengelola_catatan()
        elif pilihan_menu == "4":
            print(f"Terima kasih sudah mencoba, {nama_pengguna}. Sampai jumpa!")
            break  # Keluar dari loop while dan program selesai
        else:
            print("Pilihan tidak valid. Silakan masukkan angka dari 1 sampai 4.")
