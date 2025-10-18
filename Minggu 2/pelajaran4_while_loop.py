# Perulangan 'while' akan terus berjalan selama kondisinya True


angka = 1


while angka <= 5:  # ulangi selama angka kurang dari atau sama dengan 5
    print("Angka:", angka)
    angka += (
        1  # menambah nilai angka setiap iterasi untuk menghindari loop tak berujung
    )


print("Selesai!")
