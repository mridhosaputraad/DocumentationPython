# Di Python ada beberapa struktur data, yakni list, tuple, set, dan dictionary.
# Kenapa harus menggunakan tuples? kalo kita punya sebuah data yang tidak bisa dirubah misal data sensus penduduk, data ktp, data member, id, dsb. Karena tuple lebih ringan daripada list untuk di proses.
# Karena struktur dari tuple lebih sederhana daripada list
# Membuat tuples sama seperti list


# List
Ganjil = [1, 3, 5, 7, 9]
Ganjil[2] = 99
Ganjil.append(2)

# Tuple
Genap = (2, 4, 6, 6, 8, 10)
# Genap[2] = 99 ini akan error
# Genap.append(2) ini akan error

print(type(Ganjil))
print(type(Genap))

# dir untuk mengetahui apa saja yang bisa dilakukan tipe data ini
# print(dir(Ganjil))
print(Genap.index(8))

# Jadi tuple berbeda dengan list.
# FYI
# Tuple ini nilainya tidak bisa dirubah, ditambah maupun dikurang karena sifatnya fix
