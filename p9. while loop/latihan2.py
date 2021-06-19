# Contoh 3 : else, continue, pass
angka = 0

while angka < 10:

    if angka == 5:
        # print('checkpoint 1')
        # break
        # jadi akan langsung keluar dari looping

        # Solusinya
        # angka += 1
        # continue
        # Dia tidak error, tapi akan stack di angka 5 jadinya posisinya infinite loop

        pass

    print('nilai angka adalah', angka)
    angka += 1
else:
    # Fungsinya nengecek status bahwa while sudah beres
    print('nilai angka diakhir while adalah', angka)
    # angka terakhir ini bisa kita catch dengan else

print('di luar while')
