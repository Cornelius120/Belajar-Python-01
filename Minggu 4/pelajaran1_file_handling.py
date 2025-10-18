# File Handling digunakan untuk membaca dan menulis file
# Fungsi open() digunakan untuk membuka file
# Mode 'w' untuk menulis (write), 'r' untuk membaca (read), dan 'a' untuk menambah (append)

# Menulis ke file
with open("data.txt", "w") as file:
    # 'with' akan otomatis menutup file setelah selesai digunakan
    file.write("Halo, Miyamura! Ini adalah contoh penulisan file.\n")
    file.write("Baris kedua dari file ini.\n")

print("File berhasil dibuat dan ditulis.")

# Membaca isi file
with open("data.txt", "r") as file:
    isi = file.read()  # membaca seluruh isi file

print("Isi file:")
print(isi)


"""
📘 **Penjelasan:**

* `with open()` menjaga file tetap aman agar tertutup otomatis.
* Mode file:

  * `'w'` → tulis (hapus isi lama)
  * `'a'` → tambah di akhir
  * `'r'` → baca isi file
"""
