# scope variable : local & global
namaKucing = 'cassandra'    # variabel ini scopenya global
makananKucing = 'royal canin'


def ubahNamaKucing(namaBaru):
    global namaKucing     # cara mengakses variabel di scope global
    namaKucing = namaBaru   # variabel ini scopenya local
    print('saya ubah nama kucing menjadi', namaKucing)


def kasihMakanKucing(makanan, nama):
    global namaKucing, makananKucing
    namaKucing = nama
    makananKucing = makanan


ubahNamaKucing('ketie')
kasihMakanKucing('universal', 'alex')
print('nama kucing saya menjadi', namaKucing, 'dan makan', makananKucing)


# Contoh lainnya
namaNinja = 'naruto'
elemen = 'angin'


def daftarNinja(nama, kekuatan):
    global namaNinja, elemen
    namaNinja = nama
    elemen = kekuatan
    print('namanya adalah', nama, 'kekuatannya adalah', kekuatan)


daftarNinja('sai', 'lukisan')
print('nama :', namaNinja, 'kekuatan :', elemen)
