# Modul adalah file Python (.py) yang berisi fungsi atau class dan bisa digunakan ulang di file lain
# Misalnya kita punya file bernama 'matematika.py' berisi fungsi-fungsi matematika

# ======== File: matematika.py ========
# def tambah(a, b):
#     return a + b
#
# def kali(a, b):
#     return a * b

# ======== File utama ========
import matematika  # mengimpor modul matematika

print("Hasil tambah:", matematika.tambah(5, 3))
print("Hasil kali:", matematika.kali(4, 2))

"""
📘 **Penjelasan:**

* File modul harus berada di folder yang sama atau di path yang dikenali Python.
* Kita bisa membuat package dengan menambahkan file `__init__.py` dalam folder.
"""
