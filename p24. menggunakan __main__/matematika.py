def tambah(a, b):
    print(a, '+', b, '=', a+b)


def kurang(a, b):
    print(a, '-', b, '=', a-b)


def main():
    print('ini adalah fungsi utama dari matematika')


if __name__ == '__main__':
    main()

# print(__name__)
# Dia akan jadi __main__
# Ketika di main.py, __main__ ini berubah menjadi matematika
# Fungsi dari __main__ ini untuk menjalankan fungsi yang ditandai dengan adanya "if __name__ == __main__: namafungsi()".
# Nah namafungsi() ini lah yang pertama kali di jalankan, intinya sama kaya fungsi-fungsi main yang ada di java dan c++ dimana fungsi main tersebut dieksekusi pertama kali

# FYI
# is memeriksa memori
# == memeriksa nilai
