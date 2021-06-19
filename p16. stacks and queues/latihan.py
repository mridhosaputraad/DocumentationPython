# FYI : Salah satu aplikasi dari list, kalo misalnya ada hubungannya dengan penumpukan data atau antrian dengan menggunakan python. Jadi rata-rata untuk simulasi event salah satunya menggunakan queue misalnya simulasi antrian rumah sakit.
# Perbedaan stack dan queue, kalo stack seperti tata lokasi sayuran di supermarket (perilakunya menumpuk), keluarnya di akhir. sedangkan queue, misalkan seperti antrian di restoran, jadi keluarnya yang pertama kali atau didepan.


# > Mensimulasikan stacks (tumpukan) LIFO
tumpukan = [1, 2, 3, 4, 5, 6]
print('data sekarang: ', tumpukan)

# Memamsukan data baru
tumpukan.append(7)
print('data masuk: ', 7)
print('data sekarang: ', tumpukan)
tumpukan.append(8)
print('data masuk: ', 8)
print('data sekarang: ', tumpukan)

out = tumpukan.pop()
# dia akan menghilangkan tumpukan di akhir. bedanya .pop() dengan .remove()
# .pop() menghapus data yang berada paling akhir
# .remove() menghapus data yang spesifikasi seperti LIKE kea list.remove(sepeda)
print('data keluar: ', out)
print('data sekarang: ', tumpukan)


print(50*'=')
# Kasus
barang = ['Sepatu', 'Sepeda', 'Tas', 'Kacamata']
i = 0

print('Contoh penumpukan dengan LOOP')
print('1.Tambah\n2.Hapus')
user = 'DEFAULT'

while user not in ['q', 'quit']:
    user = input('> ')

    if user == '1':
        while 1:
            i += 1
            item = input('Masukan barang %d: ' % i)
            if item == '':
                break   # akan mengakhiri LOOP jika user menekan enter.
            barang.append(item)
        print(barang)
    elif user == '2':
        print('Barang Sekarang')
        print(barang)
        print('Akan menghapus')
        print(barang)
        print('Barang sekarang baru New Terbaru')
        print(barang)
