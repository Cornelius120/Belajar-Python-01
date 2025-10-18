# Dictionary menyimpan data dalam format pasangan kunci:nilai (key:value).
# Ini sangat berguna untuk data yang memiliki label, seperti data biodata.

# Membuat dictionary data diri
# "nama", "umur", "kota" adalah 'key' (kunci)
# "Miyamura", 21, "Tangerang" adalah 'value' (nilai)
data_diri = {
    "nama": "Miyamura", 
    "umur": 21, 
    "kota": "Tangerang",
    "sudah_menikah": False # Bisa menyimpan berbagai tipe data
}

print("--- Mengakses Data ---")
# Mengakses nilai berdasarkan kuncinya (key)
print(f"Nama saya: {data_diri['nama']}")
print(f"Umur saya: {data_diri['umur']} tahun")
print("-" * 20) # Mencetak garis pemisah

# --- Menambah & Mengubah Data ---
print("\n--- Menambah & Mengubah Data ---")
# Menambah pasangan key:value baru
data_diri["pekerjaan"] = "Mahasiswa"
print(f"Data setelah ditambah pekerjaan: {data_diri}")

# Mengubah nilai dari kunci yang sudah ada
data_diri["kota"] = "Jakarta"
print(f"Data setelah pindah kota: {data_diri}")
print("-" * 20)

# --- Perulangan pada Dictionary ---
print("\n--- Menampilkan Semua Data dengan Loop ---")
# Menggunakan method .items() untuk mendapatkan kunci dan nilai sekaligus
for kunci, nilai in data_diri.items():
    # .title() agar kuncinya jadi huruf kapital di awal
    print(f"{kunci.title()}: {nilai}")

"""
📘 **Penjelasan Tambahan:**

* **Kunci Unik:** Setiap kunci (key) dalam dictionary harus unik.
* **Fleksibel:** Dictionary sangat fleksibel untuk menstrukturkan data yang kompleks.
* **Kapan digunakan?** Gunakan Dictionary saat Anda punya data yang saling berhubungan dan setiap nilai punya label yang jelas. Gunakan List jika Anda hanya butuh urutan data biasa.
"""
