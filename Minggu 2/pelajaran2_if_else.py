# Percabangan digunakan untuk membuat keputusan berdasarkan kondisi
# Sintaks dasar:
# if kondisi:
# kode jika benar
# else:
# kode jika salah


umur = int(
    input("Masukkan umur kamu: ")
)  # input selalu string, jadi perlu dikonversi ke int


if umur >= 18:
    print("Kamu sudah dewasa!")
elif umur >= 13:
    print("Kamu masih remaja.")
else:
    print("Kamu masih anak-anak.")
