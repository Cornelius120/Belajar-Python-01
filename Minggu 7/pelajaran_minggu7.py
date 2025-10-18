"""
MINGGU 7 — PYTHON INTERMEDIATE ➜ ADVANCED
=====================================================
Topik:
1️⃣ Membaca & Menulis File JSON
2️⃣ Membaca & Menulis File CSV
3️⃣ Pengenalan OOP Lanjutan (Inheritance, Encapsulation)
4️⃣ Menggunakan Modul Eksternal (requests)

Catatan Modul:
"""

# Modul eksternal yang perlu diinstall:
# requests → install dengan: pip install requests
# Modul lainnya (json, csv, os) sudah built-in bawaan Python.

import json
import csv
import os
import requests


# =====================================================
# 1️⃣ Membaca & Menulis File JSON
# =====================================================
def simpan_data_json(data, nama_file="data.json"):
    """Menyimpan dictionary atau list ke file JSON"""
    try:
        with open(nama_file, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        print(f"Data berhasil disimpan ke {nama_file} ✅")
    except Exception as e:
        print("Gagal menyimpan file JSON:", e)


def baca_data_json(nama_file="data.json"):
    """Membaca data dari file JSON"""
    if not os.path.exists(nama_file):
        print("File JSON belum ada.")
        return None
    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            data = json.load(file)
        print(f"Isi {nama_file}:\n", data)
        return data
    except Exception as e:
        print("Gagal membaca file JSON:", e)


# =====================================================
# 2️⃣ Membaca & Menulis File CSV
# =====================================================
def simpan_data_csv(header, data, nama_file="data.csv"):
    """Menyimpan data list ke file CSV"""
    try:
        with open(nama_file, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(data)
        print(f"Data berhasil disimpan ke {nama_file} ✅")
    except Exception as e:
        print("Gagal menyimpan file CSV:", e)


def baca_data_csv(nama_file="data.csv"):
    """Membaca isi file CSV dan menampilkannya"""
    if not os.path.exists(nama_file):
        print("File CSV belum ada.")
        return
    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except Exception as e:
        print("Gagal membaca file CSV:", e)


# =====================================================
# 3️⃣ OOP Lanjutan (Inheritance & Encapsulation)
# =====================================================
class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
        self.__nilai = []  # Private attribute (encapsulation)

    def tambah_nilai(self, nilai):
        if 0 <= nilai <= 100:
            self.__nilai.append(nilai)
        else:
            print("Nilai harus antara 0 dan 100!")

    def rata_rata(self):
        return sum(self.__nilai) / len(self.__nilai) if self.__nilai else 0

    def tampilkan_info(self):
        print(f"Nama: {self.nama}, NIM: {self.nim}, Rata-rata: {self.rata_rata():.2f}")


class MahasiswaBeasiswa(Mahasiswa):
    def __init__(self, nama, nim, beasiswa):
        super().__init__(nama, nim)
        self.beasiswa = beasiswa

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Penerima Beasiswa: {self.beasiswa}")


# =====================================================
# 4️⃣ Modul Eksternal: Requests (API sederhana)
# =====================================================
def ambil_data_api(url="https://jsonplaceholder.typicode.com/posts/1"):
    """Mengambil data dari API menggunakan modul requests."""
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            print("Data berhasil diambil dari API:")
            print(json.dumps(data, indent=4))
            return data
        else:
            print(f"Gagal mengambil data (status: {response.status_code})")
    except requests.RequestException as e:
        print("Terjadi kesalahan koneksi:", e)


# =====================================================
# Menu Utama
# =====================================================
def main_menu():
    while True:
        print("\n=== MENU UTAMA - MINGGU 7 ===")
        print("1. Simpan & Baca File JSON")
        print("2. Simpan & Baca File CSV")
        print("3. Demo OOP Lanjutan")
        print("4. Ambil Data dari API (requests)")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            data = {
                "nama": "Miyamura",
                "pekerjaan": "Mahasiswa",
                "hobi": ["Manga", "Anime"],
            }
            simpan_data_json(data)
            baca_data_json()
        elif pilihan == "2":
            header = ["Nama", "Nilai"]
            data = [["Miyamura", 95], ["Izumi", 88], ["Hori", 92]]
            simpan_data_csv(header, data)
            baca_data_csv()
        elif pilihan == "3":
            m1 = MahasiswaBeasiswa("Miyamura", "12345", "Akademik")
            m1.tambah_nilai(90)
            m1.tambah_nilai(85)
            m1.tampilkan_info()
        elif pilihan == "4":
            ambil_data_api()
        elif pilihan == "5":
            print("Terima kasih! Program Minggu 7 selesai 👋")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")


if __name__ == "__main__":
    main_menu()
