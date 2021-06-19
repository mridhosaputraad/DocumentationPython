# Function, adalah membuat algoritma generic yang bisa dipanggil berulang-ulang. Misalnya:
# Mendefinisikan fungsi
def fungsi():
    print('ini adalah fungsi')


# Memanggil fungsi
fungsi()
print(50*'=')


# membuat fungsi sederhana
def suaraAyam():
    print('kukuruyuk!!!!')


def hargaAyam():
    suaraAyam()
    print('harga ayam per 1 kg adalah Rp. 20.000')


# membuat fungsi dengan input argumen
def hargaTotalAyam(kg):
    suaraAyam()
    harga = 20000
    hargaTotal = kg * harga
    print('harga', kg, 'ayam adalah', hargaTotal)


hargaAyam()
hargaTotalAyam(2)
