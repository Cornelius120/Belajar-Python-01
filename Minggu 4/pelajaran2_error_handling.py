# Error handling digunakan agar program tidak langsung berhenti saat ada error
# Gunakan try-except untuk menangkap kesalahan

try:
    angka = int(
        input("Masukkan angka: ")
    )  # bisa menyebabkan error jika input bukan angka
    hasil = 10 / angka  # bisa menyebabkan error jika angka = 0
    print("Hasil pembagian:", hasil)
except ValueError:
    # Terjadi jika input bukan angka
    print("Input harus berupa angka!")
except ZeroDivisionError:
    # Terjadi jika membagi dengan nol
    print("Tidak bisa membagi dengan nol!")
finally:
    # Selalu dijalankan, apapun hasilnya
    print("Program selesai dijalankan.")


"""
📘 **Penjelasan:**

* `try` → tempat kode yang mungkin error.
* `except` → menangani error tertentu.
* `finally` → dijalankan meskipun terjadi error.

"""
