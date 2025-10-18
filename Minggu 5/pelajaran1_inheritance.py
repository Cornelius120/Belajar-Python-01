# Inheritance (Pewarisan) memungkinkan satu class mewarisi atribut dan method dari class lain


# Class induk (Parent Class)
class Mahasiswa:
    def __init__(self, nama, jurusan):
        self.nama = nama
        self.jurusan = jurusan

    def info(self):
        print(f"Nama: {self.nama}, Jurusan: {self.jurusan}")


# Class anak (Child Class) yang mewarisi class Mahasiswa
class MahasiswaAktif(Mahasiswa):
    def __init__(self, nama, jurusan, semester):
        # Memanggil konstruktor dari class induk
        super().__init__(nama, jurusan)
        self.semester = semester

    def status(self):
        print(f"Mahasiswa {self.nama} sedang menempuh semester {self.semester}.")


# Membuat objek dari class turunan
mhs1 = MahasiswaAktif("Miyamura", "Informatika", 5)

# Memanggil method dari parent dan child class
mhs1.info()
mhs1.status()


"""
📘 **Penjelasan:**

* `super()` digunakan untuk memanggil konstruktor class induk.
* Pewarisan membantu menghindari duplikasi kode.
"""
