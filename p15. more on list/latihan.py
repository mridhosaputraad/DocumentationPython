barang = ['kunci', 'ember', 'jaket', 'ban', 'mobil']
print(barang)

# Beberapa method yang bisa digunakan untuk memanipulasi list
# 1. append fungsinya menambah data ke dalam list
barang.append('sepeda')
print(barang)

# 2. extend fungsinya mengambil iterables dari string
# Pengantar:
# data = 'test'   # string ini sifatnya iterables
# for i in data:
#     print(i)
barang.extend('dompet')
print(barang)

# 3. insert ini sifatnya fleksibel
barang.insert(3, 'sepeda')
print(barang)

# 4. count untuk menghitung anggota data
jumlahSepeda = barang.count('sepeda')
print('jumlah sepeda adalah: ', jumlahSepeda)

# 5. remove untuk menghapus data
barang.remove('sepeda')
print(barang)

# 6. reverse
barang.reverse()
print(barang)


# Kasus
print(50*'=')
stuff = barang.copy()   # di belakang layar yang terjadi ini membuat list baru
stuff.append('gelas')
print(stuff)
print(barang)  # karena append ini sifatnya menumpuk sedangkan yang kita ingin gelasnya tidak di tampilkan. cara mengatasinya dengan menambahkan .copy()
