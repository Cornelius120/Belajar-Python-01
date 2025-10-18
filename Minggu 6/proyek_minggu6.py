"""
MINGGU 6 — PROYEK AKHIR PYTHON (Diperbaiki)
=====================================================
Dokumen ini berisi beberapa proyek mini yang sudah diperbaiki agar siap dijalankan.
Perbaikan utama:
- Ditambahkan *main menu* untuk memilih program sehingga skrip langsung berguna.
- Semua input yang berisiko ValueError dilindungi dengan fungsi pembantu (try/except).
- Setiap fungsi dapat dijalankan sendiri dari menu, atau seluruh program berjalan dari main_menu().
- Komentar jelas menjelaskan jika ada module eksternal yang harus diinstall.
"""

# -----------------------------
# Catatan tentang modul
# -----------------------------
# """
# Semua modul yang digunakan pada file ini adalah modul bawaan Python (built-in):
# - datetime (pada catatan harian)
# - random (pada game tebak angka)
# Jadi **tidak perlu** melakukan `pip install` untuk menjalankan proyek-proyek ini.
# Jika di masa depan kita menambahkan modul eksternal, komentar akan menyebutkan perintah pip.
# """

from datetime import datetime
import random

# -----------------------------
# Fungsi pembantu: input aman
# -----------------------------


def input_int(prompt, minimum=None, maksimum=None):
    """
    Meminta input integer dari pengguna dengan penanganan error.
    Mengembalikan integer jika valid, atau None jika user membatalkan (ketik 'q').
    """
    while True:
        teks = input(prompt)
        if teks.strip().lower() == "q":
            return None
        try:
            nilai = int(teks)
            if minimum is not None and nilai < minimum:
                print(f"Masukkan angka minimal {minimum}.")
                continue
            if maksimum is not None and nilai > maksimum:
                print(f"Masukkan angka maksimal {maksimum}.")
                continue
            return nilai
        except ValueError:
            print("Input tidak valid! Masukkan angka atau ketik 'q' untuk kembali.")


def input_float(prompt, minimum=None, maksimum=None):
    """
    Meminta input float dari pengguna dengan penanganan error.
    Mengembalikan float jika valid, atau None jika user membatalkan (ketik 'q').
    """
    while True:
        teks = input(prompt)
        if teks.strip().lower() == "q":
            return None
        try:
            nilai = float(teks)
            if minimum is not None and nilai < minimum:
                print(f"Masukkan nilai minimal {minimum}.")
                continue
            if maksimum is not None and nilai > maksimum:
                print(f"Masukkan nilai maksimal {maksimum}.")
                continue
            return nilai
        except ValueError:
            print(
                "Input tidak valid! Masukkan angka (mis. 75.5) atau ketik 'q' untuk kembali."
            )


# -----------------------------
# 1️⃣ Sistem Login Sederhana
# -----------------------------
users = {"admin": "12345", "miyamura": "pythonrocks"}


def login():
    """
    Sistem login sederhana — tidak terhubung ke database.
    Ketik 'q' pada username untuk kembali ke menu utama.
    """
    print("=== SISTEM LOGIN SEDERHANA ===")
    username = input("Masukkan username (atau 'q' untuk kembali): ")
    if username.strip().lower() == "q":
        return
    password = input("Masukkan password: ")

    if username in users and users[username] == password:
        print(f"Selamat datang, {username}! ✅")
    else:
        print("Username atau password salah! ❌")


# -----------------------------
# 2️⃣ Aplikasi TODO List
# -----------------------------


def todo_app():
    """
    Aplikasi TODO sederhana.
    Ketik 'q' pada prompt menu untuk kembali ke menu utama.
    """
    todos = []

    while True:
        print("=== APLIKASI TODO LIST ===")
        print("1. Tambah tugas")
        print("2. Lihat tugas")
        print("3. Hapus tugas")
        print("4. Keluar ke menu utama")

        pilihan = input("Pilih menu (1-4): ")
        if pilihan.strip().lower() == "q" or pilihan == "4":
            print("Kembali ke menu utama...")
            break

        if pilihan == "1":
            tugas = input("Masukkan tugas baru: ")
            if tugas.strip():
                todos.append(tugas.strip())
                print("Tugas berhasil ditambahkan!")
            else:
                print("Tugas tidak boleh kosong.")
        elif pilihan == "2":
            if not todos:
                print("Belum ada tugas.")
            else:
                print("Daftar tugas:")
                for i, t in enumerate(todos, 1):
                    print(f"{i}. {t}")
        elif pilihan == "3":
            if not todos:
                print("Belum ada tugas untuk dihapus.")
                continue
            indeks = input_int(
                "Masukkan nomor tugas yang ingin dihapus (atau 'q' untuk batal): "
            )
            if indeks is None:
                print("Batal menghapus.")
                continue
            index = indeks - 1
            if 0 <= index < len(todos):
                hapus = todos.pop(index)
                print(f"Tugas '{hapus}' berhasil dihapus!")
            else:
                print("Nomor tugas tidak valid!")
        else:
            print("Pilihan tidak valid! Silakan pilih 1, 2, 3, atau 4.")


