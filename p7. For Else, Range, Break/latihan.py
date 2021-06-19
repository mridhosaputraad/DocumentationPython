# For Range
# for i in range(10, 40, 5):
#     # jadi ini seperti membuat virtualisasi
#     print(i)

# print(range(10, 40, 5))  # bisa jadi range ini sebuah class

print(50*'=')
# misal
number = 50

# Sederhananya
# for i in range(0, 5):
#     print(i)
# else:
#     # fungsi else ini akan dijalankan setelah proses for selesai
#     print('halo')

for i in range(0, 40):
    print(i)

    if i == number:
        print('angka ditemukan', i)
        break  # break ini akan mengeluarkan program dari proses looping/semua proses di atasnya
    # else:
        # misal angka tidak ditemukan, masalahnya adalah saat i nya (angka 1) masuk ke else yang bukan 25 maka dia akan menampilkan hasil angka tidak ditemukan
        # print('angka tidak ditemukan')
else:
    # fungsi ketika proses for sudah selesai, baru mengeksekusi sesuatu yang ada di else
    print('angka tidak ditemukan')

print("space di luar for")
