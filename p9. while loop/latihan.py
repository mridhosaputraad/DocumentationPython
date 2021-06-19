# Struktur
# while argument:
#     statement
# Penjelasan, saat argumentnya (selama bernilai true) terpenuhi maka statement ini akan terus dilaksanakan


# Contoh 1 : Tipenya menggunakan syarat
angka = 0  # jadi, dia melakukan berdasarkan iterasi ini (0)

while angka < 5:
    print('nilai angka adalah', angka)  # Ini looping forever, solusinya:
    angka = angka + 1

print('di luar while')  # saat looping beres, barulah keluar ke sini


print(50*'=')
# Contoh 2 : Tipenya menggunakan boolean
start = True
angka = 0

while start:
    print('di dalam while')
    if angka == 10:
        start = False
        print('oke angka 10 diketemukan')
    angka += 1