# -----------------------------
# 3️⃣ Konversi Nilai dan Penilaian
# -----------------------------


def konversi_nilai():
    """
    Mengonversi angka (0-100) menjadi predikat.
    Pengguna dapat ketik 'q' untuk kembali ke menu utama.
    """
    print("=== KONVERSI NILAI MAHASISWA ===")
    nilai = input_float("Masukkan nilai (0-100) atau 'q' untuk batal: ", 0, 100)
    if nilai is None:
        print("Dibatalkan.")
        return

    if nilai >= 90:
        predikat = "A"
    elif nilai >= 80:
        predikat = "B"
    elif nilai >= 70:
        predikat = "C"
    elif nilai >= 60:
        predikat = "D"
    else:
        predikat = "E"

    print(f"Nilai: {nilai}, Predikat: {predikat}")


# -----------------------------
# 4️⃣ Catatan Harian dengan Tanggal
# -----------------------------


def catatan_harian():
    """
    Menyimpan catatan ke file catatan.txt dengan timestamp.
    Menggunakan modul built-in 'datetime' — tidak perlu pip install.
    """
    print("=== CATATAN HARIAN ===")
    catatan = input("Tuliskan catatan hari ini (atau ketik 'q' untuk batal): ")
    if catatan.strip().lower() == "q" or not catatan.strip():
        print("Dibatalkan atau catatan kosong.")
        return

    waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open("catatan.txt", "a", encoding="utf-8") as file:
            file.write(f"[{waktu}] {catatan}")
        print("Catatan berhasil disimpan ke file catatan.txt ✅")
    except Exception as e:
        print("Terjadi kesalahan saat menyimpan file:", e)


# -----------------------------
# 5️⃣ Mini Game — Tebak Angka
# -----------------------------


def tebak_angka():
    """
    Game tebak angka antara 1 sampai 10.
    Input pengguna divalidasi agar tidak crash.
    """
    angka_rahasia = random.randint(1, 10)
    percobaan = 0

    print("=== GAME TEBAK ANGKA ===")
    print("Saya telah memilih angka antara 1 sampai 10. Ketik 'q' untuk menyerah.")

    while True:
        tebakan = input("Masukkan tebakanmu: ")
        if tebakan.strip().lower() == "q":
            print(f"Game berakhir. Angka rahasia adalah {angka_rahasia}.")
            return
        try:
            tebakan_int = int(tebakan)
        except ValueError:
            print("Masukkan angka yang valid (1-10) atau ketik 'q' untuk batal.")
            continue

        if not (1 <= tebakan_int <= 10):
            print("Masukkan angka antara 1 dan 10.")
            continue

        percobaan += 1

        if tebakan_int < angka_rahasia:
            print("Terlalu kecil!")
        elif tebakan_int > angka_rahasia:
            print("Terlalu besar!")
        else:
            print(
                f"Selamat! Kamu menebak dengan benar dalam {percobaan} kali percobaan 🎉"
            )
            break


# -----------------------------
# Menu Utama
# -----------------------------


def main_menu():
    """
    Menu utama untuk memilih salah satu proyek.
    Jalankan program ini dengan: python nama_file.py
    """
    while True:
        print("=== MENU UTAMA - MINGGU 6 ===")
        print("1. Sistem Login Sederhana")
        print("2. Aplikasi TODO List")
        print("3. Konversi Nilai dan Penilaian")
        print("4. Catatan Harian (simpan ke file)")
        print("5. Mini Game - Tebak Angka")
        print("6. Keluar")

        pilihan = input("Pilih program (1-6): ")
        if pilihan == "1":
            login()
        elif pilihan == "2":
            todo_app()
        elif pilihan == "3":
            konversi_nilai()
        elif pilihan == "4":
            catatan_harian()
        elif pilihan == "5":
            tebak_angka()
        elif pilihan == "6" or pilihan.strip().lower() == "q":
            print("Terima kasih! Sampai jumpa 👋")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih antara 1 sampai 6.")


if __name__ == "__main__":
    main_menu()
