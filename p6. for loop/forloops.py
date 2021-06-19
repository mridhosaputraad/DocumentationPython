# list sebagai iterable
gorengan = ['bakwan', 'cireng', 'tahu isi', 'tempe goreng', 'ubi goreng']

for g in gorengan:  # artinya, g ini mengambil setiap komponen gorengan. g juga dapat diartikan variabel baru yang masih dalam scope gorengan
    print(g)
    print(len(g))


print(50*'=')
# string sebagai iterable
bakwan = 'bakwan'

for i in bakwan:
    print(i)  # artinya, i menghitung setiap huruf bakwan


print(50*'=')
# for di dalam for
buah = ['semangka', 'jeruk', 'apel', 'anggur']
sayur = ['kangkung', 'wortel', 'tomat', 'kentang']

Daftar_belanja = [gorengan, buah, sayur]

for subDaftarBelanja in Daftar_belanja:
    # artinya, subDaftarBelanja akan mengambil setiap isi list Daftar_belanja
    print(subDaftarBelanja)
    for komponen in subDaftarBelanja:
        # artinya, dia mengambil per komponen dari subDaftarBelanja
        print(komponen)
